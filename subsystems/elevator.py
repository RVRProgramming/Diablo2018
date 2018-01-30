import wpilib
from wpilib.command.subsystem import Subsystem

from common import robotMap


class Elevator(Subsystem):
    
    def __init__(self):
        super().__init__()
        self.elevatorMotor = wpilib.VictorSP(robotMap.elevatorMotor)
        
    def elevate(self, speed):
        self.elevatorMotor.set(speed)


elevator = Elevator()
