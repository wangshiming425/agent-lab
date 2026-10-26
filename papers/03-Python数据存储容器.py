#1.列表list(有序加可重复+修改)
list_1=[1,3,7,9,11]
list_2=[2,4,6,8,10]

#1.1访问列表,索引
print(list_1[0])
print(list_1[1:3])   #左闭右开
print(list_1[1:])
print(list_1[:3])
print(list_1[-1])    #反向索引
print(list_1[-2:])

#列表方法
list_1.append(13)   #增
print(list_1)
list_1.remove(13)   #删除
print(list_1)
list_1[0]=0    #改
print(list_1)
list_1.reverse()  #翻转
print(list_1)

#拼接
list=[*list_1,*list_2]
print(list)

result=[i**2 for i in list if i %2==0]   #列表推导式
print(result)
print(3 in result)   #判断一个元素是否在列表中


print("-"*20)



#2.元组tuple(不可修改+可重复,有序)
tuple_1=(1,3,7,9,11)
print(tuple_1)
tuple_2=(2,4,6,8,10)
print(tuple_2)
tuple=(*tuple_1,*tuple_2)
print(tuple)
#展示租组包和解包的应用
a =1
b=3
a,b=b,a
print(a,b)
#定义单元素元组,需要在末尾加,
tuple_one=(1,)
print(tuple_one)
print(type(tuple_one))



print("-"*20)



#3.集合(去重加无顺序+可修改)
set_1={1,3,7,9,11}
print(set_1)
set_2={2,4,6,8,10}

print(set_2)
set_3=set_1|set_2
print(set_3)

set_1.add(5)
print(set_1)

print("-"*20)

#4.字典(无顺序+可修改)
dict_1={"name":"张三","age":18}
print(dict_1)
print(dict_1["name"])

# !/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])