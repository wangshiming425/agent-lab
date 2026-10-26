#1.字符串拼接 - 只能拼接两个字符串
str1 = "Hello"
str2 = "World"
str3 = str1 + " " + str2
print(str3)

#2.字符串格式化输出
#2.1占位符
name = "张三"
age = 25

print("我叫%s，今年%d岁" % (name, age))
# 输出：我叫张三，今年25岁
#2.2自动转化加格式化
print(f"{str1}黑黑")

#3.输入与输出
age=int(input("请输入您的年龄:"))
print(f"您今年:{age}岁")

