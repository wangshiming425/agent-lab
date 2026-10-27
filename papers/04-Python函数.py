# 两数之和演示
def two_sum(num_1: float, num_2: float) -> float:
    """
    两数之和
    :param num_1:
    :param num_2:
    :return:
    """
    return num_1 + num_2

#这里有类型注解的使用,可以标注参数类型和返回值类型,但起不到限制作用



class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #打印时底层调用到的
    def __str__(self) -> str:
        return f"Student(name={self.name}, age={self.age}, gender={self.gender})"


#有默认值的传参,默认值必须在参数列表末尾
def reg_stu(name:str, age:int, gender:set="男"):
    student = Student(name, age, gender)
    print(student)


if __name__ == '__main__':
    print( "两数之和为：" +str(two_sum(1, 2)))
    print("-" * 30)
    reg_stu(name="张三",age=19)

print("-"*30)
def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象

#id()函数可以查看数据的地址
#传入不可变对象
a = 1
print(id(a))
change(a)

print("-"*30)
# 不定长参数

# 可写函数说明
# arg1 是必选参数，vartuple 是可选参数,且以元组的形式传入
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)




print("-"*30)
# 可写函数说明
# arg1 是必选参数，vardict 是可选参数,且以字典的形式传入
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)