def mtest(str):
	if str == 'Hello':
		raise NameError('无效输入')
	if str.isdigit():
		raise TypeError('数据类型错误')


try:
	mtest('1')
	#mtest('Hello')
except NameError as e:
	print(e)
except TypeError as e:
	print(e)
else:
	print('Done')
