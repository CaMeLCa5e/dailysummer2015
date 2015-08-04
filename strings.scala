val str = "hello"
str: java.lang.String = hello
str.reverse 
res6: String = olleh 
str.map(_.toUpper)
res7: String = HELLO 
str drop 3 
res8: String = lo 
str slice(1, 4)
String = ell 
val s: Seq[Char] = str
Seq[Char] = WrappedString(h, e, l, l, o)

val a1 = Array(1, 2, 3)
a1: Array[Int] = Array(1, 2, 3)
val a2 = a1 map(_ * 3)
Array[Int] = Array(3, 6, 9)
val a3 = a2 filter(_ %2 != 0)
Array[Int] = Array(3, 9)
a3.reverse
res1: Array[Int] = Array(9, 3)
