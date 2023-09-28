####Python dict字典方法完全攻略（全）
###keys()、values() 和 items() 方法
scores = {'数学': 95, '语文': 89, '英语': 90}
print(scores.keys())
print(scores.values())
print(scores.items())

# 使用 for in 循环遍历它们的返回值
a1= {'数学': 95, '语文': 89, '英语': 90}
for k in a1.keys():
    print (k,end=' ')
print("\n---------------")
for v in a1.values():
    print(v,end=' ')
print("\n---------------")
for k,v in a1.items():
    print("key:",k," value:",v)