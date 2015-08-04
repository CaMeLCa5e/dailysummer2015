import collection.mutable.{HashMap, ArrayBuffer}
val buf = ArrayBuffer(1, 2, 3)
buf: scala.collection.mutable.ArrayBuffer[Int] = 
ArrayBuffer(1, 2, 3)
val map = HashMap(buf -> 3)
map: scala.collection.mutable.HashMap[scala.collection.
mutable.ArrayBuffer[Int], Int] = Map((ArrayBuffer(1, 2, 3),3))
map(buf)
res13: Int = 3
buf(0) += 1
map(buf)
ArrayBuffer(2, 3, 3)

