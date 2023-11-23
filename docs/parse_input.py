import pandas 
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("html_file")
args = parser.parse_args()

tables = pandas.read_html(args.html_file)
transactions_table: pandas.DataFrame = tables[1]
for row_id, transaction in transactions_table.iterrows():
    # transaction: pandas.Series 
    date = transaction.get("Data operacji")
    if not date:
        print("Nie znaleziono daty operacji")
    description = transaction.get("Opis")
    if not description:
        print("Nie znaleziono opisu")
    amount = transaction.get("Kwota")
    if not amount:
        print("Nie znaleziono kwoty")
    print(description)
    print(amount) #float
    break
