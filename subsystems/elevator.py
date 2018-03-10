import ctre
import wpilib
from wpilib.command.subsystem import Subsystem

from common import robotMap


class Elevator(Subsystem):
    
    def __init__(self):
        super().__init__()
        
        # Initialize motors.
        self.elevatorEncoder = wpilib.Encoder(4, 5, False, wpilib.Encoder.EncodingType.k1X)
        self.elevatorMotor1 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.elevatorMotor1)
        self.elevatorMotor2 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.elevatorMotor2)
        
    def elevate(self, speed):
        # Set elevation speed.
        self.elevatorMotor1.set(speed)
        self.elevatorMotor2.set(speed)
        
    def getPosition(self):
        return self.elevatorEncoder.get()

elevator = Elevator()
