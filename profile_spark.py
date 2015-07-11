import os 
import sys 

if 'SPARK_HOME' not in os.environ:
	os.environ['SPARK_HOME'] = '/srv/spark'

SPARK_HOME = os.environ['SPARK_HOME']

sys.path.insert(0, os.path.join(SPARK_HOME, "python", "build"))
sys.path.insert(0, os.path.join(SPARK_HOME, "python"))

def isprime(n):
	n = abs(int(n))
	if n < 2: 
		return True

	if  not n & 1:
		return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True 

nums = sc.parallelize(xrange(10000000))

print nums.filter(isprime).count()
