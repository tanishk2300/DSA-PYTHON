str="swiss"

def non_repeating(str):
    count={}
    # Step 1: count frequency
    for ch in str:
        count[ch]=count.get(ch,0)+1
    # Step 2: find first non-repeating
    for ch in str:
        if  count[ch]==1:
            return ch
    return None

print("non repeating character :",(non_repeating(str)))
