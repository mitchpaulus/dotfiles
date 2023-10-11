# FTP

Firefox and Chrome both killed FTP. [Source](https://www.ghacks.net/2021/04/16/firefox-90-wont-handle-ftp-sites-anymore/)

Can still get to FTP data using the file explorer. Drop the URL in the
address bar. Example:

<ftp://ftp.ncdc.noaa.gov/pub/data/noaa/>

<ftp://ftp.ncdc.noaa.gov/pub/data/noaa/2021/722590-03927-2021.gz>

```
wget ftp://asdfasdf/
wget -r ftp://asdfasdf/ # recursive for directories
```
