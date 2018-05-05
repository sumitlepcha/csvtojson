import csv

f = open("Column Header.csv")

#read the file object
reader = csv.reader(f)

for row in reader:
    col_count = len(row)
columncount = col_count
print(columncount)


filereader = open("Column Header.csv")

readfile = csv.reader(filereader)
rows = list(readfile)

i=1
while i < columncount:
    print("{")
    for row in rows:
        print('"',row[0],'"',':','"',row[i],'"')
        
    print("}")
    i = i+1
