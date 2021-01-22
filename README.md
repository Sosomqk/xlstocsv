XLS to CSV converter.
Very fast, extremely light and easy to use.

Installation: `pip install xls2csv`

Complementary package to xlsx2csv(https://github.com/xevo/xls2csv) - great tool, but does not work with .xls files

`xls2csv` works only with xls file (for legacy systems and 'legacy' clients :))

Dependencies: 
    - python > 2.7
    - pandas, 
    - xlrd

Usage: `xls2csv /path/to/xls_or_xlsx_file/` # spits CSV lines on CLI
Usage: `xls2csv /path/to/xls_or_xlsx_file/ /path/to/file.csv` # writes in a CSV file
