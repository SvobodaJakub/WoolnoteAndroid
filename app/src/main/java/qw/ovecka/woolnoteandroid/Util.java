package qw.ovecka.woolnoteandroid;


import android.util.Log;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

/**
 * Created by Jakub Svoboda on 22.1.17.
 */

final class Util {
    protected static String SmallFileIntoString(File file) throws IOException, IndexOutOfBoundsException {

        FileInputStream fileInputStream = new FileInputStream(file);
        long fileLen = file.length();
        if (fileLen - 2 > Integer.MAX_VALUE) {
            throw new IndexOutOfBoundsException("The provided file is too large.");
        }
        byte[] data = new byte[(int) fileLen];
        fileInputStream.read(data);
        fileInputStream.close();
        String result = new String(data, "UTF-8");
        return result;
    }

    // removes potentially unsafe characters
    // the result has to be used inside "" or '' in order to be safe
    // if you need to properly escape, you need a different function than this one
    protected static String SimpleSanitizeShellString(String tainted) {
        return tainted.replaceAll("'", "_").replaceAll("\"", "_").replaceAll("&", "_").replaceAll("$", "_").replaceAll("!", "_");
    }

    protected static String GenerateSecureRandomString() {
        SecureRandom prng = new SecureRandom();
        byte[] randomBytes = new byte[8];
        prng.nextBytes(randomBytes);
        byte[] hash;
        try {
            MessageDigest md5 = null;
            md5 = MessageDigest.getInstance("MD5");
            md5.update(randomBytes);
            hash = md5.digest();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            // TODO: find out whether the BigInteger way is actually the best way and if it is, refactor the code to use only that branch
            BigInteger seedBigInt = new BigInteger(randomBytes);
            long seed = seedBigInt.longValue();
            Random rng2 = new Random(seed);
            hash = new byte[16];
            rng2.nextBytes(hash); // not really a hash but it doesn't matter here
        }

        StringBuffer stringBuffer = new StringBuffer();
        for (int i = 0; i < hash.length; i++) {
            stringBuffer.append(Integer.toHexString(0xFF & hash[i]));
        }

        String hashString = stringBuffer.toString();
        return hashString;
    }

    protected static ArrayList<String> GetIpAddreses() {
        // inspired by http://stackoverflow.com/questions/20103428/java-get-ip-address
        ArrayList<String> ipAddresses = new ArrayList<String>();
        try {
            for (NetworkInterface networkInterface : Collections.list(NetworkInterface.getNetworkInterfaces())) {
                for (InetAddress inetAddress : Collections.list(networkInterface.getInetAddresses())) {
                    if ((!inetAddress.isLoopbackAddress()) && (!inetAddress.isLinkLocalAddress())) {
                        ipAddresses.add(inetAddress.getHostAddress().toString());
                        Log.d("WOOLNOTE", inetAddress.getHostAddress().toString());
                    }
                }
            }
        } catch (SocketException ex) {
            Log.e("WOOLNOTE", ex.toString());
        }
        return ipAddresses;
    }
}
