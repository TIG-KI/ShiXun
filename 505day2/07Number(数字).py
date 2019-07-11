'''
整型：可以任意整型的数，写法和数学一模一样

'''
import math
import random
#import 导入库
#库：封装了一些功能
num1 = 25
num2 = 50
num3 = 1000000000000

print(type(num1))
print(type(num3))
print(num1+num2)

'''
浮点型（小数）
'''
num4 = 1.1
print(type(num4))
num5 = 1.2

num6 = 2.1
num7 = 1.0
print(num4+num5)
print(num6-num7)

'''
复数：包括实数部分和虚数部分 i+mj  i和m都是浮点数
'''
#声明一个复数
m1 = 1 + 2j
print(m1)
#怎么查看复数的实数部分
print(m1.real)
#怎么查看复数的虚数部分
print(m1.imag)
#怎么得到复数的共轭复数
print(m1.conjugate())

'''
类型转换
'''
#浮点型转换成整型
n1 = int(2.999999999999999999)
print(n1)
#字符串转换成整型(全是数字才能转，而且不能有特殊符号)
n2 = int("123")
#n3 = int("ahsdaojdsa")
#n4 = int("123 564 678")
#+或者-只能作为正负号的时候才能转
n5 = int("+100")
n6 = int("-100")
print(n6)
#整型或者字符串转换成浮点型
n7 = float(1000000000000000000) #1e+18 1*10^18
n8 = float("2")
print(n8)

'''
常见的一些数学函数
'''
#abs(n) 获取n的绝对值
y1 = -100
print(abs(y1))
#print(abs("-123"))
print(abs(-12.2))

#round(number[,n]) 四舍五入  当n不存在时，默认为0，当n存在时，表示的保留小数点后n位
y2 = 4.554
print(round(y2))
print(round(y2,1))
print(round(y2,2))

#pow(x,y) 结果是x的y次方  **次方符号
#计算2的3次方
print(pow(2,3))
print(2**3)

'''
math库
'''
#ceil表示向上去取整
print(math.ceil(5.2))
print(math.ceil(5.6))
#floor向下取整
print(math.floor(5.2))
print(math.floor(5.6))
#sqrt开平方，结果正数，浮点数
print(math.sqrt(16))

'''
radom库
'''
list = [1,2,4,6]
print(list)
#从列表里面随机取一个数
print(random.choice([1,2,4,6]))
print(random.choice(range(5))) #range(5) [0,1,2,3,4]

#随机生成UI个1~100任意整数
print(random.choice(range(100))+1)

print(random.choice("good")) #"good"-->['g','o','o','d']


