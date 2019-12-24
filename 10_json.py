json = {"name":"iu",

        "age":"27",
        "where":"anywhere",
        "phone-number":"010-1111-9999",
        "friends":[{"name":"유인나", "age":"38"},
                   {"name":"노홍철", "age":"40"}]
        }

print(json.keys())# key 값

print(json['name'])# vlaue 값
print(json['age'])
print(json['where'])
print(json['phone-number'])

# print(json['friends'])

friends = json["friends"]
for friend in friends:
    print(friend) # friend 전체추출
    print(friend['age']) # friend 부분추출
