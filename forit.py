words = ['cat', 'window', 'greggory']
for w in words: 
	print w, len (w)

for w in words [:]:
	if len(w) > 6:
		words.insert(0, w)
print words

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print i, a[i]