from wpilib.command.command import Command

from common.oi import oi
from subsystems.driveBase import driveBase


class TeleDrive(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the DriveBase while running.
        self.requires(driveBase)
        
    def execute(self):
        # Set the drive speeds in accordance with the Gamepad thumbstick values and Drive Speed Modifier
        driveBase.drive(oi.getLeftDrive() * oi.getDriveSpeedModifier(), oi.getRightDrive() * oi.getDriveSpeedModifier())
                
    def isFinished(self):
        # TeleDrive never finishes.
        return False

    def interrupted(self):
        # In case of an interruption, stop drive motors.
        driveBase.drive(0, 0)
