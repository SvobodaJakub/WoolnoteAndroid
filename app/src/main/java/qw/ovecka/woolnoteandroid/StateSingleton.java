package qw.ovecka.woolnoteandroid;


import android.content.SharedPreferences;
import android.content.res.AssetManager;
import android.util.Log;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Map;

/**
 * Created by Jakub Svoboda on 20.1.17.
 */

class StateSingleton {
    private static StateSingleton stateSingleton = new StateSingleton();
    private final Object lock = new Object();
    private Thread nativeProcessThread = null;
    private String dataDir = null; // getApplicationContext().getApplicationInfo().dataDir;
    private String filesDir = null; // getApplicationContext().getFilesDir().getAbsolutePath();
    private Boolean startupOnceHappened = false;
    private AssetManager assetManager = null; // getAssets();
    private String loginPassword = Util.GenerateSecureRandomString();
    private SharedPreferences sharedPreferences = null; // PreferenceManager.getDefaultSharedPreferences(this);
    private String prefNameDefaultLoginPassword = null; // getString(R.string.pref_name_login_password);
    private String prefNameKillServer = null; // getString(R.string.pref_name_kill_server_activity_destroy);
    private String prefNameImportExportDir = null; // getString(R.string.pref_name_import_export_dropbox_sync_dir);
    private String prefDefaultValueImportExportDir = null; // getString(R.string.pref_name_import_export_dropbox_sync_dir);


    // private prevents instantiation
    private StateSingleton() {
    }

    protected static StateSingleton getInstance() {
        return stateSingleton;
    }


    protected void GenerateHttpsCert() {
        // TODO reused paths to shared variables
        String cert_folder_name = "https_cert";
        String cert_dir_path = GetFilesDirPath() + "/" + cert_folder_name;
        String openssl_path = GetDataDirPath() + "/lib/libopeXssX.so";
        String openssl_config_dir_path = GetFilesDirPath() + "/assets";
        String openssl_config_file_path = openssl_config_dir_path + "/openssl.cnf";

        // TODO: use Java instead of unix commands?
        // delete the old https_cert folder
        processExec("cd '" + GetFilesDirPath() + "' && rm -rf '" + cert_folder_name + "' && ls -la", Constants.DebugLogcat, false);
        // create a new https_cert folder
        processExec("cd '" + GetFilesDirPath() + "' && mkdir '" + cert_folder_name + "' && ls -la", Constants.DebugLogcat, false);

        String commandToGenCert = String.format("cd '%s' && ls -la && OPENSSL_CONF='%s' '%s' req -x509 -newkey rsa:4096 -days 10000 -nodes -config '%s' -subj \"/C=XX/L=Default City/O=Default Company Ltd\" -keyout key.pem -out cert.pem && ls -la",
                cert_dir_path,
                openssl_config_dir_path,
                openssl_path,
                openssl_config_file_path);
        processExec(commandToGenCert, Constants.DebugLogcat, false);

        String commandToGetCertHash = String.format("cd '%s' && ls -la && OPENSSL_CONF='%s' '%s' x509 -in cert.pem -noout -sha256 -fingerprint > hash.txt && cat hash.txt",
                cert_dir_path,
                openssl_config_dir_path,
                openssl_path);
        processExec(commandToGetCertHash, Constants.DebugLogcat, false);

    }

