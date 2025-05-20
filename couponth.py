import requests
from bs4 import BeautifulSoup
import time

url = 'https://coupon.co.th/'
response = requests.get(url)


time.sleep(2)
# print(response.text)
html = response.text
soup = BeautifulSoup(html,'html.parser')
data = soup.find_all('div',{'class':'row one-kortingscode'})
# print(data)

for element in data[:7]:
    print(element.a['data-aff-href'])
    title = element.find('span')
    desc = element.find_all('p')
    print(title.text.strip())
    # print(desc.text)
    print(desc[1].text)
    print('----------------')







# print(html)
# with open('output_tops.html','w',encoding='utf-8') as file:
#     file.write(html)