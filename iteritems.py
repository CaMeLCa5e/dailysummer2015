knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems(): 
	print k, v
	print k
	# iteritems vs. enumerate?

# for l, m in knights.enumerate():  can't do it- this is a dict. 
# 	print l, m
# 	print k

words = ['cat', 'window', 'defenstrate']

for w in words[:]: 
	if len(w) > 6: 
		words.insert(0, w)

print words

