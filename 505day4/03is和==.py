#导入同目录的文件里面定义的函数

'''
is:判断两个对象是否相等（相等包括内容相同，地址也相同）
==：判断内容是否相等
'''
list1 = [1,2,3]
print(id(list1))
list2 = [1,2,3]
print(id(list2))
print(list1 is list2)
print(list1==list2)

print(False is None)
#None既不是0，也不是False，其实就是空对象，并且是不可变对象

a1 = -6
a2 = -6
print(a1 is a2)


'''
因为python也有缓冲区的概念，将[-5,256]区间的整数放在缓冲区，但是想要看到
效果，必须到cmd窗口编写python代码。因为其他编译（pycharm）器会这个进行了优化，所有
看不到想要效果（或者保存文件在cmd里面执行也是一样）
'''

