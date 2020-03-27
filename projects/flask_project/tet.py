#coding:utf-8

def a(func):
	def b():
		# print(rule)
		return func
	return b()

@a
def c():
	print('c')

c() # c=a(c())


def a(rule):
	def b(func):
		print(rule)
		return func
	return b

@a('/')
def c():
	print('c')

c()  # c=b(c)=a('/')(c)