import wpilib
from commandbased import CommandBasedRobot

class MyRobot(CommandBasedRobot):
    def robotInit(self):
        CommandBasedRobot.robotInit(self)
        from commands.teleDrive import TeleDrive
        self.teleDrive = TeleDrive()
    
    def teleopInit(self):
        super().teleopInit()
        self.teleDrive.start()

if __name__ == "__main__":
    wpilib.run(MyRobot)