    // beware of shell escaping
    // runs in the current thread and blocks
    // TODO even though I consume stdin/stderr, Thread.interrupt() doesn't work - despite this link telling otherwise? - https://stackoverflow.com/questions/18113941/thread-launched-running-processes-wont-destroy-java
    // - Most probably, it is this problem and I can't fix it - https://stackoverflow.com/questions/21279270/android-can-native-code-get-broadcast-intent-from-android-system/21337119#answer-21337119
    protected String processExec(String shellCommand, Boolean logEnabled, Boolean throwAwayInOut) {

        int sleepInterval = 100; // 100 ms
        int numOfSleeps = 0;
        String returnOutput = "";

        if (logEnabled) Log.d("WOOLNOTE", "processExec begin - " + shellCommand);
        Runtime runtime = Runtime.getRuntime();
        try {
            Process process = runtime.exec(new String[]{"/system/bin/sh", "-c", shellCommand});
            //process.getErrorStream().close();
            process.getOutputStream().close();
            InputStream inputStream = process.getInputStream();
            InputStream errorStream = process.getErrorStream();
            Boolean processAlive = true;
            try {
                // the following is instead of process.waitFor();
                // consume stdout and stderr so that the process doesn't get blocked
                // https://stackoverflow.com/questions/646940/why-does-javas-inputstream-close-block/646969#646969
                while (processAlive) {
                    int nInput = inputStream.available();
                    int nError = errorStream.available();
                    if (nInput > 0) {
                        if (throwAwayInOut) {
                            inputStream.skip(nInput);
                        } else {
                            byte[] b = new byte[nInput];
                            nInput = inputStream.read(b, 0, nInput);
                            if (nInput > 0) {
                                String s = new String(b, 0, nInput);
                                if (logEnabled) Log.d("WOOLNOTE", "stdout: " + s);
                                returnOutput += s;
                            }
                        }
                    }
                    if (nError > 0) {
                        if (throwAwayInOut) {
                            errorStream.skip(nError);
                        } else {
                            byte[] b = new byte[nError];
                            nError = errorStream.read(b, 0, nError);
                            if (nError > 0) {
                                String s = new String(b, 0, nError);
                                if (logEnabled) Log.d("WOOLNOTE", "stdout: " + s);
                                returnOutput += s;
                            }
                        }
                    }
                    try {
                        processAlive = false;
                        process.exitValue(); // throws if the process is still running
                    } catch (IllegalThreadStateException e) {
                        processAlive = true;
                        if (numOfSleeps < 200) {
                            // make sleep intervals progressively longer to a certain extent
                            ++numOfSleeps;
                            if (numOfSleeps > 160) {
                                // after 10 * 0.1 + 90 * 0.5 + 50 * 1 + 10 * 10 = 1 + 45 + 50 + 100 = 196 s
                                sleepInterval = 60 * 1000; // 60s
                            } else if (numOfSleeps > 150) {
                                // after 10 * 0.1 + 90 * 0.5 + 50 * 1 = 1 + 45 + 50 = 96 s
                                sleepInterval = 10 * 1000; // 10s
                            } else if (numOfSleeps > 100) {
                                // after 10 * 0.1 + 90 * 0.5 = 1 + 45 = 46 s
                                sleepInterval = 1 * 1000; // 1s
                            } else if (numOfSleeps > 10) {
                                // after 10 * 0.1 = 1 s
                                sleepInterval = 500; // 500 ms
                            }

                        }
                        Thread.sleep(sleepInterval);
                    }
                }
                if (logEnabled) Log.d("WOOLNOTE", "waitFor ended on its own");
            } catch (InterruptedException e) {
                if (logEnabled) Log.d("WOOLNOTE", "thread interrupted, killing");
                process.destroy(); // after waitFor if thread interrupted
                if (logEnabled) Log.d("WOOLNOTE", "process.destroy() returned");
            }

            if (!throwAwayInOut) {
                // read the remaining stdout
                // TODO also read stderr
                InputStream stdoutIS = process.getInputStream();
                BufferedReader stdoutBR = new BufferedReader(new InputStreamReader(stdoutIS));
                String stdout = "";
                String line;
                while ((line = stdoutBR.readLine()) != null) {
                    stdout += "\n" + line;
                }
                if (logEnabled) Log.d("WOOLNOTE", "remaining stdout: " + stdout);
                returnOutput += stdout;
                process.getInputStream().close();
            } else {
                if (logEnabled) Log.d("WOOLNOTE", "no stdout because throwAwayInOut==true");
            }


        } catch (Throwable e) {
            if (logEnabled) e.printStackTrace();
        }
        if (logEnabled) Log.d("WOOLNOTE", "processExec end - " + shellCommand);

        return returnOutput;
    }

