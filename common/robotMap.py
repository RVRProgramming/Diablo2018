###############
# Controllers #
###############
joystick = 0
gamepad = 1

##############
# Drive Base #
##############

# DEAR FUTURE AIDAN: For the love of all god please make these variables drive naming specific. These are terrible. Sincerely, Aidan from 3/12/2018

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
grabberLeftMotor = 0          # This is a PLACEHOLDER
grabberRightMotor = 1         # This is a PLACEHOLDER
# Axes and Buttons
grabberOpen = 2               # Joystick: Thumb
grabberClose = 1              # Joystick: Trigger
# Constants
grabberSpeed = 1


############
# Elevator #
############
# Motors
elevatorMotor1 = 5
elevatorMotor2 = 6
# Axes and Buttons
elevatorStick = 1             # Joystick: Y-Axis
elevatorOverride = 8         
# Constants
elevatorMaxSpeed = 1
elevatorMaxHeight = 3096      # This is a PLACEHOLDER
elevatorMinHeight = -100
