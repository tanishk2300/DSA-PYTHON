
#Sort elements by frequency.
# this is use in frequency .
'''for x in arr:
        freq[x] = freq.get(x, 0) + 1'''
arr=[1,1,2,2,2,3]
def sort_freq(arr):# it help to count and arrange the numbers in frequency way like which has max number of a number .
    freq={}
    # Step 1: Count frequency
    for i in arr:
        freq[i]=freq.get(i,0)+1
        # Step 2: Sort based on frequency
    sorted_item=sorted(freq.items(), key=lambda i:i[1],reverse=True)
        # Step 3: Build result array
    result=[]
    for item ,count in sorted_item:
        result.extend([item]*count)
    return result
print(sort_freq(arr))
