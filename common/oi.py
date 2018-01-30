import wpilib

from common import robotMap


class OI:
    
    def __init__(self):
        self.gamepad = wpilib.Joystick(robotMap.gamepad)
        self.joystick = wpilib.Joystick(robotMap.joystick)
        
    def getLeftDrive(self):
        return self.gamepad.getRawAxis(robotMap.leftDriveStick)
    
    def getRightDrive(self):
        return self.gamepad.getRawAxis(robotMap.rightDriveStick)
    
    def getSlowDrive(self):
        if self.gamepad.getRawButton(robotMap.slowDriveButton):
            return robotMap.slowDriveSpeed * robotMap.maxDriveSpeed
        else:
            return robotMap.maxDriveSpeed

            
oi = OI()
    
