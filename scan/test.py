import os
import shutil
import re
import tre
# import Levenshtein



parser_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# f = open(os.path.join(parser_location, 'bundled-resource.jpg'));
# print parser_location
images_location = os.path.join(os.path.dirname(parser_location), 'images/')
# print images_location

ere_end_of_line_price = r'\$?[0-9]+[\.,][0-9]{2}$'
ere_balance_due = r'(balance)( due)?)'
ere_total = r'(total)( due)?'
ere_subtotal = r'(sub)[ -]?(total)'
# ere_tax = r'((meal(s)?)|(sales))?

string_total = 'total'
string_subtotal = 'subtotal'
# string


# ere_end_of_line_price = r'[0-9]{2}'

# ere_end_of_line_price = r'Thanks'
image_folder = 'images'

def basic_scan(image, file_name):
	full_image_path = images_location + image_name
	# New file
	# dest = open(os.path.join(parser_location, file_name), 'w')
	# shutil.copy(image.buffer(), dest)

	tre_fuzzyness = tre.Fuzzyness(delcost = 3, inscost = 1, subcost = 2, maxcost = 2)
	tre_matcher = tre.compile(ere_end_of_line_price, tre.EXTENDED)
	
	print os.path.join(parser_location, 'ocr.sh') + ' ' + full_image_path
	os.system(os.path.join(parser_location, 'ocr.sh') + ' ' + full_image_path)
	# os.path.join(parser_location, '/ocr.sh')

	raw_data = []

	with open(full_image_path + '1.txt','r') as file:
		for line in file.read().splitlines():
			# print line
			tre_match = tre_matcher.search(line, tre_fuzzyness)
			if tre_match:
				print tre_match
				print tre_match.group(0)
				raw_data.append({re.sub(r'[\s:]' + tre_match.group(0), '', line).lower() : tre_match.group(0).strip()})


	print raw_data
		# match = re.search(ere_end_of_line_price, line)
		# if match != None:
			# raw_data.append({re.sub(r'(\s)$', '', line[:match.start()]) : match.group(0)})

image_name = 'receipts3.jpg'
f = open(os.path.join(parser_location, image_name))

basic_scan(f, 'asdfadsf.jpg')