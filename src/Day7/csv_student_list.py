import csv;
with open("Day7/students.csv","r")as file:
    reader=csv.reader(file)

    for row in reader:
        if row[2]=="Pass":
            print(row[0])