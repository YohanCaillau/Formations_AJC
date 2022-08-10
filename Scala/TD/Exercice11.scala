

object Exercice11 {
  def divisible(N: Int): Boolean = {
    if (N.%(3)==0 && N.%(13)==0)
      return true
    else 
      return false
  }
   def main(args: Array[String]): Unit = {
    println("Enter one number: ")
    val N = scala.io.StdIn.readInt()
    if (divisible(N)== true)
      println(N + " is divisible by 3 and 13")
    else
      println(N + " isn't divisible by 3 and 13")
   }
}