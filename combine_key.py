input = [("k1", 1), ("k1", 2), ("k1", 3), ("k1", 4), ("k1", 5),
		 ("k2", 6), ("k2", 7), ("k2", 8), 
		 ("k3", 10), ("k3", 12)]

rdd = sc.parallelize(input)
sumCount = rdd.combineByKey(
							(lambda x: (x, 1)),
							(lambda x, y: (x[0] + y, x[1] + 1)),
							(lambda x, y: (x[0] + y,[0], x[1] + y[1]))
							)
print sumCount.collect()

avg = sumCount.mapValues(lambda v: v[0] / v[1])
print avg.collect()
