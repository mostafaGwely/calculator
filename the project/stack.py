class Stack():
    def __init__(self):
        self.item=[]
    def pop(self):
       return self.item.pop()
    def push(self,val):
        self.item.append(val)
    def peek(self):
        try :
            return self.item[len(self.item)-1]
        except:
            return "0"
    def is_emptey(self):
        return  self.item == []

