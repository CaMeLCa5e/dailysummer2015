def foreach[U](f: Elem => U): Unit = {
	val it = iterator
	while (it.hasNext) f(it.next())
}

scala> val xs = List(1, 2, 3, 4, 5)
xs: List[Int] = List(1, 2, 3, 4, 5)
scala> val git = xs grouped 3
git: Iterator[List[Int]] = non-empty iterator
scala> git.next()
res3: List[Int] = List(1, 2, 3)
scala> sit.next()
res4: List[Int] = (4, 5)
scala> sit.next()
res5: List[Int] = (1, 2, 3)
scala> sit.next()
res5: List[Int] = (2, 3, 4)
scala> sit.next()
res5: List[Int] = (3, 4, 5)

scala> val fruit = Set("apple", "orange", "peach", "bananna")
fruit: scala.collection.immutable.Set[java.lang.String] = Set(apple,
	orange, peach, bananna)
scala> fruit("peach")
res0: Boolean = true
scala> fruit("potato")
res1: Boolean = false

scala> var s = Set(1, 2, 3)
s: scala.collection.immutable.Set[Int] = Set(1, 2, 3)
scala> s += 4
scala> s -= 2
scala> s 
res2: scala.collection.immutable.Set[Int] = Set(1, 3, 4)

