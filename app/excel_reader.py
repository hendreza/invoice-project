# open the correct workbook

import pandas as pd


file_path = "/home/hendre/Documents/code/invoice-project/input/invoice.xlsx"
file_name = pd.ExcelFile(file_path)
sheet = "invoice info"

df = pd.read_excel(file_name, sheet_name=sheet)
print(df.head())