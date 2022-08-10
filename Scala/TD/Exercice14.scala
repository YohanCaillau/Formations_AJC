

object Exercice14 {
  def day(N: Int): String = {
    if (N == 1)
      return "Monday"
    else if (N == 2)
      return "Tuesday"
    else if (N == 3)
      return "Wednesday"
    else if (N == 4)
      return "Thursday"
    else if (N == 5)
      return "Friday"
    else if (N == 6)
      return "Saturday"
    else
      return "Sunday"
 }
  def main(args: Array[String]): Unit = {
    println("Enter one number between 1 and 7: ")
    val N = scala.io.StdIn.readInt()
      println("The day of the weak is : " + day(N))
   }
}