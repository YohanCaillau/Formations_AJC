

object Exercice6 {
  def test(temp1: Int, temp2: Int): Boolean = 
    {
      (temp1 < 0 && temp2 > 100) || (temp2 < 0 && temp1 > 100)
    }     
   def main(args: Array[String]): Unit = {
      println("Result: " + test(120, -1));
      println("Result: " + test(-1, 120));
      println("Result: " + test(2, 120));
      println("Result: " + test(2, 90))
    }
}