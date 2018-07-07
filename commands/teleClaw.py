from wpilib.command.command import Command

from common.oi import oi
from subsystems.pneumaticClaw import claw


class TeleClaw(Command):

    def __init__(self):
        super().__init__()
        
        # Ensure exclusive access to the Grabber while running.
        self.requires(claw)
        
    def initialize(self):
        claw.grab(False)
        
    def execute(self):
        if oi.getClawClose():
            claw.grab(True)
        elif oi.getClawOpen():
            claw.grab(False)
                    
    def isFinished(self):
        return False
        