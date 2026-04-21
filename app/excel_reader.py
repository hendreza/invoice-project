# open the correct workbook

import pandas as pd


file_path = "/home/hendre/Documents/Code/invoice-project/input/invoice.xlsx"
file_name = pd.ExcelFile(file_path)
sheet = "invoice info"

df = pd.read_excel(file_name, sheet_name=sheet)

for index, row in df.iterrows():
    if index == 0:
        print(row["invoice_number"], "|", row["invoice_date"], "|", row["name"], "|", row["last_name"], "|", row["description"], "|",  row["total"])

