import wpilib

from common import robotMap


class OI:
    
    def __init__(self):
        # Initialize the controllers.
        self.gamepad = wpilib.Joystick(robotMap.gamepad)
        self.joystick = wpilib.Joystick(robotMap.joystick)
        
    # Returns the Left Drive speed.
    def getLeftDrive(self):
        return -self.gamepad.getRawAxis(robotMap.leftDriveStick)
    
    # Returns the Right Drive speed.
    def getRightDrive(self):
        return -self.gamepad.getRawAxis(robotMap.rightDriveStick)
    
    # Returns the drive speed modifier.
    def getDriveSpeedModifier(self):
        if self.gamepad.getRawButton(robotMap.slowDriveButton):
            return robotMap.slowDriveSpeed * robotMap.maxTeleopDriveSpeed
        else:
            return robotMap.maxTeleopDriveSpeed

    # Returns whether or not to open the Grabber.
    def getClawOpen(self):
        return self.joystick.getRawButton(robotMap.clawOpen)
    
    # Returns whether or not to close the Grabber.
    def getClawClose(self):
        return self.joystick.getRawButton(robotMap.clawClose)
    
    # Returns the Elevator speed.
    def getElevatorSpeed(self):
        return self.joystick.getRawAxis(robotMap.elevatorStick)
                 
            
oi = OI()
