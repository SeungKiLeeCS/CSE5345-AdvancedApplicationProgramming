import csv
import sys
import json
import operator
import matplotlib.pyplot as plt

# example code from https://docs.python.org/3/library/csv.html
rowlist= []
with open('./worldcup.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in csvreader:
        rowlist.append(row)

csvfile.close()

elementlist= []

for i in rowlist:
    for j in i:
        elementlist.append(j.split(','))


jsonlist = []
        
for i in range(1,22):
    a_json_obj = {
        elementlist[0][0]:elementlist[i][0],        
        elementlist[0][1]:int(elementlist[i][1]),        
        elementlist[0][2]:elementlist[i][2],        
        elementlist[0][3]:elementlist[i][3],        
        elementlist[0][4]:elementlist[i][4],        
        elementlist[0][5]:elementlist[i][5],        
        elementlist[0][6]:elementlist[i][6],        
        elementlist[0][7]:int(elementlist[i][7]),
        elementlist[0][8]:int(elementlist[i][8]),        
        elementlist[0][9]:int(elementlist[i][9])            
    }
    
    jsonlist.append(a_json_obj)

jsonlist = sorted(jsonlist, key=lambda k: k['goalsScored'], reverse=True)

for i in range (0,5):
    mkfilename = "worldcupjson" + str(i+1) + '.json'
    with open(mkfilename, 'w') as outfile:
        json.dump(jsonlist[i], outfile, indent = 2)
    outfile.close()

# Extract the two values needed
yearlist = []
goallist = []

for i in range (0,5):
    yearlist.append(jsonlist[i].get('year'))
    goallist.append(jsonlist[i].get('goalsScored'))

x = yearlist
yval = goallist
x_pos = [i for i, _ in enumerate(x)]
# Graph
plt.figure(figsize=(10,6))
plt.bar(x_pos, yval, color='skyblue')
plt.xticks(x_pos, x)
plt.xlabel("World Cup Year")
plt.ylabel("# of Goals")
plt.title("5 World Cups with Most Goals")
plt.show()