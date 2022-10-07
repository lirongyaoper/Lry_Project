
#选择排序 荣耀版本
def lry_select_sort(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]

li=[9,6,8,7,1,2,3,4,5,6,45,54,32,17]
print(li)
lry_select_sort(li)
print("**************************")
print(li)