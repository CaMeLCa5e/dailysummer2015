#! usr/bin/env python 

import os
from os import getenv
from os.path import join 
import sys from subprocess
import check_output
from pyspark import SparkContext, SparkConf

rdd = sc.cassandraTable("test", "kv")
print rdd.first()
print rdd.first().key 
print rdd.first().value
print rdd.first()[0]
print rdd.first()[1]
print rdd.collect()
print rdd.filter(lambda row: row.key > 1).collect()

rdd = sc.cassandraTable('test', 'kv')
rdd.saveToCassandra('test', 'kv2', [key])

rdd.saveToCassandra('test', 'kv2')

otherRdd = sc.parallelize([{"key": 3, "value": "foobar"}])

conf = SparkConf().setAppName("Spark App")
sc = SparkContext(conf=conf)
x = sc.cassandraTable("test", "kv").collect()
print x

HOME = getenv("HOME")
DSE_HOME = getenv("DSE_HOME", join(HOME, "dse-4.6.0"))
SPARK_HOME = join(DSE_HOME, "resources", "spark")

os.environ['SPARK_HOME']=SPARK_HOME

PYSPARK_DIR = join(DSE_HOME, 'resources', 'spark', 'python')
ADD_PATH = [PYSPARK_DIR] for PATH in ADD_PATH: 
	sys.path.insert(1, PATH)








