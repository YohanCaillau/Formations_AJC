

object Exercice3 {
  def main(args: Array[String]): Unit = {
    println("Please enter the centimeter")
    val  cm = scala.io.StdIn.readInt()
    println("The value of length is " + cm + "cm")
    // Converting centimeter into meter and kilometer
    val meter = cm / 100.0;
    val kilometer = cm / 100000.0;
     
    println("Length in meter = " + meter + "m");
    println("Length in Kilometer = " + kilometer + "km");
    }
}
 
