###Python创建字典
## 1) 使用 { } 创建字典  dictname = {'key':'value1', 'key2':'value2', ..., 'keyn':valuen}
#使用字符串作为key
scores = {'数学': 95, '英语': 92, '语文': 84}
print(scores)
#使用元组和数字作为key
dict1 = {(20, 30): 'great', 30: [1,2,3]}
print(dict1)
#创建空元组
dict2 = {}
print(dict2)

## 2) 通过 fromkeys() 方法创建字典  dictname = dict.fromkeys(list，value=None)  其中，list 参数表示字典中所有键的列表（list）；value 参数表示默认值，如果不写，则为空值 None。
knowledge = ['语文', '数学', '英语']
scores = dict.fromkeys(knowledge, 60)
print(scores)


## 3) 通过 dict() 映射函数创建字典
#a = dict(str1=value1, str2=value2, str3=value3)
#方式1
demo = [('two',2), ('one',1), ('three',3)]
#方式2
demo = [['two',2], ['one',1], ['three',3]]
#方式3
demo = (('two',2), ('one',1), ('three',3))
#方式4
demo = (['two',2], ['one',1], ['three',3])
a = dict(demo)

keys = ['one', 'two', 'three'] #还可以是字符串或元组
values = [1, 2, 3] #还可以是字符串或元组
a = dict( zip(keys, values) )