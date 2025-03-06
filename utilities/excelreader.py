
import openpyxl

def excelReader(sheetname):
    # Load the workbook
    #print(sheetname)
    workbook = openpyxl.load_workbook('utilities/dsAlgo_TestData.xlsx')
    # Select the worksheet by name
    sheet = workbook[sheetname]
    # Read the header row
    headers = [cell.value for cell in sheet[1]]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(dict(zip(headers, row)))

    return data
# Example usage
if __name__=='__main__':
    sheetname = 'Login'

    data = excelReader(sheetname)

