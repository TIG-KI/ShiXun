'''
继承
定义：class 类名称(父类类名) ，表示继承了父类，没有明确哪个类
多态：在同一行为作出不同反应；条件：继承
self:指创建对象本身

封装：在类里面声明一些方法来完成一些功能
某个功能会在多出重复使用，此时可将此功能封装起来
'''
class Animal():
    def run(self):
        print("run")
    def go(self,animal):
        animal.run()

class Dog(Animal):
    #方法重写
    def run(self):
        print("dog run")
    pass

class Cat(Animal):

    def run(self):
        print("cat run")
    pass


an = Animal()


#多态的演示
dog1 = Dog()
cat1 = Cat()
an.go(dog1)
an.go(cat1)


