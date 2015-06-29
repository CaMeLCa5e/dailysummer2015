v = memoryview('0123456')
print v[1]
print v[0]
print v[-1]
print v[4]
print v[1:4]
print v[1:4].tobytes()
print v[4:5]
print v[4:5].tobytes()