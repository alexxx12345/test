#Copyright unknwn 2016
from string import ascii_lowercase as abc

def check(text):
	return set(text.lower()).issuperset(set(abc))


print 	check('abc')


