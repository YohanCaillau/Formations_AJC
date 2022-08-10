

object Exercice10 {
  def Max(N1: Int, N2: Int, N3: Int): Int = {
    if (N2 > N1)
      if (N2 > N3)
        return N2
      else
        return N3
   else 
     if (N1 > N3)
       return N1
     else 
       return N3
  }
  def main(args: Array[String]): Unit = {
    println("Enter 3 values: ")
    val N1, N2, N3 = scala.io.StdIn.readInt()
    println("The maximum is: " + Max(N1,N2,N3))
  }
}