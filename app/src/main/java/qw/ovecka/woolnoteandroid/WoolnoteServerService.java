package qw.ovecka.woolnoteandroid;

import android.app.Notification;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.widget.Toast;

public class WoolnoteServerService extends Service {
    public WoolnoteServerService() {
    }

    @Override
    public IBinder onBind(Intent intent) {
        // We don't provide binding, so return null
        return null;
    }

    private StateSingleton stateSingleton = StateSingleton.getInstance();

    /*
    Run like this:
                Intent startIntent = new Intent(MainActivity.this, WoolnoteServerService.class);
                startIntent.setAction(Constants.ActionStartWoolnoteServerServiceForeground);
                startService(startIntent);
     */
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if (intent.getAction().equals(Constants.ActionStartWoolnoteServerServiceForeground)) {
            if (stateSingleton.GetInitialized()) {
                if (!stateSingleton.IsProbablyRunning()) {
                    // show only if it is probable that the service is not running already
                    Toast.makeText(getApplicationContext(), "Starting server service - " + getString(R.string.app_name), Toast.LENGTH_SHORT).show();
                }
                stateSingleton.StartProcess();

                // TODO have a nice icon, maybe some actions?
                Notification notification = new Notification.Builder(getApplicationContext())
                        .setContentTitle(getString(R.string.app_name))
                        //.setContentText(contentText)
                        .setSmallIcon(R.drawable.ic_notification)
                        .setWhen(System.currentTimeMillis())
                        //.setContentIntent(contentIntent)
                        .build();
                startForeground(1, notification);

            } else {
                Toast.makeText(getApplicationContext(), "Uninitialized service startup attempt, shutting down - " + getString(R.string.app_name), Toast.LENGTH_SHORT).show();
                //cannot run
                stopSelf();
            }
        } else {
            Toast.makeText(getApplicationContext(), "Invalid service startup attempt, ignoring - " + getString(R.string.app_name), Toast.LENGTH_SHORT).show();
            //ignored
        }
        return START_NOT_STICKY;
    }

    @Override
    public void onDestroy() {
        Toast.makeText(getApplicationContext(), "Stopping server service - " + getString(R.string.app_name), Toast.LENGTH_SHORT).show();
        stateSingleton.StopProcess();
        stopForeground(true);
    }
}
