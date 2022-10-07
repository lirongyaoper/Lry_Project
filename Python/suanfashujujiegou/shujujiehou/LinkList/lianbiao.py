class Node:
    def __init__(self, item=None):
        self.item= item
        self.next=None

def create_linklist_head(li):
    head=Node(li[0])
    for element in li[1:]:
        node=Node(element)
        node.next=head
        head=node
    return head

def print_linklist(lk):
    while lk != None:
        print(lk.item,end=", ")
        lk=lk.next

abc=create_linklist_head([1,2,3,4])
print_linklist(abc)
print("********************************************")
def create_linklist_tail(li):#正序列表
    head=Node(li[0])
    tail=head
    for element in li[1:]:
        node=Node(element)
        tail.next=node
        tail=node
    return head



abc2=create_linklist_tail([1,2,3,4,5])
print_linklist(abc2)



