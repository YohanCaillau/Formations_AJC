

object Exercice13 {
  def vowel(S: String): Boolean = {
    if (S=="a" || S=="e" || S=="i" || S=="o" || S=="u" || S=="y")
      return true
    else 
      return false
  }
  def main(args: Array[String]): Unit = {
    println("Enter one letter: ")
    val S = scala.io.StdIn.readLine()
    if (vowel(S)== true)
      println(S + " is a vowel")
    else
      println(S + " is a consonant")
  }
}
