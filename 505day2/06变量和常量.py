'''
python解释过程：从上到下依次执行
变量：
概述：程序可以操作的存储单元的名称
名称：就是按照标识符的规则起名
注意：一定要声明该变量的类型（取决于后面的值），见名知意
程序可以动态的改变变量的值
定义：变量名 = 数据类型
查看变量的类型：type(变量名)
删除变量：del 变量名     删除之后不能再引用

常量：程序执行过程中无法改变的值
注意;python里面没有专门定义常量的规定
一般来说，大写字母变量名看出常量

'''

age = 10
age = 20
#查看变量类型
print(type(age))
num1 = "123"
print(type(num1))
#查看age变量所表示的区域的地址
print(id(age))

#删除变量
#del age
print(age)

number2 = 123
print(id(number2))
number2 = 234
print(id(number2))

_age = 5
print(_age)

print(age)

