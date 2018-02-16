from commandbased import CommandBasedRobot
import wpilib


class MyRobot(CommandBasedRobot):

    # This runs as soon as the robot starts up.
    def robotInit(self):      
        # Import and initialize commands.
        import commands
        self.teleDrive = commands.TeleDrive()
        self.teleGrab = commands.TeleGrab()
        self.teleElevate = commands.TeleElevate()
        self.autoDriveStraightPID = commands.AutoDriveStraightPID(15)
        self.autoDriveStraight = commands.AutoDriveStraight(15)
        self.diagnostics = commands.Diagnostics()

        # Start displaying SmartDash diagnostics.
        self.diagnostics.start()
        
    # This runs in a loop alongside the current mode's periodic function.
    def robotPeriodic(self):
        self.autoRestartCommand(self.diagnostics)
    
    # This runs as soon as robotInit finishes, and every time the bot is disabled after that.
    def disabledInit(self):
        pass
        
    # This runs in a loop while the bot is disabled.
    def disabledPeriodic(self):
        pass
        
    # This runs at the beginning of autonomous.
    def autonomousInit(self):
        pass
        
    # This runs in a loop throughout autonomous.
    def autonomousPeriodic(self):
        pass

    # This runs at the beginning of teleop.
    def teleopInit(self):
        # Start all teleop controls.
        self.teleDrive.start()
        self.teleGrab.start()
        self.teleElevate.start()
        
    # This runs in a loop throughout teleop.
    def teleopPeriodic(self):
        self.autoRestartCommand(self.teleDrive)
        self.autoRestartCommand(self.teleGrab)
        self.autoRestartCommand(self.teleElevate)
    
    # Starts up the command if it isnt already running.
    def autoRestartCommand(self, command):
        if not command.isRunning():
            command.start()


# Proprietary robotpy nonsense.
if __name__ == "__main__":
    wpilib.run(MyRobot)