    // runs in the current thread and blocks
    //TODO doesn't work for some reason
    protected void processExec(String[] cmdArray, String[] envp, File dir, Boolean logEnabled, Boolean throwAwayInOut) {

        int sleepInterval = 100; // 100 ms
        int numOfSleeps = 0;

        if (logEnabled) Log.d("WOOLNOTE", "processExec2 begin - " + Arrays.toString(cmdArray));
        if (logEnabled) Log.d("WOOLNOTE", "processExec2 envp - " + Arrays.toString(envp));
        if (logEnabled) Log.d("WOOLNOTE", "processExec2 dir - " + dir.getAbsolutePath());
        if (logEnabled)
            Log.d("WOOLNOTE", "processExec2 dir exists - " + Boolean.toString(dir.exists()));
        ProcessBuilder pb = new ProcessBuilder(cmdArray);
        Map<String, String> env = pb.environment();
        for (String envPairStr : envp) {
            String key = "";
            String value = "";
            String[] pair = envPairStr.split("=");
            key = pair[0];
            value = pair[1];
            env.put(key, value);
        }
        pb.directory(dir);


        //Runtime runtime = Runtime.getRuntime();
        try {
            //Process process = runtime.exec(cmdArray, envp, dir);
            Process process = pb.start();
            //process.getErrorStream().close();
            //process.getOutputStream().close(); //TODO?
            InputStream inputStream = process.getInputStream();
            InputStream errorStream = process.getErrorStream();
            Boolean processAlive = true;
            try {
                // the following is instead of process.waitFor();
                // consume stdout and stderr so that the process doesn't get blocked
                // https://stackoverflow.com/questions/646940/why-does-javas-inputstream-close-block/646969#646969
                while (processAlive) {
                    int nInput = inputStream.available();
                    int nError = errorStream.available();
                    if (nInput > 0) {
                        if (throwAwayInOut) {
                            inputStream.skip(nInput);
                        } else {
                            byte[] b = new byte[nInput];
                            nInput = inputStream.read(b, 0, nInput);
                            if (nInput > 0) {
                                String s = new String(b, 0, nInput);
                                if (logEnabled) Log.d("WOOLNOTE", "stdout: " + s);
                            }
                        }
                    }
                    if (nError > 0) {
                        if (throwAwayInOut) {
                            errorStream.skip(nError);
                        } else {
                            byte[] b = new byte[nError];
                            nError = errorStream.read(b, 0, nError);
                            if (nError > 0) {
                                String s = new String(b, 0, nError);
                                if (logEnabled) Log.d("WOOLNOTE", "stdout: " + s);
                            }
                        }
                    }
                    try {
                        processAlive = false;
                        process.exitValue(); // throws if the process is still running
                    } catch (IllegalThreadStateException e) {
                        processAlive = true;
                        if (numOfSleeps < 200) {
                            // make sleep intervals progressively longer to a certain extent
                            ++numOfSleeps;
                            if (numOfSleeps > 160) {
                                // after 10 * 0.1 + 90 * 0.5 + 50 * 1 + 10 * 10 = 1 + 45 + 50 + 100 = 196 s
                                sleepInterval = 60 * 1000; // 60s
                            } else if (numOfSleeps > 150) {
                                // after 10 * 0.1 + 90 * 0.5 + 50 * 1 = 1 + 45 + 50 = 96 s
                                sleepInterval = 10 * 1000; // 10s
                            } else if (numOfSleeps > 100) {
                                // after 10 * 0.1 + 90 * 0.5 = 1 + 45 = 46 s
                                sleepInterval = 1 * 1000; // 1s
                            } else if (numOfSleeps > 10) {
                                // after 10 * 0.1 = 1 s
                                sleepInterval = 500; // 500 ms
                            }

                        }
                        Thread.sleep(sleepInterval);
                    }
                }
                if (logEnabled) Log.d("WOOLNOTE", "waitFor ended on its own");
            } catch (InterruptedException e) {
                if (logEnabled) Log.d("WOOLNOTE", "thread interrupted, killing");
                process.destroy(); // after waitFor if thread interrupted
                if (logEnabled) Log.d("WOOLNOTE", "process.destroy() returned");
            }

            if (!throwAwayInOut) {
                InputStream stdoutIS = process.getInputStream();
                BufferedReader stdoutBR = new BufferedReader(new InputStreamReader(stdoutIS));
                String stdout = "";
                String line;
                while ((line = stdoutBR.readLine()) != null) {
                    stdout += "\n" + line;
                }
                if (logEnabled) Log.d("WOOLNOTE", "remaining stdout: " + stdout);
                process.getInputStream().close();
            } else {
                if (logEnabled) Log.d("WOOLNOTE", "no stdout because throwAwayInOut==true");
            }


        } catch (Throwable e) {
            if (logEnabled) e.printStackTrace();
        }
        if (logEnabled) Log.d("WOOLNOTE", "processExec2 end - " + Arrays.toString(cmdArray));

    }

