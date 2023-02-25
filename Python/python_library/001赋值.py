# a = "zhangxiaoji"

# def foo(b):
#     print (">>>before id(b):",id(b))
#     b = "lizhiwei"
#     print (">>>after id(b):",id(b))
# print (">>>before id(a):", id(a))

# foo(a)
# print (">>>after id(a):", id(a))
# print(f"{a}")
######################################################################

# a = ["lirongyaoper"]
# def foo (b):
#     print(">>> before valve(b):",b)
#     print(">>> before id(b):",id(b))
#     b[0] = "lizhiwei"
#     b.append("guoqingwei")
#     print(">>> before valve(b):",b)    
#     print(">>> after id (b):",id(b))
# print(">>> before value(a):",a)
# print(">>> before id(a):",id(a))
# foo(a)
# print(">>> after value(a):",a)
# print(">>> after id(a):",id(a))
######################################################################
# import copy
# a = "lirongyao"
# a1 =a 
# a2 = copy.copy(a)
# a = "lirongyaoper"


# b = ["lirongyao",54,32,999]
# b1 = b
# b2 = copy.copy(b)
# b[1] = "lizhaoyao"
# b[3] = "cuixiujuan"


# c = [["中国","美国","加拿大"],"习近平",["朝鲜","日本"]]
# c1 = c
# c2 = copy.copy(c)
# c[0][2] = "英国"
# c[1] = "李荣耀"


a1 = "lirongyao"
list1 = [1,2,a1,3,"yes",[4,5]]
list2 = [6,7]
list3 = list1 +list2

list4 = list1.extend(list2)

list5 = list1.append(list2)




