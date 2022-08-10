
object Exercice9 {
  def main(args: Array[String]): Unit = {
    println("Please enter the grades")
    val arr = new Array[Int](5)
    println("the values of array is ")
    for (i <- 0 to 4) {
      arr(i) = scala.io.StdIn.readInt()
    }
    println("The sum is : " +arr.sum)
    println("The mean is : " +arr.sum/arr.length) 
    println("The percentage is : " + ((arr.sum/arr.length)/100))
  }
}