

object Exercice6 {
  def main(args: Array[String]): Unit = {
    println("Please enter the base number")
    val  base = scala.io.StdIn.readInt()
    println("The number is " + base)
    // Calculate
    println("The square root of " + base + " is : "+ math.sqrt(base));
    }
}