    protected void SetAssetManager(AssetManager assetManager) {
        synchronized (lock) {
            if (this.assetManager != null) {
                //throw new UnsupportedOperationException("SetAssetManager() can only be called once.");
                return;
            }
            this.assetManager = assetManager;
        }
    }

    protected AssetManager GetAssetManager() {
        synchronized (lock) {
            if (this.assetManager == null) {
                throw new NullPointerException("SetAssetManager() must be called before GetAssetManager().");
            }
            return this.assetManager;
        }
    }

    protected void SetDataDirPath(String dataDir) {
        synchronized (lock) {
            if (this.dataDir != null) {
                //throw new UnsupportedOperationException("SetDataDirPath() can only be called once.");
                return;
            }
            this.dataDir = dataDir;
        }
    }

    protected String GetDataDirPath() {
        synchronized (lock) {
            if (this.dataDir == null) {
                throw new NullPointerException("SetDataDirPath() must be called before GetDataDirPath().");
            }
            return this.dataDir;
        }
    }

    protected void SetFilesDirPath(String filesDir) {
        synchronized (lock) {
            if (this.filesDir != null) {
                //throw new UnsupportedOperationException("SetFilesDirPath() can only be called once.");
                return;
            }
            this.filesDir = filesDir;
        }
    }

    protected String GetFilesDirPath() {
        synchronized (lock) {
            if (this.filesDir == null) {
                throw new NullPointerException("SetFilesDirPath() must be called before GetFilesDirPath().");
            }
            return this.filesDir;
        }
    }

    protected void SetSharedPreferences(SharedPreferences sharedPref) {
        synchronized (lock) {
            if (this.sharedPreferences != null) {
                //throw new UnsupportedOperationException("SetSharedPreferences() can only be called once.");
                return;
            }
            this.sharedPreferences = sharedPref;
        }
    }

    protected SharedPreferences GetSharedPreferences() {
        synchronized (lock) {
            if (this.sharedPreferences == null) {
                throw new NullPointerException("SetSharedPreferences() must be called before GetSharedPreferences().");
            }
            return this.sharedPreferences;
        }
    }

