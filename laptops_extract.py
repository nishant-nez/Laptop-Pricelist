# Program that displays the price and model of three different laptop brands entered by the user from itti.com

import requests
from bs4 import BeautifulSoup


brand = input('Enter your choice of laptop brand: asus/acer/alienware : ')
url = "https://itti.com.np/laptops-by-brands/{}-laptop-nepal?product_list_limit=36".format(brand.lower())

raw_html = requests.get(url)
html_doc = BeautifulSoup(raw_html.content, 'html.parser')

prods = html_doc.find_all(class_="product-item-link")
prods_list = []

for item in prods:
    try:
        prods_list.append(item.string.strip())
    except:
        pass


prices = html_doc.find_all(class_="price")
price_list = []

for pp in prices:
    try:
        price_list.append(pp.string.strip())
    except:
        pass


print("\n\nINDEX       PRICE\t\t\t\t\t\tPRODUCT\n")
for i in range(len(prods_list)):
    print(i + 1, '\t', price_list[i], '\t\t', prods_list[i])


print()
print()
