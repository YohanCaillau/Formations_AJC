

object Exercice12 {
  def test(strl: String): String = {
    strl.toUpperCase()
  }
  def main(args: Array[String]): Unit = {
    print("In uppercase: " + test("Hello World")+ "\n");
    print("In uppercase: " + test("HELLO World"));
  }
}