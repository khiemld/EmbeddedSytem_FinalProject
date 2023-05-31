import cv2
import numpy as np
import time
from imutils.perspective import four_point_transform
import RPi.GPIO as GPIO
#from imutils import contours
import imutils
from sensor import UltraSonic

US=UltraSonic()
camera = cv2.VideoCapture(0)
in1 = 13
in2 = 12
in3 = 21
in4 = 20
ena = 6
enb = 26
# Setup Output Pins
# Motor trái
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)
pwm_left = GPIO.PWM(ena,1000)
# Motor phải
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
pwm_right = GPIO.PWM(enb,1000)

pwm_left.start(50)
pwm_right.start(50)

hz=50

def avoid():
    while True:
		#print("distance: ", US.Distance())
        if US.Distance() < 50:
            #Quay phai
            pwm_left.ChangeDutyCycle(80)
            pwm_right.ChangeDutyCycle(60)
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            time.sleep(0.5)
            # #Di thang
            pwm_left.ChangeDutyCycle(hz)
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            pwm_right.ChangeDutyCycle(hz)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            time.sleep(0.5)
        else: 
            #Di thang
            pwm_left.ChangeDutyCycle(hz)
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            pwm_right.ChangeDutyCycle(hz)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            time.sleep(0.5)

        # if the `q` key was pressed, break from the loop
        if cv2.waitKey(1) & 0xFF is ord('q'):
            cv2.destroyAllWindows()
            print("Stop programm and close all windows")
            break

def main():
    avoid()


if __name__ == '__main__':
    main()
