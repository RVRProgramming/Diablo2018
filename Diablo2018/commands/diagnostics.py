from wpilib.command.command import Command

from subsystems.elevator import elevator
from subsystems.driveBase import driveBase


class Diagnostics(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        super().execute()
        driveBase.diagnosticsToSmartDash()
        elevator.diagnosticsToSmartDash()
      
    def isFinished(self):
        return False
