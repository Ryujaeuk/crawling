import requests
from urllib.parse import urlparse

keyword = "아이유"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
result = requests.get(urlparse(url).geturl(),
         headers={"X-Naver-Client-Id" : "F1ebJdnJeFNkXOQDgPCH",
                  "X-Naver-Client-Secret" : "AtM7cIY7Lj"})


# print(json_obj['lastBuildDate'])
# print(json_obj['total'])
# print(json_obj['start'])
# print(json_obj['display'])
json_obj = result.json()
for item in json_obj['items']:
    print(item)