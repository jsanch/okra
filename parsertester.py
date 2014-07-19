import os
import scan.okraparser
# parser_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

image_name = 'shitty.jpg'
# f = open(os.path.join(parser_location, image_name))

print scan.okraparser.full_scan(image_name)
