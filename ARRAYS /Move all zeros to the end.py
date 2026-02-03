arr=[0,1,0,2,3,4,0]#this is an array .

zero=[]#here all zeros are store .
non_zero=[]# here nonzeros are stored.
for x in arr:# we create here loop .
    if x==0:
            zero.append(x)#all zeros appending in zero=[].
    else:
            non_zero.append(x)#all non zero appending in non_Zeros=[].
    
result=non_zero+zero#here all non zero and zero which is stored in lists are added .

print(result)#output= [1, 2, 3, 4, 0, 0, 0] .
