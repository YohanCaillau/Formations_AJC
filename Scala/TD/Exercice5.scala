

object Exercice5 {
  def main(args: Array[String]): Unit = {
    println("Please enter the base number")
    val  base = scala.io.StdIn.readInt()
    println("The number is " + base)
    println("Please enter the exponent")
    val  exponent = scala.io.StdIn.readInt()
    // Calculate
    println(base+"^"+exponent+" is : "+(math.pow(base, exponent)));
    }
}
