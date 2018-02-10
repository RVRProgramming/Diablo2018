import wpilib
from wpilib.command.subsystem import Subsystem

from common import robotMap


class Elevator(Subsystem):
    
    def __init__(self):
        super().__init__()
        
        # Initialize motors.
        self.elevatorMotor1 = wpilib.VictorSP(robotMap.elevatorMotor1)
        self.elevatorMotor2 = wpilib.VictorSP(robotMap.elevatorMotor2)
        
    def elevate(self, speed):
        # Set elevation speed.
        self.elevatorMotor1.set(speed)
        self.elevatorMotor2.set(speed)


elevator = Elevator()
