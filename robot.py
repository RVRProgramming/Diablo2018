from commandbased import CommandBasedRobot
import wpilib

class MyRobot(CommandBasedRobot):

    # This runs as soon as the robot starts up.
    def robotInit(self):      
        super().robotInit()
        # Import and initialize commands.
        import commands
        self.teleDrive = commands.TeleDrive()
        self.teleElevate = commands.TeleElevate()
        self.autoDriveStraightPID = commands.AutoDriveStraightPID(5.5)
        self.diagnostics = commands.Diagnostics()
        self.disaDisableTalons = commands.DisaDisableTalons()

        # Start displaying SmartDash diagnostics.
        self.diagnostics.start()
        
    # This runs in a loop alongside the current mode's periodic function.
    def robotPeriodic(self):
        super().robotPeriodic()
    
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
        self.teleElevate.start()
        
    # This runs in a loop throughout teleop.
    def teleopPeriodic(self):
        super().teleopPeriodic()

# Proprietary robotpy nonsense.
if __name__ == "__main__":
    wpilib.run(MyRobot)
