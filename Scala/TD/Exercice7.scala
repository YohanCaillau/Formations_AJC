

object Exercice7 {
  def main(args: Array[String]): Unit = {
    println("Please enter the first angle")
    val  angle1 = scala.io.StdIn.readInt()
    println("The angle is " + angle1)
    println("Please enter the second angle")
    val  angle2 = scala.io.StdIn.readInt()
    println("The angle is " + angle2)
    // Calculate
    println("The third angle is : "+(180-(angle1+angle2)));
    }
}