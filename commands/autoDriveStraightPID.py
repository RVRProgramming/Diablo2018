
from wpilib.command.command import Command

from common import robotMap
from subsystems.driveBase import driveBase


class AutoDriveStraightPID(Command):
    
    def __init__(self, distance):
        super().__init__()
        self.distance = distance * robotMap.countsPerRevolution
        
    def initialize(self):
        super().initialize()
        driveBase.resetEncoderPosition()
        
        # Set PID Constants and Settings.
        driveBase.l1.selectProfileSlot(robotMap.PIDSlot, 0)
        driveBase.l1.config_kF(robotMap.PIDSlot, 0, robotMap.ctreTimeout)
        driveBase.l1.config_kP(robotMap.PIDSlot, 0.008, robotMap.ctreTimeout)
        driveBase.l1.config_kD(robotMap.PIDSlot, 0, robotMap.ctreTimeout)
        driveBase.l1.config_kI(robotMap.PIDSlot, 0, robotMap.ctreTimeout)
        
        driveBase.r1.selectProfileSlot(robotMap.PIDSlot, 0)
        driveBase.r1.config_kF(robotMap.PIDSlot, 0, robotMap.ctreTimeout)
        driveBase.r1.config_kP(robotMap.PIDSlot, 0.008, robotMap.ctreTimeout)
        driveBase.r1.config_kD(robotMap.PIDSlot, 0, robotMap.ctreTimeout)
        driveBase.r1.config_kI(robotMap.PIDSlot, 0, robotMap.ctreTimeout)
    
        driveBase.l1.configNominalOutputForward(robotMap.minEffort, robotMap.ctreTimeout)
        driveBase.l1.configNominalOutputReverse(-robotMap.minEffort, robotMap.ctreTimeout)
        driveBase.l1.configPeakOutputForward(robotMap.maxEffort, robotMap.ctreTimeout)
        driveBase.l1.configPeakOutputReverse(-robotMap.maxEffort, robotMap.ctreTimeout)
        
        driveBase.r1.configNominalOutputForward(robotMap.minEffort, robotMap.ctreTimeout)
        driveBase.r1.configNominalOutputReverse(-robotMap.minEffort, robotMap.ctreTimeout)
        driveBase.r1.configPeakOutputForward(robotMap.maxEffort, robotMap.ctreTimeout)
        driveBase.r1.configPeakOutputReverse(-robotMap.maxEffort, robotMap.ctreTimeout)
        
        driveBase.l1.configAllowableClosedloopError(robotMap.PIDSlot, robotMap.allowableError, robotMap.ctreTimeout)
        driveBase.r1.configAllowableClosedloopError(robotMap.PIDSlot, robotMap.allowableError, robotMap.ctreTimeout)
        
    def execute(self):
        driveBase.positionPID(self.distance)
            
    def isFinished(self):
        # Return True if the velocity of both sides is less than 1 RPM and error is less than 250.
        # This very possibly is broken. If it isnt, thats great!
        if not driveBase.getLeftError() == None and not driveBase.getRightError() == None:
            return True if abs((driveBase.getLeftVelocity() * 10) / robotMap.countsPerRevolution) * 60 < 1 and abs((driveBase.getRightVelocity() * 10) / robotMap.countsPerRevolution) * 60 < 1 and abs(driveBase.getLeftError()) < robotMap.allowableError and abs(driveBase.getRightError()) < robotMap.allowableError else False
        else:
            return False
    
    def end(self):
        super().end()
        driveBase.drive(0, 0)

