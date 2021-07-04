"""
File: nested_for_loop.py
Name: Ian Chen
------------------------
This program show students the basic
concepts of nested (double) for loop
by printing a 4 rows 3 cols rectangle
"""

# These constants control the diameter of the rectangle
ROW = 4
COL = 3
# 外圈慢變，內圈快變

def main():
	for i in range(ROW):
		for j in range(COL):
			print('#',end="")
		print("")


####  DO NOT EDIT CODE BELOW THIS LINE  ####
if __name__ == '__main__':
	main()
	