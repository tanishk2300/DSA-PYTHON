class stack:
    def __init__(self, size):
        self.stack=[None]*size # create fixed size array
        self.size=size
        self.top=-1 # stack is empty
    def push(self,value):
        if self.top==self.size-1:
            print("stack overflow")
            return
        self.top+=1
        self.stack[self.top]=value
    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
            return
        value =self.stack[self.top]
        self.top-=1#Means stack empty.
        return value
    def peek(self):
        if self.top==-1:#Means stack empty.
            return None
        return self.stack[self.top]
    def is_empty(self):
        return self.top==-1
    

# s=stack(5)
# s.push(10)
# s.push(20)
# s.push(30)


s = stack(5)

s.push(10)
s.push(20)
s.push(30)

print(s.pop())   # 30
print(s.peek())  # 20



        

# print(s.pop())
# print(s.peek())
