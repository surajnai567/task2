import excel
import pyexcel


filename_main = "NIFTY25JUN2010000PE.xlsx"
filename_coverted = "converted_data.xlsx"
temp = 0

for row in excel.get_excel_sheet(filename_main):
	excel.update_to_excel(filename_coverted, row)