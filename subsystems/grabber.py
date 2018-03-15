import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.smartdashboard import SmartDashboard

from common import robotMap


class Grabber(Subsystem):
    
    def __init__(self):
        super().__init__()
        
        # Initialize motors.
        self.leftArmMotor = wpilib.Spark(robotMap.grabberLeftMotor)
        self.rightArmMotor = wpilib.Spark(robotMap.grabberRightMotor)
        self.PDP = wpilib.PowerDistributionPanel()             

    def diagnosticsToSmartDash(self):
        SmartDashboard.putNumber("Left Grabber Amperage", self.getLeftCurrent())
        SmartDashboard.putNumber("Right Grabber Amperage", self.getRightCurrent())
        
    def grab(self, directionLeft, directionRight):
        self.leftArmMotor.set(-robotMap.grabberSpeed * directionLeft)
        self.rightArmMotor.set(robotMap.grabberSpeed * directionRight)
        
    def getLeftCurrent(self):
        return self.PDP.getCurrent(11)
    
    def getRightCurrent(self):
        return self.PDP.getCurrent(4)
    
grabber = Grabber()
