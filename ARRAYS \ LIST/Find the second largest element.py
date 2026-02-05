arr = [3,4,6,4,8,7]

largest = second_largest =float('-inf')#-inf means negative infinity.

for i in arr:
    if i > largest:
        second_largest=largest#we equalise second largest number to largest number.
        largest=i# largest number is i in the array.
    elif i>second_largest and i != largest:# i must be greater and not equal to largest nummber . 
        second_largest=i


print("second largest number:",second_largest)#output="second largest number: 7".
