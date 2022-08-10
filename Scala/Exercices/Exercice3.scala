

object Exercice3 {
  def test(x: Int, y: Int): Boolean = 
    {
      (x == 30 || y == 30) || (x+y == 30)
    }     
   def main(args: Array[String]): Unit = {
      println("Result: " + test(20, 84));
      println("Result: " + test(30, 30));
      println("Result: " + test(30, 84));
      println("Result: " + test(15, 15))
    }
}
