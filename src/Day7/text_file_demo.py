file=open("sample.txt","w")
file.write("Hello,this is a file handling example.")
file.close()
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

#context managers with open
with open("sample.txt","r") as file:
    content=file.read()
    print(content)

#error handling with try/except
try:
    with open("missing.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

#csv Parsing Basics
import csv;
with open("Day7/data.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#Excel 
import openpyxl
workbook=openpyxl.load_workbook("Day7/student_clg.xlsx")
sheet=workbook.active
for row in sheet.iter_rows(values_only=True):
    print(row)

