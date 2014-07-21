from decimal import *
import os
import shutil
from PIL import Image
import tre
import re
import codecs
import json

DEBUG = False

def debug(x):
	if DEBUG:
		print x

class OkraParseException(Exception):
	pass

parser_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# f = open(os.path.join(parser_location, 'bundled-resource.jpg'));
images_location = os.path.join(os.path.dirname(parser_location), 'images/')

config_file = open(os.path.join(parser_location, 'parser-config.json'), 'r')
config = json.load(config_file, 'ascii')

reverse_map_file = open(os.path.join(parser_location, 'map.json'), 'r')
reverse_map = json.load(reverse_map_file, 'ascii')

reverse_name_map_file = open(os.path.join(parser_location, 'name-map.json'), 'r')
reverse_name_map = json.load(reverse_name_map_file, 'ascii')

character_map = {}
name_character_map = {}

for key in reverse_map:
	for letter in reverse_map[key]:
		character_map[str(letter)] = str(key)

for key in reverse_name_map:
	for letter in reverse_name_map[key]:
		name_character_map[str(letter)] = str(key)		

debug(config)
debug(character_map)
debug(reverse_name_map)

ere_end_of_line_price = r'\$?[0-9]+[\.,][0-9]{2}$'

string_total = 'total'
string_subtotal = 'subtotal'
image_folder = 'images'

def analyze_tab(tab_param):
	debug(tab_param)

	tab = {}
	tab['items'] = []
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
		tab['items'].append({'name' : item['description'], 'price' : float(price_fix(item['value']))})
		# tab['items'][item['description']] = price_fix(item['value'])
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
	elif (avail_tax and avail_subtotal):
		if not (meta_tax + meta_subtotal == item_total or meta_subtotal == item_total):
			raise OkraParseException('8')
		elif (meta_tax + meta_subtotal == item_total):
			tab['meta'] = {string_total : item_total, string_subtotal : meta_subtotal, string_tax : meta_tax}
		elif (meta_subtotal == item_total):
			tab['meta'] = {string_total : item_total, string_subtotal : meta_subtotal, string_tax : 0}
		else:
			raise OkraParseException('9')
	elif avail_tax:
		tab['meta'] = {string_total : item_total, string_subtotal : item_total - meta_tax, string_tax : meta_tax}
	else:
		raise OkraParseException('Nuttin')

	print tab
	return tab

def price_fix(price_string_param):
	final_price_string = ''
	for letter in price_string_param:
		# print letter
		if not letter in '0123456789.':
			# print 'not numeric letter'
			if letter in character_map:
				debug('letter in character map')
				final_price_string += character_map[letter]
		else:
			# print 'is numeric letter'
			final_price_string += letter

	# return Decimal(price_string_param.strip('$'))
	debug('price fix')
	debug(price_string_param)
	debug(final_price_string)
	return Decimal(final_price_string)

def name_fix(name_string_param):
	final_name_string = ''
	for letter in name_string_param:
		# print letter
		if not letter in 'abcdefghijklmnopqrstuvwxyz':
			# print 'not numeric letter'
			if letter in name_character_map:
				# debug('letter in character map')
				final_name_string += name_character_map[letter]
		else:
			# print 'is numeric letter'
			final_name_string += letter

	# return Decimal(price_string_param.strip('$'))
	debug('name fix')
	debug(name_string_param)
	debug(final_name_string)
	return final_name_string

def full_scan(image_name):
	full_image_path = images_location + image_name

	image = Image.open(full_image_path)
	# if image.size[0] >= 1600:
	ratio = float(1600)/float(image.size[0])
	image = image.resize((1600, int(image.size[1]*ratio)))
	image = image.transpose(Image.ROTATE_270)
	image.save(full_image_path,'JPEG',quality=100)

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
				if len(tmp_description) > 2:
					raw_tab_data.append({'description' : tmp_description, 'value' : tmp_value})


	tre_fuzzyness = tre.Fuzzyness(maxerr = 3)
	tab_meta = {}

	cut_off_meta = 0

	for raw_item in raw_tab_data:
		raw_item_description = raw_item['description']
		raw_item_value = raw_item['value']
		matches_to_compare = []
		for parser_key in config['mid_parsers']:
			tre_matcher = tre.compile(config['mid_parsers'][parser_key]['ere'], tre.EXTENDED)
			tre_match = tre_matcher.search(name_fix(raw_item_description), tre_fuzzyness)
			debug('xxxxxxxxxxxxxxxxxxxxxxxxxx')
			debug(name_fix(raw_item_description) + ' XXX ' + config['mid_parsers'][parser_key]['ere'] + ' XXX ' + raw_item_value)
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
			tab_meta[min[1]] = raw_item_value
		else:
			debug('SHOULD HAVE BEEN CUT OFF')
			if cut_off_meta < 1:
				tab_items.append(raw_item)

	tab = {'tab_items' : tab_items, 'tab_meta' : tab_meta}
	print tab

	# print analyze_tab(tab)
	x = analyze_tab(tab)
	print x
	return x


	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################
	######################

	######################
	######################
	######################
	######################

	######################
	######################
	######################