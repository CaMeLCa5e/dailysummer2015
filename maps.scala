scala> def f(x: String) = {
	println("taking my time."); sleep(100)
	x.reverse}

f: (x: String)String

val cache = collection.mutable.Map[String, String]()
cache: scala.collection.mutable.Map[String, String] = Map()

def cachedF(s: String) = cache.getOrElseUpdate(s, f(s))
cachedF: (s: String) String
cachedF("abc")
