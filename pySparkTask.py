#! usr/bin/env python 

from __future__ import print_function 

try: 
	import cPickle as pickle 
except ImportError: 
	import pickle 
import logging 
import sys 

class PySparkRunner(object): 
	def __init__(self, job, *args):
		with open(job, "rb") as fd: 
			self.job = pickle.load(fd)
		self.args = args 

	def run(self):
		from pyspark import SparkContext, SparkConf
		conf = SparkConf()
		self.job.setup(conf)
		with SparkContext(conf=conf) as sc: 
			self.job.setup_remote(sc)
			self.job.main(sc, *self.args)

if __name__ == '__main__':
	logging.basicConfig(level=logging.WARN)
	PySparkRunner(*sys.argv[1:]).run()
	