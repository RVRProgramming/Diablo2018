import ctre
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.smartdashboard import SmartDashboard

from common import robotMap


class Elevator(Subsystem):
    
    def __init__(self):
        super().__init__()
        
        # Initialize motors.
        self.elevatorMotor1 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.elevatorMotor1)
        self.elevatorMotor2 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.elevatorMotor2)
        
        self.elevatorMotor2.follow(self.elevatorMotor1)
        
        self.PDP = wpilib.PowerDistributionPanel()
        
    def elevate(self, speed):
        # Set elevation speed.
        self.elevatorMotor1.set(speed)

    def diagnosticsToSmartDash(self):
        SmartDashboard.putNumber("Elevator Speed", self.elevatorMotor1.getMotorOutputPercent())
        SmartDashboard.putNumber("Elevator Motor 1 Amperage", self.PDP.getCurrent(robotMap.elevatorPDPPort1))
        SmartDashboard.putNumber("Elevator Motor 2 Amperage", self.PDP.getCurrent(robotMap.elevatorPDPPort2))

elevator = Elevator()
