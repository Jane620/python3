

# 体现交集的处理

def get_samepart(str1,str2):
    res = []
    for x in str1:
        for y in str2:
            if x == y:
                res.append(x)
    return res

str1 = 'spam'
str2 = 'scam'
str3 = [x for x in str1 if x in str2]
print(get_samepart(str1,str2))
print(str3)

