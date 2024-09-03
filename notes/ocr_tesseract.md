# OCR w/ Tesseract

Installation on Ubuntu

```sh
sudo apt install tesseract-ocr libtesseract-dev tesseract-ocr-eng
```

```sh
tesseract -l eng input_file.png output_base
```

Set resolution with --dpi

Example of converting Andover graphics to correct name:
See Wichita Falls Lamar and Duncanville FAR

```fish
(convert $p -crop 332x20+83+5 png:- |  tesseract --user-words words.txt --psm 7  --dpi 72  -l eng - stdout | head -n 1 | awk 'BEGIN { FS=" \\\\" } { print $NF } ' | sed 's/[]*)]//g'  )
```

For examples of EBO, see Taylor EBO or Allen EBO:
