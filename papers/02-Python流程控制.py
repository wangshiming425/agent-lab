# #if - elif - else
# x =int(input("请输入一个整数:"))
# if x > 0:
#     print("x is positive")
# elif x == 0:
#     print("x is zero")
# else:
#     print("x is negative")
#
# #match结构模式匹配
# day = int(input("请输入今天星期几:"))
# match day:
#     case 1:
#         print("星期一")
#     case _:
#         print("不是星期一")
# #while循环
# while day<10:
#     print("hello world!!!")
#     day +=1
#for循环
for i in range(1,10):
    for j in range(1,10):
        if(j>=i):
            print(f"{i}*{j}={i*j}",end="    ")
    print()