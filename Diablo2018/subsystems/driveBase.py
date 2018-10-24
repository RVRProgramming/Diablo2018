from ctre import FeedbackDevice, ControlMode, NeutralMode
import ctre
from robotpy_ext.common_drivers.navx.ahrs import AHRS
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.robotbase import RobotBase
from wpilib.smartdashboard import SmartDashboard

from common import robotMap


class DriveBase(Subsystem):
    
    def __init__(self):
        super().__init__()
        # Initialize and calibrate the NavX-MXP.
        self.gyro = AHRS.create_spi(wpilib.SPI.Port.kMXP)
        self.gyro.reset()
        
        # Initialize motors.
        self.l1 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.left1)
        self.l2 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.left2)
        self.r1 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.right1)
        self.r2 = ctre.wpi_talonsrx.WPI_TalonSRX(robotMap.right2)
        
        # Select a sensor for PID.
        self.l1.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0, robotMap.ctreTimeout)
        self.r1.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0, robotMap.ctreTimeout)      
        
        # Left sensor runs in reverse so the phase must be set for PID.
        self.l1.setSensorPhase(True)
        self.r1.setSensorPhase(True)
        
        # Invert motor output as necessary.
        self.r1.setInverted(True)
        self.r2.setInverted(True)
        
        # Set secondary motors to follow primary motor speed.
        self.l2.follow(self.l1)
        self.r2.follow(self.r1)
        
        # Set talons to brake automatically.
        self.l1.setNeutralMode(NeutralMode.Brake)
        self.l2.setNeutralMode(NeutralMode.Brake)
        self.r1.setNeutralMode(NeutralMode.Brake)
        self.r2.setNeutralMode(NeutralMode.Brake)
        
        # If code is running on a RoboRio, configure current limiting.
        if RobotBase.isReal():
            self.l1.configPeakCurrentLimit(robotMap.peakCurrent, robotMap.ctreTimeout)
            self.l1.configPeakCurrentDuration(robotMap.peakTime, robotMap.ctreTimeout)
            self.l1.configContinuousCurrentLimit(robotMap.continuousCurrent, robotMap.ctreTimeout)
            self.l1.enableCurrentLimit(True)
            
            self.l2.configPeakCurrentLimit(robotMap.peakCurrent, robotMap.ctreTimeout)
            self.l2.configPeakCurrentDuration(robotMap.peakTime, robotMap.ctreTimeout)
            self.l2.configContinuousCurrentLimit(robotMap.continuousCurrent, robotMap.ctreTimeout)
            self.l2.enableCurrentLimit(True)
            
            self.r1.configPeakCurrentLimit(robotMap.peakCurrent, robotMap.ctreTimeout)
            self.r1.configPeakCurrentDuration(robotMap.peakTime, robotMap.ctreTimeout)
            self.r1.configContinuousCurrentLimit(robotMap.continuousCurrent, robotMap.ctreTimeout)
            self.r1.enableCurrentLimit(True)
            
            self.r2.configPeakCurrentLimit(robotMap.peakCurrent, robotMap.ctreTimeout)
            self.r2.configPeakCurrentDuration(robotMap.peakTime, robotMap.ctreTimeout)
            self.r2.configContinuousCurrentLimit(robotMap.continuousCurrent, robotMap.ctreTimeout)
            self.r2.enableCurrentLimit(True)
        
        # Reset max recorded velocities
        self.maxRecordedLeftVelocity = 0
        self.maxRecordedRightVelocity = 0
        
        self.r1.configNeutralDeadband(0.1, 10)
        self.r2.configNeutralDeadband(0.1, 10)
        self.l1.configNeutralDeadband(0.1, 10)
        self.l2.configNeutralDeadband(0.1, 10)
        
    def diagnosticsToSmartDash(self):
        # Add position, velocity, and angle values to the SmartDash.
        
        SmartDashboard.putNumber("Left Encoder", self.getLeftPosition() / robotMap.countsPerRevolution)
        SmartDashboard.putNumber("Right Encoder", self.getRightPosition() / robotMap.countsPerRevolution)
#         SmartDashboard.putNumber("Left Velocity", self.getLeftVelocity())
#         SmartDashboard.putNumber("Right Velocity", self.getRightVelocity())
         
        if RobotBase.isReal():
            SmartDashboard.putNumber("Left Speed", self.l1.getMotorOutputPercent())
            SmartDashboard.putNumber("Right Speed", self.r1.getMotorOutputPercent())
        
        SmartDashboard.putNumber("Gyro Angle", self.gyro.getAngle())
        SmartDashboard.putNumber("Barometric Pressure", self.gyro.getBarometricPressure())

    def drive(self, leftSpeed, rightSpeed):
        # Set drive speed.
        self.l1.set(leftSpeed)
        self.r1.set(rightSpeed)
        
    def disable(self):
        self.l1.disable()
        self.r1.disable()
        
    def getGyroAngle(self):
        return self.gyro.getAngle()
        
    def resetGyroAngle(self):
        self.gyro.reset()
        
    def getLeftPosition(self):
        return -self.l1.getSensorCollection().getQuadraturePosition() 
        
    def getRightPosition(self):
        return self.r1.getSensorCollection().getQuadraturePosition()
    
    def resetEncoderPosition(self):
        self.l1.getSensorCollection().setQuadraturePosition(0, robotMap.ctreTimeout)
        self.r1.getSensorCollection().setQuadraturePosition(0, robotMap.ctreTimeout)
        
    def getRightVelocity(self):
        return self.r1.getSensorCollection().getQuadratureVelocity()
        
    def getLeftVelocity(self):
        return -self.l1.getSensorCollection().getQuadratureVelocity()

    def positionPID(self, position):
        self.l1.set(ControlMode.Position, position)
        self.r1.set(ControlMode.Position, position)
        
    def getLeftError(self):
        return self.l1.getClosedLoopError(0)
        
    def getRightError(self):
        return self.r1.getClosedLoopError(0)


driveBase = DriveBase()
