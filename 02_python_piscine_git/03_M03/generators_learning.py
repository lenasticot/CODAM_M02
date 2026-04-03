import sys

def infinite_sequence():
	num = 0
	while True:
		yield num
		num += 1


def	is_palindrome(num):
	if num // 10 == 0:
		return False
	temp = num
	reversed_num = 0

	while temp != 0:
		reversed_num = (reversed_num * 10) + (temp % 10)
		temp = temp // 10
	if num == reversed_num:
		return num
	else:
		False


def main():
	# for i in infinite_sequence():
	# 	pal = is_palindrome(i)
	# 	if pal:
	# 		print(i)
	num_squared_lc = [num **2 for num in range(10000)]
	num_squared_gc = (num**2 for num in range(10000))
	# print(num_squared_lc)
	print(sys.getsizeof(num_squared_lc))
	# print(num_squared_gc)
	print(sys.getsizeof(num_squared_gc))
