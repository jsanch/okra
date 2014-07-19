#!/bin/sh
tesseract $1 $1'1'
# ./textcleaner -g $1 'e_'$1
# tesseract 'e_'$1 $1'2'

# rm 'e_'$1