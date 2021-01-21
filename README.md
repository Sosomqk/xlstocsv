Patched working version of https://github.com/xevo/xls2csv

The original version does not suport XLS. 
This version converts xls to xlsx and then to csv.

Dependencies: pandas, xlrd, openpyxl

Usage: `xlsx2csv /path/to/xls_or_xlsx_file/` # spits CSV lines on CLI
Usage: `xlsx2csv /path/to/xls_or_xlsx_file/ /path/to/file.csv` # writes in a CSV file