    protected void StartProcess() {
        synchronized (lock) {
            if (this.nativeProcessThread != null) {
                return;
            }

            if (nativeGetServerRunning()) {
                return;
            }

            this.nativeProcessThread = new Thread(new Runnable() {
                public void run() {
                    try {
                        //TODO
                        Thread.sleep(1000); // give any remaining processes that are being killed a little time

                        String hello_py_path = GetFilesDirPath() + "/assets/hello.py";
                        String woolnote_dir_path = GetFilesDirPath() + "/assets/woolnote";
                        String woolnote_main_path = woolnote_dir_path + "/woolnote.py";
                        String pythonhome_path = GetFilesDirPath() + "/assets";
                        String python_path = GetDataDirPath() + "/lib/libpython35woolnote.so";

                        String cert_folder_name = "https_cert";
                        String cert_dir_path = GetFilesDirPath() + "/" + cert_folder_name;
                        String cert_hash_file_path = cert_dir_path + "/hash.txt";
                        String cert_hash = "";
                        try {
                            cert_hash = Util.SmallFileIntoString(new File(cert_hash_file_path));
                        } catch (Throwable e) {
                            cert_hash = "error while reading https cert hash";
                        }
                        cert_hash = Util.SimpleSanitizeShellString(cert_hash);
                        cert_hash = cert_hash.replaceAll("=", " = ").replaceAll(":", " ").replaceAll("_", "");

                        String path_save_db = "/sdcard/woolnote";
                        String path_save_db_backup = "/sdcard/woolnote/backups";
                        String login_password = Util.SimpleSanitizeShellString(GetLoginPassword()).replaceAll("_", "");
                        String import_export_path = Util.SimpleSanitizeShellString(GetPrefImportExportDir()).replaceAll("_", "");


                        // without $HOME, python fails - https://bugs.python.org/issue10496

                        String woolnoteHardcodedEnvVar = String.format(" WOOLNOTE_HARDCODE_SSL_CERT_HASH='%s' WOOLNOTE_HARDCODE_PATH_CERT='%s' WOOLNOTE_HARDCODE_PATH_SAVE_DB='%s' WOOLNOTE_HARDCODE_PATH_SAVE_DB_BACKUP='%s' WOOLNOTE_HARDCODE_LOGIN_PASSWORD='%s' WOOLNOTE_HARDCODE_PATH_DROPBOX_SYNC='%s' ",
                                cert_hash,
                                cert_dir_path,
                                path_save_db,
                                path_save_db_backup,
                                login_password,
                                import_export_path);

                        String commandToRunPython = String.format("cd '%s' && %s LANG=C.utf-8 HOME='%s' PYTHONIOENCODING=utf-8 PYTHONUTF8=1 PYTHONHOME='%s' '%s' -B '%s' ",
                                woolnote_dir_path,
                                woolnoteHardcodedEnvVar,
                                pythonhome_path,
                                pythonhome_path,
                                python_path,
                                woolnote_main_path);

                        // note: if debug logging is enabled, snooping logcat reveals the login password
                        processExec(commandToRunPython, Constants.DebugLogcat, false);

                    } catch (Throwable e) {
                        //if (logEnabled) e.printStackTrace();

                        // possible race condition where it calls StopProcess() after someone calls another StartProcess(), resulting in killing the process again
                        // make sure that nativeProcessThread==null so that it can be started again
                        StopProcess();
                    }
                }
            });

            try {
                this.nativeProcessThread.start();
            } catch (Throwable e) {
                //e.printStackTrace();
            }
        }
    }

    private void nativeKillProcess() {

        // android 4.4 - toolbox grep works
        // android N - toolbox grep - no such tool
        // using whatever grep is in PATH
        // using toolbox ps so that the output format is well known and no other ps program is used (still might break in future android versions..)
        processExec("toolbox ps | grep libpython35woolnote.so | grep -v PID | while read l ; do arr=($l); echo kill -9 ${arr[1]}; done", Constants.DebugLogcat, false);
        processExec("toolbox ps | grep libpython35woolnote.so | grep -v PID | while read l ; do arr=($l); kill -9 ${arr[1]}; done", Constants.DebugLogcat, false);

    }

    private Boolean nativeGetServerRunning() {
        String stdout = processExec("toolbox ps | grep libpython35woolnote.so | grep -v PID | while read l ; do arr=($l); echo kill -9 ${arr[1]}; done", Constants.DebugLogcat, false).trim();
        return (stdout.length() > 0);
    }

