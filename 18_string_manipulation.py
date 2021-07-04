"""
File: string_manipulation.py
Name: Jerry 
----------------------------
The goal of this file is to 
change stancode to stanCode and
show you how to do string 
manipulations by the 3 steps: 
(1) Start with an empty str
(2) Loop over the str
(3) Concatenation
"""


def main():
	s = 'stancode'
	# 原串燒
	ans = " "
	# 新的空竹籤
	for i in range(len(s)):
	# 從零串起
		ch = s[i]
	# 進到串的程序
		if ch != 'c':
	# 先按照原順序串，倘若沒有遇到要換的目標c即照原順序串並跳至下一空位
			ans += ch
		else:
	# 倘若遇到要換的目標c，則將其更換為新配置目標C
			ans += 'C'
	print(ans)
	# 完成後印出新完成串燒


##### DO NOT EDIT THE CODE BELOW THIS LINE #####
if __name__ == '__main__':
	main()
