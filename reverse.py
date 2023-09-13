#reverse a string
def reverseString(str1):
    return str1[::-1]

def reverseString2(str1):
    strList = list(str1)
    strList.reverse()
    revStr = "".join(strList)
    return revStr

def reverseString3(str1):
    revStr = ""
    for c in str1:
        revStr = c + revStr
    return revStr

def reverseString4(str1):
    revStr = ""
    for c in reversed(str1):
        revStr += c
    return revStr

#reverse the word order
def reverseString5(str1):
    strList = str1.split(" ")
    strList.reverse()
    return " ".join(strList)

print(reverseString("mother"))
print(reverseString2("hello"))
print(reverseString3("backwards"))
print(reverseString4("again"))
print(reverseString5("what the heck"))


