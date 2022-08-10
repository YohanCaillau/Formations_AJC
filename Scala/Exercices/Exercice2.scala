

object Exercices2 {
  def sumInts(a: Int, b: Int): Int = 
    if (a != b) {a + b }
    else {(a+b)*3}
  
   def main(args: Array[String]): Unit = {
      println("Result: " + sumInts(84,20));
      println("Result: " + sumInts(2,2))
    }
}
