a = [('k1', 'v1'), ('k2', 'v2')]
b = [('k3', 'v3'), ('k4', 'v4'), ('k5', 'v5')]

rdd1 = sc.parallelize(a)
print rdd1.collect()

rdd2 = sc.parallelize(b)
print rdd2.collect()

rdd3 = rdd.cartesian(rdd2)
print rdd3.collect()
