from string import ascii_lowercase as abc

def check(text):
	return set(text.lower()).issuperset(set(abc))


print 	(check('abc')== False)
print (check('abcdefghijklmnopqrstuvwxyz')== True)
print (check('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == True)
print (check('Quick brown fox jumps over the lazy dog') == True)



