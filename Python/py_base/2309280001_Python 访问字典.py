tuple1 = (['one',88],['two',26],['three',100],['four',-59])
diclry = dict(tuple1)
# dictname[key]  其中，dictname 表示字典变量的名字，key 表示键名。注意，键必须是存在的，否则会抛出异常。

print(diclry['four'])
# dictname.get(key[,default])  dictname 表示字典变量的名字；key 表示指定的键；default 用于指定要查询的键不存在时，此方法返回的默认值，如果不手动指定，会返回 None
print(diclry.get('three'))
print(diclry.get('five','lryno'))