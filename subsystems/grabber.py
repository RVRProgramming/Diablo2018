import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.smartdashboard import SmartDashboard

from common import robotMap


class Grabber(Subsystem):
    
    def __init__(self):
        super().__init__()
        
        # Initialize motors.
        self.leftArmMotor = wpilib.Spark(robotMap.leftArmMotor)
        self.rightArmMotor = wpilib.Spark(robotMap.rightArmMotor)
        self.leftArmEncoder = wpilib.Encoder(0, 1, False, wpilib.Encoder.EncodingType.k1X)
        self.rightArmEncoder = wpilib.Encoder(2, 3, False, wpilib.Encoder.EncodingType.k1X)
        self.leftArmEncoder.reset()
        self.rightArmEncoder.reset()
        
    def grab(self, speed):
        # Set grabbing speed.
        self.leftArmMotor.set(speed)
        self.rightArmMotor.set(-speed)

    def getLeftEncoder(self):
        return self.leftArmEncoder.getDistance()
    
    def getRightEncoder(self):
        return self.rightArmEncoder.getDistance()
    
    def diagnosticsToSmartDash(self):
        SmartDashboard.putNumber("Left Arm Encoder", self.getLeftEncoder())
        SmartDashboard.putNumber("Right Arm Encoder", self.getRightEncoder())

grabber = Grabber()
