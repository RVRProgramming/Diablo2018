import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.smartdashboard import SmartDashboard

from common import robotMap


class Grabber(Subsystem):
    
    def __init__(self):
        super().__init__()
        
        # Initialize motors and PDP.
        self.leftArmMotor = wpilib.Spark(robotMap.grabberLeftMotor)
        self.rightArmMotor = wpilib.Spark(robotMap.grabberRightMotor)
        self.PDP = wpilib.PowerDistributionPanel()             

    def diagnosticsToSmartDash(self):
        # SmartDashboard.putNumber("Left Grabber Amperage", self.getLeftCurrent())
        # SmartDashboard.putNumber("Right Grabber Amperage", self.getRightCurrent())
        pass
    
    def grab(self, speedLeft, speedRight):
        self.leftArmMotor.set(-robotMap.grabberSpeed * speedLeft)
        self.rightArmMotor.set(robotMap.grabberSpeed * speedRight)
        
    def getLeftCurrent(self):
        return self.PDP.getCurrent(11)
    
    def getRightCurrent(self):
        return self.PDP.getCurrent(4)

    
grabber = Grabber()
