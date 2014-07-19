#!/bin/sh
# tesseract $1 $1'1' letters
/root/okra/scan/textcleaner -g $1 '/root/okra/images/tmp.jpg'
# tesseract 'e_'$1 $1'2'

# rm 'tmp.jpg'