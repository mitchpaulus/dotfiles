My Epson printer on Linux (Manjaro) seemed to work with the following URI:

```
dnssd://EPSON%20ET-3830%20Series._ipp._tcp.local/?uuid=cfe92100-67c4-11d4-a45f-dccd2f3d6862
```

No idea how to figure this URI out from first principles.


From ChatGPT

```
The dnssd URI scheme stands for DNS Service Discovery,
and it's a way of locating and using services on a local network using multicast DNS (mDNS) and DNS Service Discovery (DNS-SD).
```

What's in a PPD? This is the top lines from my EPSON special ppd file.
Can figure out what PPD file a printer is tied to by searching for the 'NickName'
that matches the "Make and Model" in the CUPS web interface.

Can get to the CUPS web interface by going to <http://localhost:631/printers/>

```ppd
*PPD-Adobe: "4.3"
*% Adobe Systems PostScript(R) Printer Description File
*% Copyright 1987-1996 Adobe Systems Incorporated.
*% All Rights Reserved.
*% Copyright (c) SEIKO EPSON Corporation. 2009
*FormatVersion: "4.3"
*FileVersion: "1.1"
*LanguageVersion: English
*LanguageEncoding: ISOLatin1
*PCFileName: "EPET-3830 Series.PPD"
*Product: "(EPSON ET-3830 Series)"
*PSVersion: "(3010.000) 550"
*ModelName: "EPSON ET-3830 Series"
*ShortNickName: "EPSON ET-3830 Series"
*NickName: "EPSON ET-3830 Series , Epson Inkjet Printer Driver 2 (ESC/P-R) for Linux"
*Manufacturer: "Epson"
*LanguageLevel: "3"
*ColorDevice: True
*DefaultColorSpace: RGB
*FileSystem: True
*Throughput: "1"
*TTRasterizer: Type42
*cupsLanguages: "nl fr de it ja pt pt_PT es ko ru zh_TW zh_CN"
*cupsVersion: 1.2
*cupsManualCopies: True
*cupsModelNumber: 1
*cupsFilter: "application/vnd.cups-raster 0 epson-escpr-wrapper2"
*LandscapeOrientation: Plus90
*VariablePaperSize: False
*DefaultOutputOrder: Reverse
*ESCPRCompression: 3, 16
*1284DeviceID: "MFG:Epson;MDL:ET-3830 Series;DES:EPSON ET-3830 Series;"

```
