import os
import shutil
import re
import tre
# import sys
import codecs
import json
# import Levenshtein

# sys.setdefaultencoding('utf-8')

parser_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# f = open(os.path.join(parser_location, 'bundled-resource.jpg'));
# print parser_location
images_location = os.path.join(os.path.dirname(parser_location), 'images/')
# print images_location

config_file = open(os.path.join(parser_location, 'parser-config.json'), 'r')
config = json.load(config_file, 'ascii')

print config

ere_end_of_line_price = r'\$?[0-9]+[\.,][0-9]{2}$'
# ere_balance_due = r'(balance)( due)?)'
# ere_total = r'(total)( due)?'
# ere_subtotal = r'(sub)[ -]?(total)'
# ere_tax = r'((meal(s)?)|(sales))?

string_total = 'total'
string_subtotal = 'subtotal'
# string

def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"

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

	raw_tab_data = []
	tab_items = []
	tab_meta = []


	with open(full_image_path + '1.txt','r') as file:
		for line in file.read().splitlines():
			# print line
			# line = line.encode('punycode')
			print line
			tre_match = tre_matcher.search(line, tre_fuzzyness)
			if tre_match:
				# print tre_match
				# print tre_match.group(0)
				# print line
				tmp_description = re.sub(r'[\s:]*' + tre_match.group(0), '', line).lower()
				tmp_value = tre_match.group(0).strip()
				# tmp_value = 'asdfa'
				raw_tab_data.append({'description' : tmp_description, 'value' : tmp_value})


	# print raw_tab_data

	tre_fuzzyness = tre.Fuzzyness(maxerr = 3)
	# print tre_fuzzyness


	for item in raw_tab_data:
		item_description = item['description']
		matches_to_compare = []
		for parser_key in config['mid_parsers']:
			tre_matcher = tre.compile(config['mid_parsers'][parser_key]['ere'], tre.EXTENDED)
			tre_match = tre_matcher.search(item_description, tre_fuzzyness)
			# print "xxxxxxxxxxxxxxxxxxxx"
			# print 'comparing: ' + item_description + ', ' + config['mid_parsers'][parser_key]['ere']
			if tre_match:
				# print tre_match.groups()

				# print tre_match.cost
				# print tre_match.cost
				# print tre_match.numdel
				# print tre_match.numins
				# print tre_match.numsub
				# print 'match'
				matches_to_compare.append((tre_match, config['mid_parsers'][parser_key]['string']))

		if matches_to_compare:
			# If there were matches
			min = matches_to_compare[0]
			for match in matches_to_compare:
				if match[0].cost < min[0].cost:
					min = match

			print str(min[0].cost) + ' ' + min[1] + ' : ' + item['value']
		else:
			tab_items.append(item)
			# If there were no matches


	print tab_items
		# print "xxxxxxxxxxxxxxxxxxxx"
		# print min[1], whatisthis(min[1])
		# print item_description, whatisthis(item_description)
		# x = str(min[1]) + ' : ' + item_description
		# print min[0].cost
		# print min[0].numdel
		# print min[0].numins
		# print min[0].numsub
		# print unicode(x)
		# print x
		# print config['mid_parsers'][parser_key]['string'] + ' : ' + item['value']

				# print "xxxxxxxxxxxxxxxxxxxx"
				# item['used'] = True
				# raw_tab_data.remove(item)
				# print item_description
				# print config['mid_parsers'][parser_key]['string'] + ' : ' + item['value']
				# print config['mid_parsers'][parser_key]['string']

	# tre_matcher = tre.compile(config['mid_parsers']['test']['ere'], tre.EXTENDED)
	# tre_match = tre_matcher.search('sub totat', tre_fuzzyness)
	# print tre_match.cost
	# print tre_match



	# print raw_tab_data
		# match = re.search(ere_end_of_line_price, line)
		# if match != None:
			# raw_tab_data.append({re.sub(r'(\s)$', '', line[:match.start()]) : match.group(0)})

image_name = 'receipts3.jpg'
f = open(os.path.join(parser_location, image_name))

basic_scan(f, 'asdfadsf.jpg')