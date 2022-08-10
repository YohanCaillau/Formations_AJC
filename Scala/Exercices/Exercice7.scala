

object Exercice7 {
  def test(x: Int, y: Int): Boolean = 
    {
      (x >= 100 && x <= 200) || (y >= 100 && y <= 200);
    }
     
   def main(args: Array[String]): Unit = {
      println("Result: " + test(100, 199));
      println("Result: " + test(250, 300));
      println("Result: " + test(90, 190));
      println("Result: " + test(100, 210));
    }
}
