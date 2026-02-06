def count_vowels_cons(str):
    vowels="aeiouAEIOU"
    vow=0
    cons=0
    for ch in str:
        if ch.isalpha():
            if ch in vowels:
                vow +=1
            else:
                cons+=1  
    return vow,cons
str=input("enter a string to count vowels and consonants")
vowels,consonents=count_vowels_cons(str)
print("vowels",vowels)
print("cons",consonents)
