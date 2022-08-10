

object Exercice4 {
  def main(args: Array[String]): Unit = {
    println("Please enter the number of days")
    val  days = scala.io.StdIn.readInt()
    println("The number of day is " + days)
    // Converting centimeter into year and weeks
    val year =  days / 365.0;
    val week = days / 7;
     
    println("Days in weak = " + week.toInt + " weeks");
    println("Days in year = " + year.toInt + " year");
    }
}