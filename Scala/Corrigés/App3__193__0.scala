object scala_basic {
  def test(x:Int, y:Int) : Boolean  =
    {
     x == 30 || y == 30 || x + y == 30
    }
     
   def main(args: Array[String]): Unit = {
      println("Result: " + test(30, 0));
      println("Result: " + test(25, 5));
      println("Result: " + test(30, 20));
      println("Result: " + test(25, 20));
   }
}
