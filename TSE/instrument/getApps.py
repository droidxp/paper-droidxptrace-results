#To get download key acess androzoo web site
#https://androzoo.uni.lu/ and ask for a key


key="0a34ff6b56a67972ad9f8bc60664287f689e50575f036d6bb637ce98b28ce9a7" 

import os
import csv

count = 213

with open('listInstru3.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] != "Benign":
            fileName = None
            fileName="benign-"+"app-"+str(count+1)+"-"+row[0]+".apk"
            print(fileName)
            os.system("curl -G -d apikey="+key+" -d sha256="+row[0]+" https://androzoo.uni.lu/api/download -o "+fileName)
        count=count+1