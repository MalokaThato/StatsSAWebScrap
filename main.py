import urllib.request
import bs4 as BeautifulSoup
import pandas as  pd
import matplotlib.pyplot as plt

site = "http://www.statssa.gov.za/?page_id=3892"

page = urllib.request.urlopen(site)

soup = BeautifulSoup.BeautifulSoup(page)

tables  = soup.select_one('table')

count = 0

columns = []
states = []
year1 = []
year2 = []

for row in tables.findAll("tr"):
    cells = row.findAll('td')

    if count < 1:

        columns.append(cells[0].find(text=True))
        columns.append(cells[1].find(text=True))
        columns.append(cells[2].find(text=True))

    elif count > 1:
        print("Now printing info for rows")

        states.append(cells[0].find(text=True))

        year1.append(cells[1].find(text=True).replace(" ",""))

        year2.append(cells[2].find(text=True).replace(" ",""))

    count +=1

df = pd.DataFrame(columns=columns)

df[columns[0]] = states
df[columns[1]] = pd.to_numeric(year1)
df[columns[2]] = pd.to_numeric(year2)

#df[columns[1]] = pd.to_numeric

year = input("""Which year would you like to view the data?
1. %s
2. %s \n""" % (str(columns[1]), str(columns[2])))


print(df)

if year == columns[1]:

    df.plot(kind='bar', x=columns[0], y=columns[1])

elif year == columns[2]:
    df.plot(kind='bar', x=columns[0], y=columns[2])

else:
    print("Selection not known.")
    exit()

plt.show()
