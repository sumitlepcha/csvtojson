import csv
import datetime
import time
import os

#Enter the file to be read. This is the only place where we need to enter the file name.
#Enter input file name here
filename = "Copy File.csv"

#Enter the output file name here.
ofilename = "/home/deepshikha/Desktop/jsonoutput.cxmsg"

#Update the file name here. 
f = open(filename)

#read the file object
reader = csv.reader(f)

#Reading the number of columns in the file and this columncount is used for iteration.
for row in reader:
    col_count = len(row)
columncount = col_count
#print(columncount)

#This is to read the number of rows in the csv
rowcount = 0

f = open(filename)
rows = csv.reader(f)
#calcuating the number of rows
for countrow in rows:
    rowcount = rowcount +1
#print (rowcount)


#Update the file name here as well.
filereader = open(filename)
readfile = csv.reader(filereader)
#Adding rows to a list
rows = list(readfile)
#print (rows)


#This is the outpur file. File name shall not changed here.
open_json_file = open(ofilename,'w')


#Loop starts here and the output will be written into a file
i=1
while i < columncount:

# extracting the event id
    for eventid in rows:
#        print (eventid[0])
        if eventid[0] == 'eventid':
            print (eventid[i])
            eeventid = eventid[i]

#getting the timestamp
    st = int(time.time())
    systme = str(st)
    print(systme)

#"qname"|""|eventId|currentTime|event json
#63_1526293159849||EFM-63_1526293159849|1526293160630|
    print("host_",eeventid,"||",eeventid,"|",systme,"|{")
    open_json_file.write("host-"+eeventid+"||"+eeventid+"|"+systme+"|{")
    
    itercount = 0
    for row in rows:
        if row[0] == 'eventtype' or row[0] == 'eventsubtype' or row[0] == 'event-name' or row[0] == 'source' or row[0] == 'eventts' :
            print ('"',row[0],'":"',row[i],'",')
            open_json_file.write('"'+row[0]+'":"'+row[i]+'",')
            
            
        elif row[0] == 'addentity10':
            print("'",row[0],"':'",row[i],"'")
            open_json_file.write("'"+row[0]+"':'"+row[i]+"'")

        elif row[0] == 'msgBody':
            
            print('"',row[0],'":"','{')
            open_json_file.write('"'+row[0]+'":"'+'{')
            
        else:
            print("'",row[0],"':'",row[i],"',")
            open_json_file.write("'"+row[0]+"':'"+row[i]+"',")
                        
    print('}')
    open_json_file.write(str('}"}\n\n'))
    
    i = i+1
    itercount += 1

#Closing the that was opened for writing
open_json_file.close()
