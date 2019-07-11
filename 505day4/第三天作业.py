import  math
'''
1.输出1~100内前5个可以被3整除的数
'''

count = 0 #记录个数
for x in range(1,101):
    if x%3==0 and count<5:
        print(x)
        count += 1
    # if count==5:
    #     break
'''
2.while打印九九乘法表
'''
i = 1 #外层循环的变量
j = 1 #内存循环的变量
while i<=9:
    while j<=i:
       print(str(j) +" * "+str(i)+" ="+str(i*j),end=" ")
       j += 1
    print()
    i += 1
    j = 1
'''
3.打印出所有的 "水仙花数 "，所谓 "水仙花数 "是指一个三位数，
其各位数字立方和等于该数本身。*例如：153是一个 "水仙花数 "，
因为153=1的三次方＋5的三次方＋3的
三次方。
'''
a = b = c = 0 # a个位 b十位 c百位
for x in range(100,1000):
    a = x%10
    b = x%100//10
    c = x//100
    if a**3+b**3+c**3==x:
        print(x)
print("---------")
'''
4.输出101~200内的质数
'''
for x in range(101,201):
    m = True #确定到底是否质数
    for y in range(2,math.ceil(x/2)+1):
        if x%y==0:
            m = False
    if m:
        print(x,end=" ")
'''
5.用循环计算1！+2！+3！+...+10!
'''
num = 1
sum = 0
for x in range(1,11):
    # for y in range(1,x+1):
    num *= x
    sum += num
print(sum)
'''
6.100元怎么买100个蛋，鸡蛋1毛一个，鸭蛋3元一个，鹅蛋6元一个
'''
a = b = c = 0 #a鸡蛋 b鸭蛋 c鹅蛋
while a<=100:
    a += 1
    while b<=100:
        b += 1
        c = 100 - a - b
        if (a*0.1+b*3+c*6)==100 and c>=0:
            print("鸡蛋 %d 鸭蛋 %d 鹅蛋 %d" % (a,b,c))
    b = 0
