class SparkConf(object):
	"""docstring for SparkConf"""
	def __init__(self, loadDefaults=True, _jvm=None):
		super(SparkConf, self).__init__()
		self.arg = arg
		from pyspark.context import SparkContext
		SparkContext._ensure_initialized()
		_jvm = _jvm or SparkContext._jvm
		self._jconf = _jvm.SparkConf(loadDefaults)

	def set(self, key, value):
		"""Set config property"""
		self._jconf.set(key, unicode(value))
		return self

	def setMaster(self, value): 
		self._jconf.setMaster(value))
		return self

	def setAppName(self, value): 
		self._jconf.setAppName(value)
		return self

	def setSparkHome(self, value): 
		self._jconf.setSparkHome(value)
		return self

	def setExecutorEnv(self, key=None, value=None, pairs=None):
		if (key != None and pairs != None) or (key == None and pairs == None):
			raise Exception("Pass a pair value")
		elif key != None:
			self._jconf.setExecutorEnv(key, value)
		elif pairs != None: 
			for (k, v) in pairs: 
				self._jconf.setExecutorEnv(k, v)
		return self 

	def setAll(self, pairs):
		for (k, v) in pairs: 
			self._jconf.set(k, v)
		return self

	def get(self, key, defaultValue=None): 
		if defaultValue == None: 
			if not self._jconf.contains(key):
				return None 
			return self._jconf.get(key, defaultValue)

	def contains(self, key): 
		return self._jconf.contains(key)

if __name__ == '__main__':
	test()