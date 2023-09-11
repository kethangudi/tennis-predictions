from bs4 import BeautifulSoup
import requests
import lxml.html as lh
import pandas as pd
#import mechanize
import csv
 
#br = mechanize.Browser()
#url = "https://www.atptour.com/en/players/"
#br.set_handle_robots(False)
#br.set_handle_equiv(False) 

#br.open('https://www.atptour.com/en/players/')
#br.select_form(nr=0)
#print (br.geturl())

#csvFile = pd.read_csv('links.csv')
file = open('links.csv')
data= csv.reader(file)
csvFile = list(data)
# displaying the contents of the CSV file
#print(csvFile)
desired_queries = csvFile
#desired_queries2 = ['/player-stats?year=0&surfaceType=clay','/player-stats?year=0&surfaceType=hard',
                    #'/player-stats?year=0&surfaceType=grass']
desired_queries2 = ['/player-stats?year=0&surfaceType=grass']
offense = 0;
defense = 0; 
style = []
player = []
for i in desired_queries:
    for query in i:
        for query2 in desired_queries2:
            url = 'https://www.atptour.com/en/players/' + query + query2
            page = requests.get(url)
            doc = lh.fromstring(page.content)
            tr_elements = doc.xpath('//tr')
            #off = []
            x = 0
            #for t in tr_elements[x]:
             #   name = t.text_content()
             #   print(name) 

            #i = 0
            for t in tr_elements[11]:
            #   i+=1
                name=t.text_content()
                num = len(name)
                if(len(name) ==12):
                    offense = int(name[5:7])
                    #print (cull)
                    #off.append(name)
                if(len(name) ==11):
                    offense = int(name[5:6])
                    #print (cull)
                    #off.append(name)
            #defe = []
            for t in tr_elements[19]:
            #   i+=1
                name=t.text_content()
                num = len(name)
                if(len(name) == 12 ):
                    #print (name[5:7])
                    defense = int(name[5:7])
                    #defe.append(name)
                if( len(name) == 11):
                    defense = int(name[5:6])


            #html_text = requests.get('https://www.atptour.com/en/players/jan-lennard-struff/sl28/player-stats').text
            #soup = BeautifulSoup(html_text,'lxml')
            #jobs = soup.find('table',class_='mega-table')
            #print(jobs)
            style.append(offense-defense)
        player.append(style)
        style = []


#with open("style.csv","w+") as my_csv:
#    newarray = csv.writer(my_csv)
#    newarray.writerows(player)

for i in player:
    for j in i:
       print(j, end=" ")
    print()
