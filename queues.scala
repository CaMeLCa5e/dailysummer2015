val queue = new scala.collection.mutable.Queue[String]
scala.collection.mutable.Queue[String] = Queue()
queue.type = Queue(a)
queue ++= List("b", "c")
queue.type = Queue(a, b, c)
scala.collection.mutable.Queue[String] = Queue(a, b, c)
queue.dequeue
String = a 
queue 
scala.collection.mutable.Queue[String] = Queue(b, c)


def cachedF(arg: String) = cache get arg match {
	case Some(result) => result
	case None =>
		val result = f(x)
		cache(arg) = result
		result
}