import csv

filereader = open("IB_Fraud_R01.csv")

readfile = csv.reader(filereader)
rows = list(readfile)

jsondict = dict()

i=1
while i < 37:
    print("{")
    for row in rows:
        if row[0] == 'msgBody':
            print('"',row[0],'"',':','"',row[i])
        else:
            print('"',row[0],'"',':','"',row[i],'"')
        
    print("}",'"',"}")
    i = i+1
