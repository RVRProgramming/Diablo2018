
from ctre._impl import StatusFrameEnhanced
from wpilib.command.command import Command

from common import robotMap
from subsystems.driveBase import driveBase


class AutoMotionProfiling(Command):
    
    def __init__(self, profile):
        super().__init__()
        self.profile = profile
        
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
        
        driveBase.l1.configNeutralDeadband(robotMap.mpDeadband, robotMap.ctreTimeout)
        driveBase.r1.configNeutralDeadband(robotMap.mpDeadband, robotMap.ctreTimeout)
        
        driveBase.l1.configMotionProfileTrajectoryPeriod(robotMap.mpPeriod, robotMap.ctreTimeout)
        driveBase.r1.configMotionProfileTrajectoryPeriod(robotMap.mpPeriod, robotMap.ctreTimeout)
        
        driveBase.l1.setStatusFramePeriod(StatusFrameEnhanced.Status_10_MotionMagic, robotMap.mpPeriod, robotMap.ctreTimeout)
        
    def execute(self):
        pass
            
    def isFinished(self):
        return False
    
    def end(self):
        super().end()
        driveBase.drive(0, 0)

