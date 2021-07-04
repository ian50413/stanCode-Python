"""
File: file_reading.py
Name:Ian Chen
---------------------------
This file shows how we can open and
print text files through Python code
"""


def main():
	filename = 'text/JerrySecret5.txt'
	with open(filename,'r') as f:
		for line in f:
			print(line)


if __name__ == '__main__':
	main()
