import os
import re
import Levenshtein

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

end_of_lines_to_search = r'\$?[\d]+[\.,][\d]{1,2}$'

image_name = 'receipts3.jpg'
os.system('./ocr.sh ' + image_name)

raw_data = []

with open(image_name + '1.txt','r') as file:
	for line in file.read().splitlines():
		match = re.search(end_of_lines_to_search, line)
		if match != None:
			raw_data.append({re.sub(r'(\s)$', '', line[:match.start()]) : match.group(0)})


print raw_data
