from bs4 import BeautifulSoup as bs
import requests as req
import matplotlib.pyplot as plt
import numpy as np
import re

res = req.get("https://www.nasdaq.com/quotes/stock-quotes.aspx")
soup = bs(res.content, "html.parser")
tableNode = soup.select('td')

namelist = []
volumelist = []
percentlist = []

# Node 1~5 is one Company
# 1 : Name
# 3 : PctChange
# 4 : Volume
for i in range(1,21):
    if i%4 == 0:
        # Volume node will trim the html tags and comma, then convert to int
        volume_node = int(
            str(tableNode[i])
            .replace('<td>', '')
            .replace(' </td>', '')
            .replace(',', '')
            )
        volumelist.append(volume_node)

        # Trim the company name of the html tags
        company_node = re.sub(r'</div>\n</td>', '', re.sub(r'<td>(?s).*coName small">', '', str(tableNode[i-3])))
        # Trim common Filler words for company name
        company_node = re.sub(r',(s?).*','',company_node.replace('Inc.', '').replace('Group', '').replace('Ltd.', '').replace('Technology', ''))
        namelist.append(company_node.strip())

        # strip the html tags, and add - in case the percent change is negative
        percentchange = str(tableNode[i-1])
        if "▼" in percentchange:
            percentchange = float('-' + re.sub(r'\D.\D(?s).*</span></td>', '', re.sub(r'<td><span class=".*">', '', str(tableNode[i-1]))))
        else:
            percentchange = float(re.sub(r'\D.\D(?s).*</span></td>', '', re.sub(r'<td><span class=".*">', '', str(tableNode[i-1]))))

        percentlist.append(percentchange)

x = namelist
yval = volumelist
x_pos = [i for i, _ in enumerate(x)]
plt.figure(figsize=(10,6))
plt.bar(x_pos, yval, color='green')
plt.xticks(x_pos, x)
plt.xlabel("Company")
plt.ylabel("Volume")
plt.title("Most Active Sept.8, 2018")
plt.show()        

x = namelist
yval = percentlist
x_pos = [i for i, _ in enumerate(x)]
plt.figure(figsize=(10,6))
plt.bar(x_pos, yval, color='red')
plt.xticks(x_pos, x)
plt.xlabel("Company")
plt.ylabel("Δ%")
plt.title("Percent Change Sept.8, 2018")
plt.show()