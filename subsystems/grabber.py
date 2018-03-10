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
        
        self.leftArmController = wpilib.PIDController(0.01, 0, 0, self.leftArmEncoder, self.leftArmMotor)
        self.rightArmController = wpilib.PIDController(0.01, 0, 0, self.rightArmEncoder, self.rightArmMotor)
        
        self.leftArmController.setInputRange(robotMap.minAccum, robotMap.maxAccum)
        self.leftArmController.setOutputRange(-robotMap.grabberSpeed, robotMap.grabberSpeed)
        self.rightArmController.setInputRange(robotMap.minAccum, robotMap.maxAccum)
        self.rightArmController.setOutputRange(-robotMap.grabberSpeed, robotMap.grabberSpeed)
        
        self.stopPID()
        
    def grab(self, setpoint):
        # Set grabbing setpoint.
        self.leftArmController.setSetpoint(setpoint)
        self.rightArmController.setSetpoint(setpoint)
        
    def startPID(self):
        self.leftArmController.enable()
        self.rightArmController.enable()
        
    def stopPID(self):
        self.leftArmController.disable()
        self.rightArmController.disable()

    def getLeftEncoder(self):
        return self.leftArmEncoder.get()
    
    def getRightEncoder(self):
        return self.rightArmEncoder.get()
    
    def diagnosticsToSmartDash(self):
        SmartDashboard.putNumber("Left Arm Encoder", self.getLeftEncoder())
        SmartDashboard.putNumber("Right Arm Encoder", self.getRightEncoder())
        SmartDashboard.putNumber("Grabber Setpoint", self.leftArmController.getSetpoint())
        SmartDashboard.putNumber("Left Arm Effort", self.leftArmMotor.getSpeed())
        SmartDashboard.putNumber("Right Arm Effort", self.rightArmMotor.getSpeed())
        
    def openSimple(self, direction):
        self.leftArmMotor.set(robotMap.grabberSpeed * direction)
        self.rightArmMotor.set(-robotMap.grabberSpeed * direction)

grabber = Grabber()
