package qw.ovecka.woolnoteandroid;

import android.content.Intent;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.text.TextUtils;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.WebSettings;
import android.webkit.WebView;

public class MainActivity extends AppCompatActivity {

    // TODO: ensure that all files have appropriate permissions (other apps can't access them)
    // TODO: ? implement up and back buttons correctly - https://developer.android.com/design/patterns/navigation.html#up-vs-back

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

/*        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });*/

        StateSingleton stateSingleton = StateSingleton.getInstance();
        stateSingleton.SetDataDirPath(getApplicationContext().getApplicationInfo().dataDir);
        stateSingleton.SetFilesDirPath(getApplicationContext().getFilesDir().getAbsolutePath());
        stateSingleton.SetAssetManager(getAssets());
        stateSingleton.SetSharedPreferences(PreferenceManager.getDefaultSharedPreferences(this));
        stateSingleton.SetPrefNameDefaultLoginPassword(getString(R.string.pref_name_login_password));
        stateSingleton.SetPrefNameKillServer(getString(R.string.pref_name_kill_server_activity_destroy));
        stateSingleton.SetPrefNameImportExportDir(getString(R.string.pref_name_import_export_dropbox_sync_dir));
        stateSingleton.SetPrefDefaultValueImportExportDir(getString(R.string.pref_import_export_dropbox_sync_dir_default_for_first_use));

        stateSingleton.StartupRunOnce();

        stateSingleton.StartProcess();

        //TODO: spin a message until python is up and running
        //TODO: how to detect woolnote is up?

        WebView myWebView = (WebView) findViewById(R.id.webview);

        WebSettings webSettings = myWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        //TODO: somehow enable the top loading indicator progress bar
        myWebView.setWebViewClient(new MainWebViewClient());

        myWebView.loadUrl("http://" + getString(R.string.main_url_without_protocol_without_passwd) + stateSingleton.GetLoginPassword());

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        StateSingleton stateSingleton = StateSingleton.getInstance();
        WebView myWebView = (WebView) findViewById(R.id.webview);

        Log.d("WOOLNOTE", "menu item clicked");
        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            Log.d("WOOLNOTE", "settings");
            Intent myIntent = new Intent(getApplicationContext(), SettingsActivity.class);
            this.startActivity(myIntent);
            return true;
        } else if (id == R.id.action_back) {
            myWebView.goBack();
            return true;
        } else if (id == R.id.action_forward) {
            myWebView.goForward();
            return true;
        } else if (id == R.id.action_refresh) {
            myWebView.loadUrl("http://" + getString(R.string.main_url_without_protocol_without_passwd) + stateSingleton.GetLoginPassword());
            return true;
        } else if (id == R.id.action_restart_server) {
            //TODO use asynchronous tasks
            stateSingleton.StopProcess();
            stateSingleton.StartProcess();
            myWebView.loadUrl("http://" + getString(R.string.main_url_without_protocol_without_passwd) + stateSingleton.GetLoginPassword());
            return true;
        } else if (id == R.id.action_quit) {
            //stop the python server
            stateSingleton.StopProcess();

            // https://stackoverflow.com/questions/17719634/how-to-exit-an-android-app-using-code
            moveTaskToBack(true);
            android.os.Process.killProcess(android.os.Process.myPid());
            System.exit(0);
            return true;
        } else if (id == R.id.action_gen_cert) {
            //stop the python server
            stateSingleton.StopProcess();
            stateSingleton.GenerateHttpsCert();
            stateSingleton.StartProcess();

            myWebView.loadUrl("http://" + getString(R.string.main_url_without_protocol_without_passwd) + stateSingleton.GetLoginPassword());
            return true;
        } else if (id == R.id.action_license) {
            //TODO: do it in a better way?
            //TODO: put a license header to all src files
            myWebView.loadUrl("file://" + stateSingleton.GetFilesDirPath() + "/assets/license.html");
            return true;
        } else if (id == R.id.action_readme) {
            //TODO: do it in a better way?
            //TODO: mention how to validate cert
            //TODO: mention how to set up import/export dir, including how to use dropbox for that
            myWebView.loadUrl("file://" + stateSingleton.GetFilesDirPath() + "/assets/README.html");
            return true;
        } else if (id == R.id.action_display_ip_address) {
            AlertDialog.Builder alert = new AlertDialog.Builder(this);
            alert.setTitle("IP Address");
            alert.setMessage("You can use the following addresses to connect to Woolnote over the local network:\n\n" +
                    "https://IPADDRESS:8089/woolnote?woolauth=LOGINPASSWORD\n\n" +
                    "https://IPADDRESS:8089/woolnote?otp=ONETIMEPASSWORD\n\n" +
                    "These IP addresses are currently used by the device:\n\n" +
                    TextUtils.join("\n", Util.GetIpAddreses()) + "\n\n" +
                    "Remember to check the SHA256 of the https certificate against the value displayed on the main page of Woolnote on this device to check that the connection has not been tampered with. A different value on the device and in the connecting computer's web browser https certificate properties window would signify an attack. Read README for more info."
            );
            alert.setPositiveButton("OK", null);
            alert.show();
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    public void onBackPressed() {
        moveTaskToBack(true);
    }

    @Override
    protected void onDestroy() {
        StateSingleton stateSingleton = StateSingleton.getInstance();
        if (stateSingleton.GetPrefKillServer()) {
            stateSingleton.StopProcess();
            super.onDestroy();
        }
    }

}
