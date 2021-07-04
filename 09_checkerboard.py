"""
File: checkerboard.py
Name:
------------------------
This program prints an alternating 
checkerboard pattern on Console
by using nested for loop.
"""

# These constants control the diameter of the checkerboard
ROW = 5
COL = 8


def main():
	for i in range(ROW):
		for j in range(COL):
			if (i+j)%2==0:
				print('A',end="")
			else:
				print('#',end="")
		print("")




####  DO NOT EDIT CODE BELOW THIS LINE  ####
if __name__ == '__main__':
	main()