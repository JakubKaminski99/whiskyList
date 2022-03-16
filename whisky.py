from requests_html import HTMLSession
 
url = 'https://sklep-domwhisky.pl/pol_m_Scotch-Whisky_Single-malt-whisky-438.html' 
session = HTMLSession()
res = session.get(url)
res.html.render()
lis=list()
products = res.html.xpath('//*[@id="search"]', first = True)
for item in products.absolute_links:
    res = session.get(item)
    if "product-pol" in str(res.html):
        name = res.html.find('div.product_info', first = True).text
        price = res.html.find('div.product_section')[1].text
        lis.append(f"{name} with the price of {price}")
        print(price)      
with open("whisky.html", "w") as file:
    for item in lis:
        file.write(f"{item} \n")

