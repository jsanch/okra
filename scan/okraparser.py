from decimal import *
import os
import shutil
import re
import tre
import codecs
import json

DEBUG = True

class OkraParseException(Exception):
	pass

parser_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# f = open(os.path.join(parser_location, 'bundled-resource.jpg'));
images_location = os.path.join(os.path.dirname(parser_location), 'images/')

config_file = open(os.path.join(parser_location, 'parser-config.json'), 'r')
config = json.load(config_file, 'ascii')

# print config

ere_end_of_line_price = r'\$?[0-9]+[\.,][0-9]{2}$'

string_total = 'total'
string_subtotal = 'subtotal'
image_folder = 'images'

def debug(x):
	if DEBUG:
		print x

def analyze_tab(tab_param):
	tab = {}
	tab['items'] = {}
	tab['meta'] = {}

	avail_total = config['mid_parsers']['total']['string'] in tab_param['tab_meta']
	avail_balance_due = config['mid_parsers']['balance_due']['string'] in tab_param['tab_meta']
	avail_subtotal = config['mid_parsers']['subtotal']['string'] in tab_param['tab_meta']
	avail_tax = config['mid_parsers']['tax']['string'] in tab_param['tab_meta']

	string_total = config['mid_parsers']['total']['string']
	string_balance_due = config['mid_parsers']['balance_due']['string']
	string_subtotal = config['mid_parsers']['subtotal']['string']
	string_tax = config['mid_parsers']['tax']['string']

	if avail_tax:
		meta_tax = price_fix(tab_param['tab_meta']['tax'])
		debug('meta_tax' + ' ' + str(meta_tax) + ' ' + str(type(meta_tax)))
	if avail_balance_due:
		meta_balance_due = price_fix(tab_param['tab_meta']['balance_due'])
		debug('meta_balance_due' + ' ' + str(meta_balance_due) + ' ' + str(type(meta_balance_due)))
	if avail_subtotal:
		meta_subtotal = price_fix(tab_param['tab_meta']['subtotal'])
		debug('meta_subtotal' + ' ' + str(meta_subtotal) + ' ' + str(type(meta_subtotal)))
	if avail_total:
		meta_total = price_fix(tab_param['tab_meta']['total'])
		debug('meta_total' + ' ' + str(meta_total) + ' ' + str(type(meta_total)))

	item_total = Decimal()
	for item in tab_param['tab_items']:
		tab['items'][item['description']] = price_fix(item['value'])
		item_total += price_fix(item['value'])

	print 'item_total', item_total, type(item_total)

	debug('avail_total' + ': ' + str(avail_total))
	debug('avail_balance_due' + ': ' + str(avail_balance_due))
	debug('avail_tax' + ': ' + str(avail_tax))
	debug('avail_subtotal' + ': ' + str(avail_subtotal))

	if (avail_total and avail_balance_due and avail_tax and avail_subtotal):
		if (meta_total != meta_balance_due):
			raise OkraParseException('1')
		elif (meta_total != meta_subtotal + meta_tax):
			raise OkraParseException('2')
		elif (meta_total !=  item_total):
			raise OkraParseException('3')
		else:
			tab['meta'] = {string_total : meta_total, string_subtotal : meta_subtotal, string_tax : meta_tax}
	elif (avail_total and avail_tax and avail_subtotal):
		if (meta_total != meta_subtotal + meta_tax):
			raise OkraParseException('4')
		elif (meta_subtotal !=  item_total):
			raise OkraParseException('5')
		else:
			tab['meta'] = {string_total : meta_total, string_subtotal : meta_subtotal, string_tax : meta_tax}
	elif (avail_total and avail_subtotal):
		print meta_subtotal
		print item_total
		print meta_subtotal == item_total
		if not (meta_total == item_total or meta_subtotal == item_total):
			raise OkraParseException('6')
		elif (meta_subtotal ==  item_total):
			tab['meta'] = {string_total : meta_total, string_subtotal : meta_subtotal, string_tax : meta_total - meta_subtotal}
		elif (meta_total == item_total):
			tab['meta'] = {string_total : meta_total, string_subtotal : meta_subtotal, string_tax : 0}
		else:
			raise OkraParseException('7')
	else:
		raise OkraParseException('8')

	return tab

def price_fix(x):
	return Decimal(x.strip('$'))

def full_scan(image_name):
	try:
		return basic_scan(image_name)
	except OkraParseException:
		return advanced_scan(image_name)

def advanced_scan(image_name):
	full_image_path = images_location + image_name
	os.system(os.path.join(parser_location, 'ocr2.sh') + ' ' + full_image_path)
	return basic_scan('tmp.jpg')

def basic_scan(image_name):
	full_image_path = images_location + image_name
	# New file
	# dest = open(os.path.join(parser_location), 'w')
	# shutil.copy(image.buffer(), dest)

	tre_fuzzyness = tre.Fuzzyness(delcost = 3, inscost = 1, subcost = 2, maxcost = 2)
	tre_matcher = tre.compile(ere_end_of_line_price, tre.EXTENDED)
	
	# print os.path.join(parser_location, 'ocr.sh') + ' ' + full_image_path
	os.system(os.path.join(parser_location, 'ocr.sh') + ' ' + full_image_path)
	# os.path.join(parser_location, '/ocr.sh')

	raw_tab_data = []
	tab_items = []
	tab_meta = []

	with open(full_image_path + '1.txt','r') as file:
		for line in file.read().splitlines():
			# print line
			# line = line.encode('punycode')
			debug(line)
			tre_match = tre_matcher.search(line, tre_fuzzyness)
			if tre_match:
				tmp_description = re.sub(r'[\s:]*' + re.escape(tre_match.group(0)), '', line).lower()
				tmp_value = tre_match.group(0).strip()
				# tmp_value = 'asdfa'
				raw_tab_data.append({'description' : tmp_description, 'value' : tmp_value})


	tre_fuzzyness = tre.Fuzzyness(maxerr = 3)
	tab_meta = {}

	cut_off_meta = 0

	for raw_item in raw_tab_data:
		raw_item_description = raw_item['description']
		matches_to_compare = []
		for parser_key in config['mid_parsers']:
			tre_matcher = tre.compile(config['mid_parsers'][parser_key]['ere'], tre.EXTENDED)
			tre_match = tre_matcher.search(raw_item_description, tre_fuzzyness)
			debug('xxxxxxxxxxxxxxxxxxxxxxxxxx')
			debug(raw_item_description + ' XXX ' + config['mid_parsers'][parser_key]['ere'])
			if tre_match:
				debug('match')
				matches_to_compare.append((tre_match, config['mid_parsers'][parser_key]['string']))

		if matches_to_compare:
			# If there were matches
			cut_off_meta += 1
			min = matches_to_compare[0]
			for match in matches_to_compare:
				if match[0].cost < min[0].cost:
					min = match
			tab_meta[min[1]] = raw_item['value']
		else:
			if cut_off_meta < 1:
				tab_items.append(raw_item)

	tab = {'tab_items' : tab_items, 'tab_meta' : tab_meta}
	# print tab

	# print analyze_tab(tab)
	return analyze_tab(tab)

# image_name = 'receipts3.jpg'
# f = open(os.path.join(parser_location, image_name))

# basic_scan(f)