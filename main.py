import excel
import pyexcel
from datetime import datetime
import timeparsing
import datetime


filename_main = "NIFTY25JUN2010000PE.xlsx"
filename_coverted = "converted_data.xlsx"
temp = 0

prev = ""
first = True
for row in excel.get_excel_sheet(filename_main):
	if first or datetime.datetime.combine(row[1], row[2]) - \
		datetime.datetime.combine(prev[1],prev[2]) >= \
		datetime.timedelta(days=0, minutes=15):
		prev = row
		first = False
		print(row)
		excel.update_to_excel(filename_coverted, row)

