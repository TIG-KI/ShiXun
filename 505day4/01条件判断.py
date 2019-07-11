'''
条件判断：if
定义：当if后面的表达式为true，则进入第一个缩进块，执行代码
为false时，有elif时，执行elif里面缩进块,elif为false，执行另外elif或者else
写法：if 布尔表达式：
        为true代码
     （elif 布尔表达式：
        为true代码
    elif 布尔表达式：
        为true代码
    .
    .
    .    可有可无）
    else:
        为false代码块

执行if时，如果不想做任何操作，用pass占位
if 布尔表达式：
    pass

在python中：空字符串 空列表 空元组 空字典 None等，在布尔表达式中都为False
非空任意类型（除了整数0）,在布尔表达式中都为True
'''
#给定一个学生的年龄，判断该学生是否成年
# age = input("输入一个年龄：")
# age = int(age)
# if age>=18:
#     print("小伙子不错！成年了")
# else:
#     print("未成年人")
#给定一个月份，判断该月份是春夏秋冬哪一季？
#

if 2>1:
    pass

# if []:
#     print("正确")
# else:
#     print("错误")
# if {}:
#     print("正确")
# else:
#     print("错误")

if [1,2]:
    print("正确")
else:
    print("错误")