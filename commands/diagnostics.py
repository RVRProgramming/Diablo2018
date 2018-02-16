from wpilib.command.command import Command

from subsystems.driveBase import driveBase

class Diagnostics(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        super().execute()
        driveBase.diagnosticsToSmartDash()
      
    def isFinished(self):
        return False
