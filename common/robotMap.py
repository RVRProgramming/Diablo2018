###############
# Controllers #
###############
joystick = 0
gamepad = 1

##############
# Drive Base #
##############
# Motors
left1 = 2
left2 = 4
right1 = 1
right2 = 3
# Axes and Buttons
leftDriveStick = 0            # Gamepad: Left Thumbstick
rightDriveStick = 5           # Gamepad: Right Thumbstick
slowDriveButton = 6           # Gamepad: Right Bumper
# Constants
maxTeleopDriveSpeed = 1
slowDriveSpeed = 0.75
ctreTimeout = 10
peakCurrent = 45
peakTime = 10000
continuousCurrent = 39
countsPerRevolution = 4096
# PID
PIDSlot = 0
maxStartEffort = 0.1
maxEffort = 0.75
maxRampEffort = 0.65
minRampEffort = 0.1
minEffort = 0
allowableError = 250 * 0
mpPeriod = 50
mpDeadband = 0.01


###########
# Grabber #
###########
# Motors
leftArmMotor = 0              # This is a PLACEHOLDER
rightArmMotor = 1             # This is a PLACEHOLDER
# Axes and Buttons
grabberOpen = 2               # Joystick: Thumb
grabberClose = 1              # Joystick: Trigger
# Constants
grabberSpeed = 0.33
accumSpeed = 1
maxAccum = 1024
minAccum = 0

############
# Elevator #
############
# Motors
elevatorMotor1 = 2            # This is a PLACEHOLDER
elevatorMotor2 = 3            # This is a PLACEHOLDER
# Axes and Buttons
elevatorStick = 1             # Joystick: Y-Axis
# Constants
elevatorMaxSpeed = 1
