import os
import okraparser
# parser_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

image_name = 'receipts3.jpg'
# f = open(os.path.join(parser_location, image_name))

okraparser.basic_scan(image_name)
