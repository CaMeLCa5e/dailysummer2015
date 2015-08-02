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