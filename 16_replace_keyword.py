"""
File: replace_keyword.py
----------------------
This file shows how to replace
a keyword by the function called
replace
"""


def main():
	s = replace('Jerry hates coding', 'hates', 'teaches')
	print(s)


def replace(old_s, old_word, new_word):
	"""
	:param old_s:
	:param old_word:
	:new_word:
	:return:
	"""
	if old_word not in old_s:
		print('Go Away!')
	else:
		ans =''
		i = old_s.find(old_word)
		#舊字串中找到old_word(hates)並停在其開頭字母故此時 i=6
		ans += old_s[:i]
		#0-6保留1-5的字母 -> 'Jerry '
		ans += new_word
		#->'Jerry teaches'
		ans +=old_s[i+len(old_word):]
		#'Jerry teaches'+old_s裡頭的[6+5:到結尾]
		return ans


if __name__ == '__main__':
	main()
