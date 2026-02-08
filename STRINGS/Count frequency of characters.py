str="hello guyss"
def count_frequency(str):
    count={}
    for ch in str:
        count[ch]=count.get(ch,0)+1

    return count
print(count_frequency(str))
