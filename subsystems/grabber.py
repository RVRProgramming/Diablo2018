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
        
        self.leftArmEncoder = wpilib.Encoder(0, 1, False, wpilib.Encoder.EncodingType.k1X)
        self.rightArmEncoder = wpilib.Encoder(2, 3, False, wpilib.Encoder.EncodingType.k1X)
        
        self.leftArmEncoder.reset()
        self.rightArmEncoder.reset()
              
    def getLeftEncoder(self):
        return self.leftArmEncoder.get()
    
    def getRightEncoder(self):
        return self.rightArmEncoder.get()
    
    def resetEncoders(self):
        self.leftArmEncoder.reset()
        self.rightArmEncoder.reset()
    
    def diagnosticsToSmartDash(self):
        SmartDashboard.putNumber("Left Arm Encoder", self.getLeftEncoder())
        SmartDashboard.putNumber("Right Arm Encoder", self.getRightEncoder())
        SmartDashboard.putNumber("Left Arm Effort", self.leftArmMotor.getSpeed())
        SmartDashboard.putNumber("Right Arm Effort", self.rightArmMotor.getSpeed())
        
    def openSimple(self, speed):
        self.leftArmMotor.set(robotMap.grabberSpeed * speed)
        self.rightArmMotor.set(-robotMap.grabberSpeed * speed)
        
    def openLeft(self, speed):
        self.leftArmMotor.set(speed)
        
    def openRight(self, speed):
        self.rightArmMotor.set(-speed)

grabber = Grabber()
