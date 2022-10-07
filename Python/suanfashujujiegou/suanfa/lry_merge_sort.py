#归并排序
def merge(li,low,mid,hight):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= hight:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <=hight:
        ltmp.append(li[j])
        j +=1
    li[low:hight+1] =ltmp

def merge_sort(li,low,hight):
    if low < hight:
        mid  = (low+hight)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,hight)
        merge(li,low,mid,hight)


li=list(range(1000))
import random
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)