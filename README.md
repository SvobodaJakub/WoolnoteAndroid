# WoolnoteAndroid
WoolnoteAndroid - a java wrapper and Python runtime and the Woolnote python note and task management app.

Woolnote - a note and task management app written in Python - https://github.com/SvobodaJakub/woolnote.

Python and OpenSSL built statically for ARM Linux / Android - https://github.com/SvobodaJakub/static_multiarch_build_python_openssl

![screenshot](https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/screenshot_first.png)

## README for woolnote for Android

### Installation
Upon installation, woolnote creates the /sdcard/woolnote directory into which data and backups are saved. If the device doesn't have the /sdcard directory, woolnote cannot run.

Upon installation, go into Settings, Import & export and set a directory into which a "woolnote.zip" file will be saved on export and read from on import. You can set this mechanism to easily back up your notes to Dropbox or a similar storage and to sync notes between multiple devices. If you don't want to deal with that now and woolnote refuses to run because the directory doesn't exist (which will happen only if you actually go to settings and leave it unconfigured), just select the /sdcard/woolnote directory and woolnote.zip imports&exports will happen there.

### Settings
Login password - A static password you can save into the bookmarks on your computer, provided you trust such bookmark storage.

Import&export - You can specify the directory used to read/write the woolnote.zip file used by the "Import" and "Export" functions of woolnote. The directory is set to /sdcard/woolnote upon installation but is changed to an example Dropbox path once the settings screen is opened. If you do not wish to use the functionality, pick the /sdcard/woolnote path. However, I strongly recommend setting it up with Dropbox (or some other service which listens to file changes and uploads them automatically) because it allows you to back up your data on demand. I have a habit of exporting the data every day, knowing that if I lose my phone, I won't lose my data.

Ordinarily, you probably want to use import & export only for backups. Woolnote starts a server reachable on the local network, so you can access the data from your computer on the same network and have no hassle with synchronization.

The Android Dropbox app listens to file changes for files marked as "Available Offline" and automatically uploads the changes, which means exports from Woolnote can be automatically uploaded to Dropbox. If the file changes on Dropbox, you have to manually open the Dropbox app go to menu, Offline, and let it sync to download the changes so that they can be imported by Woolnote. If you are a software developer and want to help me with having a better storage integration, you are welcome.

How to set up Dropbox for automatic synchronization
1. Export the woolnote.zip file from woolnote and manually import it into Dropbox using the Dropbox app to the place inside Dropbox where you wish to store it.
2. In the Dropbox app, long-click the woolnote.zip file and enable Offline. This downloads the file somewhere to /storage/emulated/0/Android/data/com.dropbox.android/files/u20358332(use your Dropbox account number)/scratch/. In woolnote, select the directory where woolnote.zip is stored by Dropbox.
3. Export from woolnote - this one is easy. Make sure the Dropbox app is running in the background. In Woolnote, select Export and export the data. Dropbox detects that the file changes and uploads it, displaying a notification.
4. Import to woolnote - this one is more complicated. Unfortunately, unlike on desktop, Dropbox doesn't automatically sync files from cloud to the device, you have to trigger the sync manually. Open the Dropbox app, display the offline files from the sidebar, let it sync. Then open woolnote and use the Import type which you want.


### Backups
Woolnote creates local backup copies of the task database on these occasions:
* Starting up the woolnote server.
* Export
* Import

Sometimes, you might need to recover old data. You might find them in the backups directory (/sdcard/woolnote/backups). The primary task database is in /sdcard/woolnote/task_store.dat. To recover data, first make a backup of task_store.dat so that you can revert in case you do something wrong. Quit woolnote. Manually fix the database file (make sure not to break the file format structure). You might find the tools grep, meld, windiff useful.

The backups directory is growing, you might want to clean it from time to time. The most comfortable way is to either delete the whole backups directory and create it again, or to selectively delete files from desktop (through cable or SSH).


### Connecting to the woolnote server
Woolnote for Android is in fact a standard Android Java application for the user interface (menu, settings, launcher icon), containing a WebView for displaying the interface of woolnote, and containing the Python interpreter and the woolnote note&task management app written in Python, which is a basic web application, displaying its user interface over HTTP or HTTPS.
Every time Woolnote for Android runs, the woolnote server runs as well. You can connect to the port 8088 over HTTP or to the port 8089 over HTTPS. You can authenticate using a login password or using a OTP (one-time password).

#### HTTP
Don't use HTTP on networks you don't trust. Anyone with sufficient access to the network can see all your transmitted data including the login password or authentication cookies and can log into woolnote as you and access or modify anything in there.

#### HTTPS
Because Woolnote cannot use a valid SSL/TLS certificate, it has to auto-generate a self-signed untrusted certificate. To check the security of the connection, you generally have to do the following on untrusted networks:

