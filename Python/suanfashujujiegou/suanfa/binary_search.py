#二分查找法
def binary_search(li,value):
    left=0
    right=len(li)-1
    while left<=right:
        mid=(left+right)//2
        if li[mid]==value:
            return mid
        elif  li[mid]>value:
            right=mid-1
        else:
            left=mid+1
    else:
        return None


li=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38]

print(binary_search(li,22))