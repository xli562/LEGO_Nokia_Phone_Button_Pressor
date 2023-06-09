#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import DCMotor


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
print('start')

MotorB = DCMotor(Port.B)
colorSensor = ColorSensor(Port.S1)

while True:
    print(colorSensor.reflection())
        


MotorB.stop()

print('end')

