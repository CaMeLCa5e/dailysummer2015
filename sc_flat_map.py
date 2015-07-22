#! usr/bin/python

lines = sc.textFile('data.txt', 1)
debuglines = lines.collect();
print debuglines

words = lines.flatMap(lambda x: x.split(' '))
debugwords = words.collect();
print debugwords

ones = words.map(lambda x: (x, 1))
debugones = ones.collect()
print debugones

counts = ones.reduceByKey(lambda x, y: x + y)
debugcounts = counts.collect()
print debugcounts

counts.saveAsTextFile("output")

nums = [10, 1, 2, 9, 3, 4, 5, 6, 7]
print sc.parallelize(nums).takeOrdered(3)

print sc.parallelize(nums).takeOrdered(3, key=lambda x: -x)

input = [("k1", 1), ("k1", 2), ("k1", 3), ("k1", 4), ("k1", 5),
		 ("k2", 6), ("k2", 7), ("k2", 8), 
		 ("k3", 10), ("k3", 12)]
rdd = sc.parallelize(input)

