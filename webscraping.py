from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'example.com'

page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')





soup.find_all("tbody")

gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])



target_table = None
for table in soup.find_all('table'):
    thead = table.find('thead')
    if thead and "Stock Revenue" in thead.get_text():
        target_table = table
        break

if target_table:
    for row in target_table.find('tbody').find_all('tr'):
        col = row.find_all("td")
        date = col[0].text.strip()
        revenue = col[1].text.strip()
        tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)