import csv

thisset = []
with open('names.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    #svFile = set(csvFile)
    for query in csvFile:
     #   query2 = set(query)
        thisset.append(query[0])
thisset = set(thisset)
with open ('names.csv','w',newline = '') as csvfile:
          my_writer = csv.writer(csvfile)
          my_writer.writerows(thisset)
#print(set(thisset))