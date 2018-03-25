from commandbased import CommandBasedRobot
import wpilib

class MyRobot(CommandBasedRobot):

    # This runs as soon as the robot starts up.
    def robotInit(self):      
        super().robotInit()
        # Import and initialize commands.
        import commands
        self.teleDrive = commands.TeleDrive()
        #self.teleGrab = commands.TeleGrab()
        self.teleElevate = commands.TeleElevate()
        self.autoDriveStraightPID = commands.AutoDriveStraightPID(5.5)
        self.diagnostics = commands.Diagnostics()
        self.disaDisableTalons = commands.DisaDisableTalons()
        #self.groupDriveStraight = commands.GroupDriveStraight()
        self.autoNoGroup = commands.AutoDriveStraightNoGroup()
        self.teleClaw = commands.TeleClaw()

        # Start displaying SmartDash diagnostics.
        self.diagnostics.start()
        
    # This runs in a loop alongside the current mode's periodic function.
    def robotPeriodic(self):
        super().robotPeriodic()
        self.autoRestartCommand(self.diagnostics)
    
    # This runs as soon as robotInit finishes, and every time the bot is disabled after that.
    def disabledInit(self):
        super().disabledInit()
        self.disaDisableTalons.start()
        
    # This runs in a loop while the bot is disabled.
    def disabledPeriodic(self):
        super().commandPeriodic()
        
    # This runs at the beginning of autonomous.
    def autonomousInit(self):
        super().autonomousInit()
        self.autoDriveStraightPID.start()
        
    # This runs in a loop throughout autonomous.
    def autonomousPeriodic(self):
        super().autonomousPeriodic()

    # This runs at the beginning of teleop.
    def teleopInit(self):
        super().teleopInit()
        # Start all teleop controls.
        self.teleDrive.start()
        self.teleClaw.start()
        self.teleElevate.start()
        
    # This runs in a loop throughout teleop.
    def teleopPeriodic(self):
        super().teleopPeriodic()
        self.autoRestartCommand(self.teleDrive)
        self.autoRestartCommand(self.teleElevate)
        self.autoRestartCommand(self.teleClaw)
    
    # Starts up the command if it isn't already running.
    def autoRestartCommand(self, command):
        if not command.isRunning():
            command.start()

# Proprietary robotpy nonsense.
if __name__ == "__main__":
    wpilib.run(MyRobot)
