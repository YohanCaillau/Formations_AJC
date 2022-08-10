

object Exercice8 {
  def main(args: Array[String]): Unit = {
    println("Please enter the base")
    val  base = scala.io.StdIn.readInt()
    println("The base is " + base)
    println("Please enter the height")
    val  heigth = scala.io.StdIn.readInt()
    println("The heigth is " + heigth)
    // Calculate
    println("The surface is : "+((base*heigth)/2));
    }
}