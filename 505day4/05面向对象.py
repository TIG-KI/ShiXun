'''
面向对象：将要解决的问题抽象成各个对象，各个对象再去完成各个功能，最后
结合起来就可以解决问题
类：有相似特征一类事物称为类（电脑，学生，老师，学校...）
对象：以类为模板（具体到某一个学生，某一个老师就是对象）
声明类：class 类名():    类名的首字母大写
声明对象：变量名 = 类名（）  声明了该类的对象
给对象添加属性：
    (1)对象引用.属性名= 属性值
    (2)通过重写父类（Object）_init_函数来添加属性
访问权限：给属性名前加一个下划线  _属性名

'''
# class Stu():
#     pass
#
# stu1 = Stu()
# print(stu1)
# print(type(stu1))
# print(Stu)

class Tea():
    pass
tea1 = Tea()
tea1.name="张三"
tea1.age= 18
print(tea1.name)
print(tea1.age)

class Sch():
    '''
    __init__方法就类似于java的构造函数
    '''
    def __init__(self,name,age): #self对象引用，指向了初始化的对象
        self.name = name #self.name指的是初始化对象的name属性
        self.age = age

sch1 = Sch("北京大学",100)
print(sch1.age)
print(sch1.name)

#测试访问权限
class Dog():
    def __init__(self,name,dogAge):
        self._name = name #  _属性名：给属性设置权限，外部不能访问
        self._dogAge = dogAge
    def set_name(self,name):
        self._name = name

    def get_name(self):
        return  self._name


dog1 = Dog("二哈",3)
print(dog1.get_name())
dog1.set_name("三哈")
print(dog1.get_name())
#print(dog1._Dog_age)


