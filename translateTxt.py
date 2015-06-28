print 'read this short text'.translate(None, 'aeiou')

x = '111'
print x.zfill(60)
print len(x)

class Counter(dict):
	def __missing__(self, key):
		return 0 
c = Counter()
print c['red']

c['red'] += 1
print c['red']
