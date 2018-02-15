import ctre
from ctre._impl.autogen.ctre_sim_enums import FeedbackDevice, ControlMode
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
        # self.l1.setInverted(True)
        # self.l2.setInverted(True)
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
        
        # Set PID Constants and Settings.
        self.l1.selectProfileSlot(0, 0)
        self.l1.config_kF(0, robotMap.kF, 10)
        self.l1.config_kP(0, robotMap.kP, 10)
        self.l1.config_kD(0, robotMap.kD, 10)
        self.l1.config_kI(0, robotMap.kI, 10)
        
        self.r1.selectProfileSlot(0, 0)
        self.r1.config_kF(0, robotMap.kF, 10)
        self.r1.config_kP(0, robotMap.kP, 10)
        self.r1.config_kD(0, robotMap.kD, 10)
        self.r1.config_kI(0, robotMap.kI, 10)
    
        self.l1.configNominalOutputForward(0, 10)
        self.l1.configNominalOutputReverse(0, 10)
        self.l1.configPeakOutputForward(0.75 * 12, 10)
        self.l1.configPeakOutputReverse(-0.75 * 12, 10)
        
        self.r1.configNominalOutputForward(0, 10)
        self.r1.configNominalOutputReverse(0, 10)
        self.r1.configPeakOutputForward(0.75 * 12, 10)
        self.r1.configPeakOutputReverse(-0.75 * 12, 10)
        
        self.l1.configAllowableClosedloopError(0, 0, 10)
        self.r1.configAllowableClosedloopError(0, 0, 10)
        
    def diagnosticsToSmartDash(self):
        # Add position, velocity, and angle values to the SmartDash.
        SmartDashboard.putNumber("Left Encoder", self.getLeftPosition() / 1000 if RobotBase.isSimulation() else self.getLeftPosition() / 4096)
        SmartDashboard.putNumber("Right Encoder", self.getRightPosition() / 1000 if RobotBase.isSimulation() else self.getRightPosition() / 4096)
        SmartDashboard.putNumber("Left Velocity", self.getLeftVelocity())
        SmartDashboard.putNumber("Right Velocity", self.getRightVelocity())
        
        SmartDashboard.putNumber("Left Thumbstick", oi.getLeftDrive())
        SmartDashboard.putNumber("Right Thumbstick", oi.getRightDrive())
        
        SmartDashboard.putNumber("NavX Angle", self.gyro.getAngle())

    def drive(self, leftSpeed, rightSpeed):
        # Set drive speed.
        self.l1.set(leftSpeed)
        self.r1.set(rightSpeed)
        
    def getGyroAngle(self):
        return self.gyro.getAngle()
        
    def resetGyroAngle(self):
        self.gyro.reset()
        
    def getLeftPosition(self):
        return -self.l1.getSensorCollection().getQuadraturePosition()
        
    def getRightPosition(self):
        return self.r1.getSensorCollection().getQuadraturePosition()
    
    def resetEncoderPosition(self):
        self.l1.getSensorCollection().setQuadraturePosition(0, 10)
        self.r1.getSensorCollection().setQuadraturePosition(0, 10)
        
    def getRightVelocity(self):
        return self.r1.getSensorCollection().getQuadratureVelocity()
        
    def getLeftVelocity(self):
        return -self.l1.getSensorCollection().getQuadratureVelocity()

    def positionPID(self, position):
        self.l1.set(ControlMode.Position, position)
        self.r1.set(ControlMode.Position, position)

driveBase = DriveBase()
