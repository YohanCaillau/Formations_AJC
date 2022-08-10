object scala_basic {
    def test(str1: String): String = {
    str1.take(str1.length() - 4) + str1.drop(str1.length() - 4).toUpperCase()
   }
   def main(args: Array[String]): Unit = {
      println("Result: " + test("Scala"));
      println("Result: " + test("Python"));
      println("Result: " + test("abc"));      
    }
  }
