str1="abcd"
str2="cdab"
def rotaion_cheak(str1,str2):
    if len(str1)!=len(str2):
        return False
    return str2 in (str1+str1)
print(rotaion_cheak(str1,str2))
