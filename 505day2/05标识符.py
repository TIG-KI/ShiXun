'''
标识符：
概述：就是一个字符串（字符串并不一定是标识符）
规定：组成部分：数字+字母+下划线组成的字符串，只能以字母或者下划线开头
作用：给变量，函数等起名称
约束条件：标识符不能是关键字（在python里面有特殊含义的英文）
注意：见名知意  驼峰命名（例：bigAge smallAge）

怎么查看关键字？
import keyword
#打印关键字
print(keyword.kwlist)
具体有：如下
['False', 'None', 'True', 'and', 'as', 'assert',
 'async', 'await', 'break', 'class', 'continue', 'def',
 'del', 'elif', 'else', 'except', 'finally', 'for',
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
  'while', 'with', 'yield']
什么是保留字？-->有些英文还没有成为关键字，但是呢，python更新版本可能会变成关键字的英文

'''