    protected void StopProcess() {
        synchronized (lock) {
            if (this.nativeProcessThread == null) {
                return;
            }

            nativeKillProcess();

            this.nativeProcessThread.interrupt();  //TODO: this alone doesn't work

            try {
                Thread.sleep(500); // give it a little time
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            this.nativeProcessThread = null;
        }

        // wait outside of the lock so that the caller is blocked and the thread can call StopProcess() on its own, eliminating race conditions as long as only one thread (activity/service) generally makes requests to start/stop
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    //TODO use http://stackoverflow.com/questions/3853472/creating-a-directory-in-sdcard-fails instead of /sdcard
    private Boolean createSdcardFilesIfNotExisting() {
        File woolnoteDir = new File("/sdcard", "woolnote");
        woolnoteDir.mkdir();
        File backupsDir = new File("/sdcard/woolnote", "backups");
        backupsDir.mkdir();
        File taskDat = new File("/sdcard/woolnote/", "tasks.dat");
        try {
            if (!taskDat.exists()) {

                taskDat.createNewFile();

            }
            File taskTrashDat = new File("/sdcard/woolnote/", "tasks_trash.dat");
            if (!taskTrashDat.exists()) {
                taskTrashDat.createNewFile();
            }
        } catch (IOException e) {
            //e.printStackTrace();
        }

        Boolean allOK = true;
        allOK &= (new File("/sdcard/woolnote/", "tasks.dat")).exists();
        allOK &= (new File("/sdcard/woolnote/", "tasks_trash.dat")).exists();
        allOK &= (new File("/sdcard/woolnote", "backups")).exists();

        return allOK;
    }

    protected void SetPrefNameDefaultLoginPassword(String prefName) {
        prefNameDefaultLoginPassword = prefName;
    }

    protected void SetPrefNameKillServer(String prefName) {
        prefNameKillServer = prefName;
    }

    protected void SetPrefNameImportExportDir(String prefName) {
        prefNameImportExportDir = prefName;
    }

    protected void SetPrefDefaultValueImportExportDir(String prefName) {
        prefDefaultValueImportExportDir = prefName;
    }

    protected String GetPrefLoginPassword() {
        String prefLoginPassword = sharedPreferences.getString(prefNameDefaultLoginPassword, "");
        prefLoginPassword = prefLoginPassword.replaceAll("<", "").replaceAll("&", "").replaceAll("\\?", "").replaceAll(" ", "").trim();
        return prefLoginPassword;
    }

    protected Boolean GetPrefKillServer() {
        Boolean prefKillServer = sharedPreferences.getBoolean(prefNameKillServer, true);
        return prefKillServer;
    }

    protected String GetPrefImportExportDir() {
        String prefImportExportDir = sharedPreferences.getString(prefNameImportExportDir, prefDefaultValueImportExportDir);
        return prefImportExportDir;
    }

    protected void StartupRunOnce() {
        synchronized (lock) {
            if (this.startupOnceHappened) {
                return;
            }

            if (GetPrefKillServer()) {
                nativeKillProcess(); // on Android 4.4 (and possibly others), the process might be still running because the OS can't Force Stop the native process, hence this killing
            }

            if (GetPrefLoginPassword().length() > 0) {
                loginPassword = GetPrefLoginPassword();
            }

            if (!nativeGetServerRunning()) {
                Log.d("WOOLNOTE", "nativeGetServerRunning==false");

                //TODO: a more elegant way to delete the existing files
                String commandToCleanFiles = String.format("cd '%s' && pwd && ls -la && rm -rf assets && pwd && ls -la && echo cleaned",
                        GetFilesDirPath());
                processExec(commandToCleanFiles, Constants.DebugLogcat, false);

                AssetExtractor.copyAssetFolder(GetAssetManager(), "files", GetFilesDirPath() + "/assets");

                createSdcardFilesIfNotExisting();


                String cert_folder_name = "https_cert";
                String cert_dir_path = GetFilesDirPath() + "/" + cert_folder_name; //TODO into a shared var
                File certFile = new File(cert_dir_path + "/cert.pem");
                if (!certFile.exists()) {
                    Log.d("WOOLNOTE", "cert.pem doesn't exist, probably the first run");
                    GenerateHttpsCert();
                } else {
                    Log.d("WOOLNOTE", "cert.pem exists, probably not the first run");
                }

            } else {
                Log.d("WOOLNOTE", "nativeGetServerRunning==true");
            }

            this.startupOnceHappened = true;
        }
    }

    protected String GetLoginPassword() {
        return loginPassword;
    }

}
