object HelloWorld{
	def main(args: Array[String]) {
		println "Test text" //print statement
	}
}

package scala 
final case class Symbol private (name: String) {
	override def toString: String = "'" + name
}

var myVar : String = "Foo"

class Outer {
	class Inner {
		private def f() {println("f") }
		class InnerMost {
			f() //OK
		}
	}
	(new Inner).f() //
}