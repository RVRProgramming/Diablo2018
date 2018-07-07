import wpilib
from wpilib.command.subsystem import Subsystem

from common import robotMap


class PneumaticClaw(Subsystem):
    
    def __init__(self):
        super().__init__()
        self.solenoid1 = wpilib.Solenoid(robotMap.clawSolenoid)
    
    def grab(self, grab):
        self.solenoid1.set(grab)

    
claw = PneumaticClaw()
