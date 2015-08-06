val myOrdering = Ordering.fromLessThan[String](_ > _)
myOrdering: scala.math.Ordering[String]

TreeSet.empty(myOrdering)
scala.collection.immutable.TreeSet[String] = TreeSet()

// empties string
TreeSet.empty[String] 
scala.collection.immutable.TreeSet[String] = TreeSet()

res3 range("one", "two")
scala.collection.immutable.TreeSet[String] = TreeSet(one, three)

def f(x: String) = {
	println("taking my time."); sleep(100)
	x.reverse }

	return f:(x: String)String
