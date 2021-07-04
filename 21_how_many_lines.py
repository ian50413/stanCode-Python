"""
File: how_many_lines.py
Name: Jerry Liao 2020/05
---------------------------
This file shows how we can calculate
the number of lines in romeojuliet.txt
through Python code
"""

# This constant shows the file path to romeojuliet.txt
FILE = 'text/romeojuliet.txt'


def main():
	"""
	This program will print the number of
	lines in romeojuliet.txt on Console
	"""
	count = 0
	with open(FILE, 'r') as f:
		for line in f:
			count += 1
	print('There are ' + str(count) + ' lines in '+str(FILE))


if __name__ == '__main__':
	main()
