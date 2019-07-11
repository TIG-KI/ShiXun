'''
循环： for  while
写法：
for  x in 序列：
    循环体
x表示：每一次循环都会把序列的值一次赋给x

循环里面常用2个关键字：
 break:终止当前循环（最里面的循环）
 continue:结束本次循环，继续下一次循环

 while:
 写法：
 while 布尔表达式：
    循环体（满足条件执行循环体,不满足条件就跳出循环）

'''
#计算1+2+3+...+100
sum = 0
for x in range(101):
    sum += x
print(sum)
#优化  加到50就不加了
sum = 0
count = 0
for x in range(100000):
    count += 1
    sum += x
    if x==50:
        break
print(sum)
print(count)

#给定一个列表[1,2,3,4,5]，输出1 2 3 5
# list1 = [1,2,3,4,5]
# for x in list1:
#     if x==4:
#         pass
#     else:
#         print(x)
print("****")
list1 = [1,2,3,4,5]
for x in list1:
    if x==4:
        continue
    print(x)
print("--------")
for x in [1,2]:
    print(x)
    for x in [3,4]:
        print(x)
        if x==3:
            break

#while循环  1+2+3+...+100
n = 0
sum = 0
while n<100:
    n += 1
    sum += n
print(sum)

num = 0
while True:
    num += 1
    print(num)
    if num==10:
        break


while True:
   pass
