package qw.ovecka.woolnoteandroid;

/**
 * Public domain code from https://rogerkeays.com/simple-android-file-chooser retrieved 2017-01-29 14:33 CET.
 * Original author: Roger Keays, published 3 June 2015
 * "Here is the FileChooser class which you can cut and paste into your project. Public domain code so do what you want with it. Peace."
 * Modified to be a directory picker rather than a file picker.
 */

import android.app.Activity;
import android.app.Dialog;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager.LayoutParams;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import java.io.File;
import java.io.FileFilter;
import java.util.Arrays;

class DirChooser {
    private static final String PARENT_DIR = "..";
    private static final String SELECT_THIS_DIR = "[SELECT THIS DIRECTORY]";

    private final Activity activity;
    private ListView list;
    private Dialog dialog;
    private File currentPath;


    // file selection event handling
    public interface FileSelectedListener {
        void fileSelected(File file);
    }

    public DirChooser setFileListener(FileSelectedListener fileListener) {
        this.fileListener = fileListener;
        return this;
    }

    private FileSelectedListener fileListener;

    public DirChooser(Activity activity) {
        this.activity = activity;
        dialog = new Dialog(activity);
        list = new ListView(activity);
        list.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int which, long id) {
                String fileChosen = (String) list.getItemAtPosition(which);
                Log.d("WOOLNOTE", fileChosen);
                File chosenFile = getChosenFile(fileChosen);
                Log.d("WOOLNOTE", chosenFile.getAbsolutePath());
                if (fileChosen.equals(SELECT_THIS_DIR)) {
                    if (fileListener != null) {
                        fileListener.fileSelected(chosenFile);
                    }
                    dialog.dismiss();
                } else if (chosenFile.isDirectory()) {
                    refresh(chosenFile);
                }
            }
        });
        dialog.setContentView(list);
        dialog.getWindow().setLayout(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT);
        refresh(Environment.getExternalStorageDirectory());
    }

    public void showDialog() {
        dialog.show();
    }


    /**
     * Sort, filter and display the files for the given path.
     */
    private void refresh(File path) {
        this.currentPath = path;
        if (path.exists()) {
            File[] dirs = path.listFiles(new FileFilter() {
                @Override
                public boolean accept(File file) {
                    return (file.isDirectory() && file.canRead());
                }
            });

            // convert to an array
            int i = 0;
            String[] fileList;
            if (path.getParentFile() == null) {
                fileList = new String[dirs.length + 1];
            } else {
                fileList = new String[dirs.length + 1 + 1];
                fileList[i++] = PARENT_DIR;
            }
            fileList[i++] = SELECT_THIS_DIR;
            Arrays.sort(dirs);
            for (File dir : dirs) {
                fileList[i++] = dir.getName();
            }

            // refresh the user interface
            dialog.setTitle(currentPath.getPath());
            list.setAdapter(new ArrayAdapter(activity,
                    android.R.layout.simple_list_item_1, fileList) {
                @Override
                public View getView(int pos, View view, ViewGroup parent) {
                    view = super.getView(pos, view, parent);
                    ((TextView) view).setSingleLine(true);
                    return view;
                }
            });
        }
    }


    /**
     * Convert a relative filename into an actual File object.
     */
    private File getChosenFile(String fileChosen) {
        if (fileChosen.equals(PARENT_DIR)) {
            return currentPath.getParentFile();
        } else if (fileChosen.equals(SELECT_THIS_DIR)) {
            return currentPath;
        } else {
            return new File(currentPath, fileChosen);
        }
    }
}
