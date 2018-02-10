import ctre
from ctre._impl.autogen.ctre_sim_enums import FeedbackDevice
from robotpy_ext.common_drivers.navx.ahrs import AHRS
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.robotbase import RobotBase
from wpilib.smartdashboard import SmartDashboard

from common import robotMap
from common.oi import oi


class DriveBase(Subsystem):
    
    def __init__(self):
        super().__init__()
        # Initialize and calibrate the NavX-MXP.
        self.gyro = AHRS.create_spi(wpilib.SPI.Port.kMXP)
        while(self.gyro.isCalibrating() and RobotBase.isReal()):
            pass
        self.gyro.reset()
        
        # Initialize motors.
        self.l1 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.left1)
        self.l2 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.left2)
        self.r1 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.right1)
        self.r2 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.right2)
        
        self.l1.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0, 10)
        self.r1.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0, 10)        
        
        self.l1.setSensorPhase(True)
        
        # Invert motor output as necessary.
        #self.l1.setInverted(True)
        #self.l2.setInverted(True)
        self.r1.setInverted(True)
        self.r2.setInverted(True)
        
        # Set secondary motors to follow primary motor speed.
        self.l2.follow(self.l1)
        self.r2.follow(self.r1)
        
        # If code is running on a RoboRio, configure current limiting.
        if RobotBase.isReal():
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
            self.r2.enableCurrentLimit(True)
        
    def drive(self, leftSpeed, rightSpeed):
        # Set drive speed.
        self.l1.set(leftSpeed)
        self.r1.set(rightSpeed)
        
        # Add encoder and gyro values to the SmartDash.
        if RobotBase.isReal():
            SmartDashboard.putNumber("Left Encoder", self.l1.getSensorCollection().getQuadraturePosition())
            SmartDashboard.putNumber("Right Encoder", self.r1.getSensorCollection().getQuadraturePosition())
            SmartDashboard.putNumber("Left Thumbstick", oi.getLeftDrive())
            SmartDashboard.putNumber("Right Thumbstick", oi.getRightDrive())
            
        SmartDashboard.putNumber("NavX Angle", self.gyro.getAngle())
        

driveBase = DriveBase()
