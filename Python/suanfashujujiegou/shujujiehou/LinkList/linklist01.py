class node():
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

class linklist():
    def __init__(self):
        self.head=None
        self.len=0

    def append_node(self,data):
        newnode=node(data,None)
        temp=self.head
        if self.head==None:
            self.head=newnode
        else :
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            self.len+=1

    def print_list(self):
        temp=self.head
        while temp.next!=None:
            print(temp.data,"-> ",end="")
            temp=temp.next
        print(temp.data)

    def del_node(self,number):
        temp=self.head
        j=0
        if self.len<number:
            print("error")
        else:
            while j<number-1:
                temp = temp.next
                j+=1
            temp.next=temp.next.next
            self.len-=1

    # def search_node(self,data):
    #     temp = self.head
    #     j = 0
    #     while temp.next!=None:
    #         temp = temp.next
    #         j += 1
    #         if temp.data==data:
    #             break
    #     return j

    def search_node(self,data):
        temp = self.head
        j = 0
        if temp.data == data:
            return j
        else:
            while temp.next!=None:
                temp = temp.next
                j += 1
                if temp.data==data:
                    break
            return j



    def change_data(self,number,newdata):
        temp = self.head
        j = 0
        if self.len < number:
            print("error")
        else:
            while j < number:
                temp = temp.next
                j += 1
            temp.data=newdata

    def insert(self,number,newdata):
        temp = self.head
        j = 0
        newnode=node(newdata)
        if self.len < number:
            print("error")
        else:
            while j < number-1:
                temp = temp.next
                j += 1
            newnode.next=temp.next
            temp.next=newnode
            self.len+=1

a=linklist()
for i in range (1,6):
    a.append_node(i)
print("append_node:  ",end="")
a.print_list()
# print("del_node(2):  ",end="")
# a.del_node(3)
# a.print_list()
# print("search_node(4):  ",end="")
# print(a.search_node(4))
print("change_data(1,999):  ",end="")
a.change_data(0,999)
a.print_list()
# print("a.insert(4,19909)):  ",end="")
# a.insert(4,19909)
# a.print_list()