1. Connect to Woolnote from your browser but don't enter valid login credentials. (woolnote menu, Display IP address tells you how)
2. Dismiss the security alert in the browser.
3. View the HTTPS certificate in the browser and view the SHA256 fingerprint.
4. On the mobile phone, go to the Woolnote main page and see the SHA256 fingerprint on top.
5. If the fingerprints are different, someone is attacking you. If the fingerprints are the same, you can now use valid login credentials to log in from the browser.
6. To log out from the browser (e.g. in case you don't trust it anymore because someone else has access to the computer), then use the menu items Quit or Restart server in Woolnote on your mobile phone.

If you are a software developer and want to make the secure network communication better and more user-friendly, you are welcome.

#### Login password
A static password you can save into the bookmarks on your computer, provided you trust such bookmark storage.

#### OTP
One-time password. Once an OTP is generated, it is valid for 5 unsuccessful tries and then it is invalidated. It is also invalidated after a successful use so that if you enter it while someone sees you, they cannot reuse it unless they can type it and hit enter faster than you.

## README for woolnote (both the pure Python version and the Android version)

### Easy to type lists
Lists are text lines beginning with "-" or "+" or "\*"or "\*\*" or "\*\*\*" followed by a space and text. The following lines automatically gain the same prefix on save (until an empty line or until a different list is defined). This allows you to easily type a long list on the phone keyboard because you don't have to search for the special characters on each line - just on the first line. If you don't like the feature, set the note's format to plaintext - this is useful when you insert arbitrary copy&pasted things like emails or code.
More information about formatting is directly inside woolnote in the "_woolnote_config" note.


# FAQ 
A.k.a. questions nobody asks that I pulled out of my colored hat :)

* Is woolnote better than other note-taking apps?
    * Objectively, no.
* What are the strengths of woolnote?
    * OpenSource, 
    * easily hackable in Python, 
    * allows easy switching between using PC and phone without synchronization, 
    * simple data format that doesn't lock you in (and you can use woolnote's source code to hack together export to another format should you decide to move to sth else), 
    * you are in control of the data,
    * backup archive with previous note database versions, 
    * simple markup language allowing the creation of ad-hoc mixed checklists and notes with simple formatting, 
    * use of a markup language to insert lists and textboxes into an ordinary plaintext text area is much faster and smoother than the feature-rich text areas that some other note-taking apps use,
    * import&export including a rudimentary ability to handle conflicts,
    * no user tracking (well, if you don't use cloud storage for import&export),
    * individual notes can be shared over the local network as read-only to other people who don't have login,
    * access token & password checking is implemented in a secure way preventing timing attacks to reveal the password over network,
    * HTTPS support.
* Should I use woolnote?
    * Depends on your needs and expertise with Python and IT in general in case something breaks.
    * If you are happy with Google Keep, Evernote, Simplepad, or any other existing product, please don't use woolnote. Woolnote is not a product, has no development lifecycle, has no support, and is not tailored to keep most users happy.
    * If you tried all of them and you are still in a search for something else, you should check out woolnote and if it fits your style, use it as a base for your own app.
* Should I fork?
    * Yes, because woolnote is not aimed for the general user, it has been created to serve my peculiar needs. Adding too much additional functionality wouldn't fit woolnote's non-extensible "architecture". It's better to create a new app using woolnote as a base.
* How do I request new functionality?
    * You can certainly try to request it through github or through a merge request. I might implement/merge it if it fits my needs, or I might advise you to fork and create your own version. If your idea is especially intriguing, I might even maintain a fork for a time, just to experiment with the idea. (I don't usually have much time for woolnote, so don't hold your breath.)
* How can we collaborate?
    * If you happen to have the exact same needs for note and task management, collaboration on a single project with a unified vision might work.
    * If you create a fork, I'd be happy to collaborate on fixing parts that are shared between our forks, to a sensible extent. I believe in friendly forking, leading to healthy competition, growth of fresh ideas, and experiments.
* Will woolnote magically help me with note and task management?
    * No.
    * You need a good system. Start with reading GTD and ZTD for much needed inspiration. Think about yourself and your life. Create a system that suits you. Create a system where you do things not because someone said so but because you have personal reasons why you should do it so.
    * A good system is a vehicle for your thoughts
    * Woolnote is a vehicle for the system. A part of it, actually. I don't want emails in woolnote. I can't have physical stuff in woolnote.
* Why is there such a weak support for reminders?
    * I don't use that functionality that often. A central part of my task list is a week-by-week timeline-like task list where most of the short-term stuff ends up. Most of the long-term reminders end up on my calendar and in my tickler note. The reminder/deadline functionality is therefore for the oddball notes that are perhaps temporary projects (like home renovation) which can't be put easily on one line into a tickler or into the calendar but are a topic of notes and tasks in one woolnote note and then I remember I need this note to pop up on me on a certain date. You can see a few examples of that in the demo file tasks.dat.
* Why does it look so awful?
    * Some people feel uneasy looking at unaligned graphical elements and whatnot. If you are one of them, I know the interface looks insane to you. I don't care about such things and I don't have the time nor the skills necessary to fix it. If you want to make the UI better, you are welcome.


# Screenshots

<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777016.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777146.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777161.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777172.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777184.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777255.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777381.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777391.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777395.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777400.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777585.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777627.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777693.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777812.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492777889.png" width="300">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492778230.png">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492778277.png">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492778308.png">
<img src="https://github.com/SvobodaJakub/WoolnoteAndroid/raw/master/screenshots/Screenshot_1492778368.png">
