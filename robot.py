from commandbased import CommandBasedRobot
import wpilib


class MyRobot(CommandBasedRobot):

    def robotInit(self):
        CommandBasedRobot.robotInit(self)
        
        # Import and initialize commands.
        from commands.teleDrive import TeleDrive
        from commands.teleGrab import TeleGrab
        from commands.teleElevate import TeleElevate
        self.teleDrive = TeleDrive()
        self.teleGrab = TeleGrab()
        self.teleElevate = TeleElevate()

    def teleopInit(self):
        super().teleopInit()
        
        # Start all teleop controls.
        self.teleDrive.start()
        self.teleGrab.start()
        self.teleElevate.start()
        
        
if __name__ == "__main__":
    wpilib.run(MyRobot)
