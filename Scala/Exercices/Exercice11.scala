

object Exercice11 {
  def test(strl: String, strl2: String): Boolean = {
    strl.equalsIgnoreCase(strl2)
  }
  def main(args: Array[String]): Unit = {
    print("Comparison: " + test("Hello World", "HELLO World")+ "\n");
    print("Comparison: " + test("HELLO World", "Bonjour le monde"));
  }
}



