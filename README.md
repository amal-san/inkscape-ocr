# inkscape-ocr 🖼️
Inkscape Extension using [tesseract_ocr](https://github.com/tesseract-ocr) to read text from Image



Note: Currently supported only for debian users and Inkscape v1.0+


## Prerequisites
   
   `sudo apt-get install -y libpng-dev libjpeg-dev zlib1g-dev autoconf automake libtool checkinstall tesseract-ocr python3-dev`
 
   `pip3 install pytesseract cairosvg`
 

## Installation

   Copy files `ocr_extension.inx` and `ocr_extension.py` to extensions directory 

   For root users  `/usr/share/inkscape/extension`
      
   For non-root users   `~/.config/inkscape/extensions`
