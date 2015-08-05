val seq: Seq[Int] = a1 
seq: Seq[Int] = WrapperArray(1, 2, 3)
val a4: Array[Int] = seq.toArray
Array[Int] = Array(1, 2, 3)
a1 eq a4 
res2: Boolean = True 

val seq: Seq[Int] = a1 
seq: Seq[Int] = WrappedArray(1, 2, 3)
seq.reverse 
Seq[Int] = WrappedArray(3, 2, 1)
val ops: collection.mutable.ArrayOps[Int] = a1 
ops: scala.collection.mutable.ArrayOps[Int] = [I(1, 2, 3)]
ops.reverse
Array[Int] = Array(3, 2, 1)

a1.reverse
res4: Array[Int] = Array(3, 2, 1)

intArrayOps(.reverse)
res5: Array[Int] = Array(3, 2, 1)

def evenElems[T: ClassManifest](xs: Vector[T]): Array[T] = {
	val arr = new Array[T]((xs.length + 1) / 2)
	for (i <- 0 until xs.length by 2)
		arr(i / 2) = xs(i)
	arr
}