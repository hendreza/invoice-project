# open the correct workbook

import pandas as pd


file_path = "/home/hendre/Documents/Code/invoice-project/input/invoice.xlsx"
file_name = pd.ExcelFile(file_path)
sheet = "invoice info"

df = pd.read_excel(file_name, sheet_name=sheet)


for index, row in df.iterrows():
    raw_date = row["invoice_date"]
    formatted_date = raw_date.strftime("%Y-%m-%d")


    raw_total = row["total"]
    formatted_total = float(raw_total)
    final_total = f"{formatted_total:.2f}"

    print(row["invoice_number"], "|", formatted_date, "|", row["name"], "|", row["last_name"], "|", row["description"], "|",  final_total)

