import time
def cal_time(func):
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=func(*args,**kwargs)
        t2=time.time()
        print("%s running time: %s secs."%(func.__name__,t2-t1))
        return result
    return wrapper
@cal_time
def linear_search(li,value):
    for ind,val in enumerate(li):
        if val==value:
            return ind
    else:
        return None
@cal_time
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
li=list(range(10000000))
linear_search(li,9999999)
binary_search(li,9999999)