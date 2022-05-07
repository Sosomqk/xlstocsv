#!/usr/bin/env python

import csv
import re
import sys
import pandas as pd

if sys.version[0] == '2':
	reload(sys)
	sys.setdefaultencoding("utf-8")

if (len(sys.argv) < 2):
	print('''Invalid file path!
		Usage: xls2csv /path/to/xls_file  # for command line output
		Usage: xls2csv /path/to/xls_file /path/to/csv_file  # for writing in a csv file
	''')
	sys.exit(1)

argv_len = len(sys.argv)
workbook = pd.read_excel(sys.argv[1], header=None, engine='xlrd') # only for xls

if (argv_len > 2): # if output file is provided
    csv_file = open(sys.argv[2], 'w')
    writer = csv.writer(csv_file)

for row in workbook.values:
	if (argv_len > 2): # if output file is provided
		writer.writerow(row)
	else:
		row2str = ','.join(str(s) for s in row)
		row2str = re.sub(r"00\:00\:00|\s", '', row2str)
		row2str = row2str.rstrip('.')
		print(row2str)

sys.exit(0)
