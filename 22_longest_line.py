"""
File: longest_line.py
Name:
---------------------------
This file shows how we can find
the longest line in romeojuliet.txt
through Python code
"""

# This constant shows the file path to romeojuliet.txt
FILE = 'text/romeojuliet.txt'


def main():
	longest_line=''
	longest_count = 0
	with open(FILE, 'r') as f:
		for line in f:
			if len(line) > longest_count:
				longest_line = line
				longest_count = len(line)
		print(longest_line)


if __name__ == '__main__':
	main()
