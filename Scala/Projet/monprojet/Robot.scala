

class Robot extends RobotRegistry{

    def cook(what: String) = cooker.cook(what)
    def getTime() = time.getTime()

}