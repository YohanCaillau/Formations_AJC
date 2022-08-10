

object Exercice12 {
  def even(N: Int): Boolean = {
    if (N%(2) == 0)
      return true
    else 
      return false
  }
  def main(args: Array[String]): Unit = {
    println("Enter one number: ")
    val N = scala.io.StdIn.readInt()
    if (even(N)== true)
      println(N + " is an even number")
    else
      println(N + " is an odd number")
  }
}