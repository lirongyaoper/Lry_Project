
import  random
from lry_cal_time import *
@lry_cal_time
def lry_insert_sort(li):
    for i in range(1,len(li)):
        temp = li[i]
        j=i-1
        while j >= 0 and li[j] > temp:
            li[j+1] = li[j]
            j -= 1
        li[j+1]=temp
        #print(li)



li = [9,8,7,6,5]
random.shuffle(li)
print(li)
print("*********************************************************")
lry_insert_sort(li)
print(li)
