from wpilib.command.command import Command

from subsystems.driveBase import driveBase
from subsystems.grabber import grabber

class Diagnostics(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        super().execute()
        driveBase.diagnosticsToSmartDash()
        grabber.diagnosticsToSmartDash()
      
    def isFinished(self):
        return False
