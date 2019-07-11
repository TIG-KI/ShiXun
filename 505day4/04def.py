import math
'''
函数：和C语言里面的函数概念一样
调用函数：
    （1）内置函数：内置函数名（）
    （2）库函数：库名.函数名（）
    （3）同目录下其他文件里面调用函数：from 文件名 import 函数名?
定义函数：
def 函数名（参数）：
    函数体
    (return 可有可无）
当没有返回值时，默认返回None
函数参数：
    （1）位置参数：def d(a,b,c):    -->a,b,c都是位置参数
    （2）默认参数：def f(a,b=2):    -->b就是默认参数，一定要放在后面
    （3）可变参数：def d2(*m):      -->m就是可变参数（元组，可以传入无数个参数）
递归函数：自己调用自己的函数
递归头：结束递归
递归体：什么调用自己
作业：现在有50瓶水，3个瓶盖可以换一瓶水，问一个人最多能喝多少瓶水？


'''
#调用函数
abs(-15)
math.ceil(2.2)
#定义函数
def add(a,b):
    return a+b
print(add(2,3))


def m():
    pass
print(m())

def n():
    print(111)
print(n())


def y(a,b=2):
    print(a)
    print(b)
print(y(3))

def person(name,address="成都"):
    print("%s:%s" %(name,address))
person("张三")
person("李四","北京")
# person()

def listDef(list):
    if isinstance(list,type([1,2])): #isinstance(x,(a,b,c...)) 判断x是否abc..类型其中一种
        for x in list:
            print(x, end=" ")
    else:
        raise ValueError("类型错误")


listDef([1,2,3])
# listDef(2)

print(isinstance(2,int))
print(isinstance(2.2,(int,float)))

#定义一个含可变参数的函数（可变参数其实就是元组）
def d2(*m):
    print(m)
    print(type(m))
    for x in m:
        print(x)
d2([1,2,3],"你好")

def m3(a=[]):
    a.append("end")
    return a
print(m3(["one","two"]))
print(m3(["1","2"]))

print(m3())
print(m3())
print("------")
def m4(a=None):
    if a is None:
        a=[]
    else:
        a.append("end")
    return a
print(m4())
print(m4())

#计算任意值得阶乘，用递归
def diDef(n):
    if n==1:
        return n
    else:
        return n*diDef(n-1)
'''
n=4 return 4*diDef(3)-->4*3*diDef(2)-->4*3*2*diDef(1)-->4*3*2*1

'''

print(diDef(4))
