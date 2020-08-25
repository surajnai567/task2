import pyexcel


# this function reads excel sheet row by row with pyexcel module
def get_excel_sheet(filename, sheet_number=0):
	sheet = pyexcel.get_sheet(file_name=filename, sheet_name=0)
	sheet.name_columns_by_row(0)
	for row in sheet:
		yield row


def update_to_excel(filename, data, sheet_number=0):
	sheet = pyexcel.get_sheet(file_name=filename, sheet_name=sheet_number)
	sheet.row += data
	sheet.save_as(filename)