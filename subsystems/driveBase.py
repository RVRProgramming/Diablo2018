import ctre
from wpilib.command.subsystem import Subsystem

from common import robotMap
from wpilib.smartdashboard import SmartDashboard


class DriveBase(Subsystem):
    
    def __init__(self):
        super().__init__()
        self.l1 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.l1)
        self.l2 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.l2)
        self.r1 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.r1)
        self.r2 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.r2)
        
        self.l1.setInverted(True)
        self.l2.setInverted(True)
        self.r1.setInverted(True)
        self.r2.setInverted(True)
        
        self.l2.follow(self.l1)
        self.r2.follow(self.r1)
        """
        self.l1.configPeakCurrentLimit(40, 10)
        self.l1.configPeakCurrentDuration(10000, 10)
        self.l1.configContinuousCurrentLimit(35, 10)
        self.l1.enableCurrentLimit(True)
        
        self.l2.configPeakCurrentLimit(40, 10)
        self.l2.configPeakCurrentDuration(10000, 10)
        self.l2.configContinuousCurrentLimit(35, 10)
        self.l2.enableCurrentLimit(True)
        
        self.r1.configPeakCurrentLimit(40, 10)
        self.r1.configPeakCurrentDuration(10000, 10)
        self.r1.configContinuousCurrentLimit(35, 10)
        self.r1.enableCurrentLimit(True)
        
        self.r2.configPeakCurrentLimit(40, 10)
        self.r2.configPeakCurrentDuration(10000, 10)
        self.r2.configContinuousCurrentLimit(35, 10)
        self.r2.enableCurrentLimit(True)"""
        
    def drive(self, leftSpeed, rightSpeed):
        self.l1.set(leftSpeed)
        self.r1.set(rightSpeed)
        
        SmartDashboard.putNumber("Left Encoder", self.l1.getSensorCollection().getQuadraturePosition())
        SmartDashboard.putNumber("Right Encoder", self.r1.getSensorCollection().getQuadraturePosition())
        
"""    def __init__(self):
        super().__init__()
        self.diabloDrive = RobotDrive(ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.l1), ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.l2), ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.r1), ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.r2))
        
    def drive(self, leftSpeed, rightSpeed):
        self.diabloDrive.tankDrive(-leftSpeed, -rightSpeed, squaredInputs=False)"""

driveBase = DriveBase()
