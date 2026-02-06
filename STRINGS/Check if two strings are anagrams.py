str1="listen"
str2="silent"

def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    count={}
    # Step 1: count frequency
    for ch in str1:
        count[ch]=count.get(ch,0)+1
        
    for ch in str2:
        if ch not in count or count[ch]==0:
            return False
        count[ch]-=1
    return True

print(anagram(str1,str2))