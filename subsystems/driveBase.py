import ctre
from wpilib.command.subsystem import Subsystem
from wpilib.robotdrive import RobotDrive

from common import robotMap


class DriveBase(Subsystem):
    
    def __init__(self):
        super().__init__()
        self.diabloDrive = RobotDrive(ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.l1), ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.l2), ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.r1), ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.r2))
        
    def drive(self, leftSpeed, rightSpeed):
        self.diabloDrive.tankDrive(leftSpeed, rightSpeed, squaredInputs=False)


driveBase = DriveBase()
