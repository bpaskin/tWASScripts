# Performance Testing Toolkit with TLSv1.2

The Performance Testing Toolkit was written in Java 5 and compiled in 32 bit and has been largely forgotten.  However, with the new security standards, it is important to have PTT connect with them in place.

Here are the steps for Windows, and Linux should be similar.

1. Download and install [PTT](https://www.ibm.com/developerworks/library/mw-1709-performtun/performtuning.html)

1. Download the latest [32 bit Java 1.7.1 SDK for Liberty for Windows](http://www-01.ibm.com/support/docview.wss?uid=swg24042440)  (Windows 32-bit, x86)

1. Extract the files to a directory.  

1. Go into the `native` directory and extract the `com.ibm.JDK71.32bit.jdk.windows.x8632_7.1...` to another directory.  That is the SDK.

1. In the root of the PTT tool, update the PerfTuningToolkit.ini
  add this in the beginnging, with the correct path to the Java binary directory
  
    `-vm`
  
    `C:\path\to\bin\javaw.exe`
  
    and add these to the bottom of the file:
  
    `-Dhttps.protocols=TLSv1.2`
  
    `-Ddrools.dialect.java.compiler.lnglevel=1.6`

1. Launch PTT, which creates new directories upon first launch

1. Edit the `ssl.client.props.ibm` file under `c:\path\to\PTT\configuration\org.eclipse.osgi\bundles\5\1\.cp\etc`
  change the line:
  
    `com.ibm.ssl.protocol=SSL_TLS`
    to
    `com.ibm.ssl.protocol=TLSv1.2`

1. Restart PTT and make connections as normal
