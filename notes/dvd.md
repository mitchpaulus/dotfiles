Ripping DVDs

- Can mount DVD using command:
    - `sudo mount -t iso9660 /dev/sr1 dvd/`

- Rip using `ffmpeg`
    - `cat *.VOB | ffmpeg -i - -vcodec h264 -acodec aac filename.mp4`
