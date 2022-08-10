

object Exercice8 {
  def test(x: Int, y: Int): Int = {
    val x_abs = Math.abs(x - 100)
    val y_abs = Math.abs(y - 100)
    if (x_abs == y_abs) 0
    else if (x_abs < y_abs) x
    else y
    }
     
   def main(args: Array[String]): Unit = {
      println("Result: " + test(78,95));
      println("Result: " + test(95,95));
      println("Result: " + test(99,70));      
    }
 }
