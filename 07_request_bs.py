# Requests 라이브러리를 이용한 web crawling
import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"

def get_bp_info(url):
    result = requests.get(url =url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    #블로그 이름
    name = bs_obj.find("div",{"class":"profile-name"})
    name_detail = name.find("h1",{"class":"case27-primary-text"})
    name_detail_text = name_detail.text

    #블로그 위치
    location = bs_obj.find("div", {"class":"cover-buttons"})
    location_deatil = location.find("span",{"class":"button-label"})
    location_detail_text = location_deatil.text

    #website link 버튼
    website = bs_obj.find("div", {"class":"buttons medium button-outlined"})
    website_link = website.find("a")['href']
    # website_link_text = website_link
    # website_link = bs_obj.find("span", {"class":"button-label"})

    dictionary1 = {}
    dictionary1['name'] = name_detail_text
    dictionary1['location'] = location_detail_text
    dictionary1['link'] = website_link
    return dictionary1

result = requests.get(url =url)
bs_obj = BeautifulSoup(result.content, "html.parser")

lf_items = bs_obj.findAll("div", {"class":"lf-item"})
hrefs = [div.find("a")['href'] for div in lf_items ]

for number in range(0, 10):
    dic_result = get_bp_info(hrefs[number])
    print(dic_result)