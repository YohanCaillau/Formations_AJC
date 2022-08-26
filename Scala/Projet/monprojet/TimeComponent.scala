import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

trait TimeComponent{

    val time: Time
    
    class TimeImpl extends Time{
        val formatter = DateTimeFormatter.ofPattern("HH:mm:ss")
	  override def getTime(): String = s"Le temps est de ${LocalDateTime.now().format(formatter)}"
    }

}