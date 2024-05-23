import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    '''The purpose of using pathlib, stem is that we can get the first part of the element 
    without any string manipulation'''
    filename = Path(filepath).stem 
    invoice_nr,invoice_date = filename.split('-')
    pdf.set_font(family="Times",size=10,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}",ln=1)
    pdf.cell(w=50,h=8,txt=f"Date {invoice_date}",ln=1)
    df = pd.read_excel(filepath,sheet_name='Sheet 1')

    #extracted the column name
    invoice_header =df.columns
    invoice_header = [items.replace("_"," ").title() for items in invoice_header]
    pdf.set_font(family="Times",size=12,style="B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=8,txt=invoice_header[0],border=1)
    pdf.cell(w=70,h=8,txt=invoice_header[1],border=1)
    pdf.cell(w=40,h=8,txt=invoice_header[2],border=1)
    pdf.cell(w=30,h=8,txt=invoice_header[3],border=1)
    pdf.cell(w=30,h=8,txt=invoice_header[4],border=1,ln=1)

    #extracted the data from excel
    for index,row in df.iterrows():
        pdf.set_font(family="Times",size=12,style="B")
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=8,txt=str(row["product_id"]),border=1)
        pdf.cell(w=70,h=8,txt=str(row["product_name"]),border=1)
        pdf.cell(w=40,h=8,txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30,h=8,txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30,h=8,txt=str(row["total_price"]),border=1,ln=1)

    
    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times",size=12,style="B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=8,txt="",border=1)
    pdf.cell(w=70,h=8,txt="",border=1)
    pdf.cell(w=40,h=8,txt="",border=1)
    pdf.cell(w=30,h=8,txt="",border=1)
    pdf.cell(w=30,h=8,txt=str(total_sum),border=1,ln=1)

    pdf.set_font(family="Times",size=12,style="B")
    pdf.cell(w=30,h=8,txt=f"The Total Price is {total_sum}.")


    pdf.output(f"PDFs/{filename}.pdf")