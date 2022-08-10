

object Exercice4 {
  def test(x: Int): Boolean = 
    {
      (20 <= x && x <= 100) || (20 <= x && x <= 300);
    }     
   def main(args: Array[String]): Unit = {
      println("Result: " + test(10));
      println("Result: " + test(30));
      println("Result: " + test(101));
      println("Result: " + test(300));
      println("Result: " + test(350));
    }
}