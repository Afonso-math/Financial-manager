import pandas as pd
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference

def load_file(path):
    return pd.read_csv(path, encoding="utf-8")

def categorize_data(df):
    organized_data = {}
    data_amount = len(df)
    for x in range(1, data_amount - 1):
        if df.iloc[x, 3] != df.iloc[x + 1, 3]:
            category_name = df.iloc[x, 2]
            organized_data[category_name] = df.iloc[x, 3]
        else:
            organized_data[x] = df.iloc[x, 3]
    return organized_data

def excel_file(data, filename='/home/afonso/Documents/Financial manager.xlsx'):
    df = pd.DataFrame(list(data.items()), columns=["Category", "Value"])
    df.to_excel(filename, index=False)
    return filename

def main():
    df = load_file("/home/afonso/Documents/Date Description Category.txt")
    organized_data = categorize_data(df)
    final_file = excel_file(organized_data, filename="Financial manager.xlsx")

main()