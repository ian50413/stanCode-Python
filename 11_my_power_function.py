"""
File: my_power_function.py
Name:
-------------------------------
This program shows students how to 
make their own functions my defining
def my_power(a, b)
"""


def main():
	print('This program prints a to the power of b.')
	a = int(input('a: '))
	b = int(input('b: '))
	print(my_power(a, b))


def my_power(a, b):
	"""
	:param a: int,a>0
	:param b: int,b>=0
	:return: int,a^b
	"""
	ans = 1
	# 上述為考量若b=0時所有數之值皆為1
	# 可透過Lec4上課教到的if,elif 切割邏輯
	for i in range(b):
		# ans = 1(放這為上課時理解性測試實驗)
		ans*=a
	# ans=ans*a
	return ans



if __name__ == '__main__':
	main()