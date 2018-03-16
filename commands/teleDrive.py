from wpilib.command.command import Command

from common import robotMap
from common.oi import oi
from subsystems.driveBase import driveBase


class TeleDrive(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the DriveBase while running.
        self.requires(driveBase)
    
    def initialize(self):
        super().initialize()
        driveBase.resetEncoderPosition()
        
        driveBase.l1.configNominalOutputForward(0, robotMap.ctreTimeout)
        driveBase.l1.configNominalOutputReverse(0, robotMap.ctreTimeout)
        driveBase.l1.configPeakOutputForward(1, robotMap.ctreTimeout)
        driveBase.l1.configPeakOutputReverse(-1, robotMap.ctreTimeout)
        
        driveBase.r1.configNominalOutputForward(0, robotMap.ctreTimeout)
        driveBase.r1.configNominalOutputReverse(0, robotMap.ctreTimeout)
        driveBase.r1.configPeakOutputForward(1, robotMap.ctreTimeout)
        driveBase.r1.configPeakOutputReverse(-1, robotMap.ctreTimeout)
        
    def execute(self):
        # Set the drive speed.
        driveBase.drive(oi.getLeftDrive() * oi.getDriveSpeedModifier(), oi.getRightDrive() * oi.getDriveSpeedModifier())
            
    def isFinished(self):
        # TeleDrive never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop drive motors.
        driveBase.drive(0, 0)
