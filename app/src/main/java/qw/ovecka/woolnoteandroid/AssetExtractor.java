package qw.ovecka.woolnoteandroid;

import android.content.res.AssetManager;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

/**
 * The AssetExtractor class contains three methods created by https://stackoverflow.com/users/2256270/matreshkin.
 * license - cc by-sa 3.0
 * source - http://stackoverflow.com/a/16984117
 * retrieved on 2017-01-29 15:07
 */

final class AssetExtractor {

    // license - cc by-sa 3.0
    // source - http://stackoverflow.com/a/16984117
    protected static boolean copyAssetFolder(AssetManager assetManager,
                                             String fromAssetPath, String toPath) {
        try {
            String[] files = assetManager.list(fromAssetPath);
            new File(toPath).mkdirs();
            boolean res = true;
            for (String file : files)
                if (file.contains("."))
                    res &= copyAsset(assetManager,
                            fromAssetPath + "/" + file,
                            toPath + "/" + file);
                else
                    res &= copyAssetFolder(assetManager,
                            fromAssetPath + "/" + file,
                            toPath + "/" + file);
            return res;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    // license - cc by-sa 3.0
    // source - http://stackoverflow.com/a/16984117
    private static boolean copyAsset(AssetManager assetManager,
                                     String fromAssetPath, String toPath) {
        InputStream in = null;
        OutputStream out = null;
        try {
            in = assetManager.open(fromAssetPath);
            new File(toPath).createNewFile();
            out = new FileOutputStream(toPath);
            copyFile(in, out);
            in.close();
            in = null;
            out.flush();
            out.close();
            out = null;
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    // license - cc by-sa 3.0
    // source - http://stackoverflow.com/a/16984117
    private static void copyFile(InputStream in, OutputStream out) throws IOException {
        byte[] buffer = new byte[1024];
        int read;
        while ((read = in.read(buffer)) != -1) {
            out.write(buffer, 0, read);
        }
    }
}

