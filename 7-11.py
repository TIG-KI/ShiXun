'''
约瑟夫
'''
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 12:04:57 2018
Description:约瑟夫问题的列表实现，基于python
Version:1.0    
@author: HJY
"""
#控制参数：
nums = 41
call = 3
#参数定义：
peoples = [True for _ in range(nums)]

#append的方法性能不好
#for _ in range(nums):
#    peoples.append(True)

result = []
num = 1

while(any(peoples)):
    for index, people in enumerate(peoples):
        if people:
            if num == call:
                peoples[index] = False
                result.append(index+1)
#                print(index+1)#每轮的出局者
#                print(peoples)#每次的队列状态
                num = 1
            else:
                num += 1

print('-' * 25)
print('\n总数为%d,报数为%d' % (nums, call))
print('约瑟夫序列为：\n%s\n' % result)
print('-' * 25)



