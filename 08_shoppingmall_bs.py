# Requests 라이브러리를 이용한 web crawling
import requests
import bs4

headers = {'User-Agent' : 'Mozolla/5.0'} #1
url = "http://jolse.com/category/toners-mists/1019/"

result = requests.get(url , headers=headers) #2 무단으로 들어가는 것이 아닌 클릭해서 들어가는 것처럼하는 소스

bs_obj = bs4.BeautifulSoup(result.text)

ul = bs_obj.find("ul", {"class":"prdList grid4"})
boxes = ul.findAll("div", {"class":"box"})

def get_product_info(box):
    ptag = box.find("p", {"class":"name"})
    spans_name = ptag.findAll("span")

    ul = box.find("li")
    spans_price = ul.findAll("span")

    # link = box.find("div", {"class": "thumbnail"})
    atag =box.find("a")
    link = atag['href']

    name = spans_name[0].text
    price = spans_price[1].text

    return {"name" : name, "price" : price, "link" : link}

for box in boxes:
    product_info = get_product_info(box)
    print(product_info)



# def get_bp_info(url):
#     result = requests.get(url =url)
#     bs_obj = BeautifulSoup(result.content, "html.parser")
#
#     #블로그 이름
#     name = bs_obj.find("div",{"class":"profile-name"})
#     name_detail = name.find("h1",{"class":"case27-primary-text"})
#     print(name_detail.text)
#
#     #블로그 위치
#     location = bs_obj.find("div", {"class":"cover-buttons"})
#     location_deatil = location.find("span",{"class":"button-label"})
#     print(location_deatil.text)
#
#     #website link 버튼
#     website = bs_obj.find("div", {"class":"buttons medium button-outlined"})
#     website_link = website.find("a")
#     # website_link = bs_obj.find("span", {"class":"button-label"})
#     print(website_link['href'])
#
#     dictionary1 = {}
#     dictionary1['name'] = name_detail
#     dictionary1['location'] = location_deatil
#     dictionary1['link'] = website_link
#     return dictionary1
# dic_result = get_bp_info(url)
#
# print(dic_result)
