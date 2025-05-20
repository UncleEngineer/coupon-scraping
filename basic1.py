import requests
from bs4 import BeautifulSoup
import time

url = 'https://xn--42cah7d0cxcvbbb9x.com/'
response = requests.get(url)

time.sleep(2)
# print(response.text)
html = response.text

# <td class="em bg-em g-u">49,542.88</td>

soup = BeautifulSoup(html,'html.parser')

price = soup.find_all('td',{'class':'em bg-em g-u'})

print(price)

print('ทองคำแท่ง-รับซื้อ: ', price[0].text)
print('ทองคำแท่ง-ขายออก: ', price[1].text)
print('ทองรูปพรรณ-รับซื้อ: ', price[2].text)
print('ทองรูปพรรณ-ขายออก: ', price[3].text)


# print(html)
# with open('output.html','w',encoding='utf-8') as file:
#     file.write(html)