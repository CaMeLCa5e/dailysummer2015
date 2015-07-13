text_file = spark.textFile("hdfs://...")
counts = text_file.flatMap(lambda line: line.split(" ")) \
			.map(lambda word: (word, 1)) \
			.reduceByKey(lambda a b: a + b)
counts.saveAsTextFile("hdfs://...")

def sample(p):
	x, y = random(), random()
	return 1 if x*x + y*y < 1 else 0

count = spark.paralleliz(xrange(0, NUM_SAMPLES)).map(sample) \
			 .reduce(lambda a, b: a +b)
print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)

points = spark.textFile(...).map(parsePoint).cache()
w = numpy.random.ranf(size = D)
for i in range(ITERATIONS): 
	gradient = points.map(
		lambda p: (1/ (1 + exp(-p.y*(w.dot(p..x))))-1) * p.y * p.x 
		).reduce(lambda a, b: a + b)
	w -= gradient
print "Final separating plane: %s" % w