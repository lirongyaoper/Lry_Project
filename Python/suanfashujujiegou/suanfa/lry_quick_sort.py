import  random
def partition(li,left,right):
    index_random=random.randint(0, len(li-1))
    temp=li[index_random]
    while left<right:
        while left<right and li[right]>= temp:
            right -=1
        li[index_random]=li[right]
        while left < right and li[left] <= temp:
            left += 1
        li[index_random]=li[left]
    li[left]=temp
    return left

def lry_quick_sort(li,left,right):
    if left < right:
        mid=partition(li,left,right)
        lry_quick_sort(li,left,mid-1)
        lry_quick_sort(li,mid+1,right)


li=[7,9,11,2,7,4,89,54,32,110,99,34,12,45,55,97,151]
print(li)
lry_quick_sort(li,0,len(li)-1)
print(li)


# def partition(li,left,right):
#     index_random=random.randint(0, len(li-1))
#     temp=li[index_random]
#     while left<right:
#         while left<right and li[right]>= temp:
#             right -=1
#         li[left]=li[right]
#         while left < right and li[left] <= temp:
#             left += 1
#         li[right]=li[left]
#     li[left]=temp
#     return left
#
# def lry_quick_sort(li,left,right):
#     if left < right:
#         mid=partition(li,left,right)
#         lry_quick_sort(li,left,mid-1)
#         lry_quick_sort(li,mid+1,right)