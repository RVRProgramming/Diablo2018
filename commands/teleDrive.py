from wpilib.command.command import Command

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
        
    def execute(self):
        # Set the drive speeds in accordance with the Gamepad thumbstick values and Drive Speed Modifier
        # driveBase.drive(oi.getLeftDrive() * oi.getDriveSpeedModifier(), oi.getRightDrive() * oi.getDriveSpeedModifier())
        driveBase.drive((oi.getRightDrive() - self.getTurnSpeed()) * oi.getDriveSpeedModifier(), (oi.getRightDrive() + self.getTurnSpeed()) * oi.getDriveSpeedModifier())
        driveBase.diagnosticsToSmartDash()
        
    def getTurnSpeed(self):
        if oi.getRightDrive() > 0.1:
            return (oi.getLeftDrive() * oi.getRightDrive())
        else:
            return 0
            
    def isFinished(self):
        # TeleDrive never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop drive motors.
        driveBase.drive(0, 0)
