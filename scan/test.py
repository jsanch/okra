import os
import shutil
import re
import tre
import json
# import Levenshtein



parser_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# f = open(os.path.join(parser_location, 'bundled-resource.jpg'));
# print parser_location
images_location = os.path.join(os.path.dirname(parser_location), 'images/')
# print images_location

config_file = open(os.path.join(parser_location, 'parser-config.json'), 'r')
config = json.load(config_file)


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

	raw_item_data = []

	with open(full_image_path + '1.txt','r') as file:
		for line in file.read().splitlines():
			# print line
			tre_match = tre_matcher.search(line, tre_fuzzyness)
			if tre_match:
				# print tre_match
				# print tre_match.group(0)
				# print line
				tmp_description = re.sub(r'[\s:]*' + tre_match.group(0), '', line).lower()
				tmp_value = tre_match.group(0).strip()
				raw_item_data.append({'description' : tmp_description, 'value' : tmp_value})


	print raw_item_data

	tre_fuzzyness = tre.Fuzzyness(delcost = 1, inscost = 2, subcost = 1, maxcost = 4)


	for item in raw_item_data:
		item_description = item['description']
		matches_to_compare = []
		for parser_key in config['mid_parsers']:
			tre_matcher = tre.compile(config['mid_parsers'][parser_key]['ere'], tre.EXTENDED)
			tre_match = tre_matcher.search(item_description, tre_fuzzyness)
			if tre_match:
				matches_to_compare.append(tre_match)
		

				# print "xxxxxxxxxxxxxxxxxxxx"
				# item['used'] = True
				# raw_item_data.remove(item)
				# print item_description
				# print config['mid_parsers'][parser_key]['string'] + ' : ' + item['value']
				# print config['mid_parsers'][parser_key]['string']

	# tre_matcher = tre.compile(config['mid_parsers']['test']['ere'], tre.EXTENDED)
	# tre_match = tre_matcher.search('sub totat', tre_fuzzyness)
	# print tre_match.cost
	# print tre_match



	# print raw_item_data
		# match = re.search(ere_end_of_line_price, line)
		# if match != None:
			# raw_item_data.append({re.sub(r'(\s)$', '', line[:match.start()]) : match.group(0)})

image_name = 'receipts3.jpg'
f = open(os.path.join(parser_location, image_name))

basic_scan(f, 'asdfadsf.jpg')