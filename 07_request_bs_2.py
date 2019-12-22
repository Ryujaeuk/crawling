# Requests 라이브러리를 이용한 web crawling
import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"

def get_bp_info(url):
    result = requests.get(url =url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    #블로그 이름
    name = bs_obj.find("div",{"class":"profile-name"})
    name_detail = name.find("h1",{"class":"case27-primary-text"})
    print(name_detail.text)

    #블로그 위치
    location = bs_obj.find("div", {"class":"cover-buttons"})
    location_deatil = location.find("span",{"class":"button-label"})
    print(location_deatil.text)

    #website link 버튼
    website = bs_obj.find("div", {"class":"buttons medium button-outlined"})
    website_link = website.find("a")
    # website_link = bs_obj.find("span", {"class":"button-label"})
    print(website_link['href'])

    dictionary1 = {}
    dictionary1['name'] = name_detail
    dictionary1['location'] = location_deatil
    dictionary1['link'] = website_link
    return dictionary1

dic_result = get_bp_info(url)

print(dic_result)
