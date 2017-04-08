package qw.ovecka.woolnoteandroid;

import android.content.Intent;
import android.net.Uri;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;


/**
 * From https://developer.android.com/guide/webapps/webview.html and slightly tweaked
 */

public class MainWebViewClient extends WebViewClient {
    @Override
    public boolean shouldOverrideUrlLoading(WebView view, String url) {
        if (Uri.parse(url).getHost().equals(view.getContext().getString(R.string.main_url_only_host_without_protocol))) {
            // This is my web site, so do not override; let my WebView load the page
            return false;
        }
        // Otherwise, the link is not for a page on my site, so launch another Activity that handles URLs
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
        view.getContext().startActivity(intent);
        return true;
    }

    @Override
    public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
        if (view != null) {

            String htmlData = "<html>" +
                    "<head>" +
                    "<meta charset=utf-8>\n" +
                    "<meta name=\"viewport\" content=\"width=device-width, height=device-height, initial-scale=1.0, user-scalable=no, user-scalable=0\"/>" +
                    "<meta http-equiv=\"refresh\" content=\"1;url=" + failingUrl + "\" />" +
                    "</head>" +
                    "<body>" +
                    "<div><p>The page " + failingUrl + " didn't load, retrying...</p><br>" +
                    "<p>Error description: " + description + "\n</p><br>" +
                    "<p>This might be caused by the Woolnote server taking a few seconds to start.</p>" +
                    "</div>" +
                    "</body>";

            view.loadUrl("about:blank");
            view.loadDataWithBaseURL(null, htmlData, "text/html", "UTF-8", null);
            view.invalidate();

        }
        super.onReceivedError(view, errorCode, description, failingUrl);
    }
}
