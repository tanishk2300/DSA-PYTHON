str="hello, hows you the day  ."

def replace_spaces(str):
    for ch in str:
        ch=str.replace(" ","%20")
    return ch
print(replace_spaces(str))

              
