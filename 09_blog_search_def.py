# 함수로 만들기

import requests
from urllib.parse import urlparse

def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
                                                            + "&display=" + str(display) \
                                                            + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "X2arOC3YqPOkU48Gebv8",
                                   "X-Naver-Client-Secret": "h4xz3kKnLY"})
    return result.json()

json_obj = get_api_result("아이유", 100, 101)

# print(json_obj)

for item in json_obj['items']:
    print(item)