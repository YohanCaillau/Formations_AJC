object scala_basic {
  def test(str1: String): String = 
    {
    val len = str1.length
    if (len <= 1) str1
    else str1.charAt(len - 1) + str1.substring(1, len - 1) + str1.charAt(0)
    }   
   def main(args: Array[String]): Unit = {
      println("Result: " + test("Scala"));
      println("Result: " + test("abcd"));
      println("Result: " + test("ab"));
      println("Result: " + test("a"));
    }
}