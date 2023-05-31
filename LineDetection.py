import numpy as np
import cv2
import RPi.GPIO as GPIO

video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 160)
video_capture.set(4, 120)
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

pwm_left.start(35)
pwm_right.start(35)

while True:
    # Capture the frames
    ret, frame = video_capture.read()

    # Crop the image
    crop_img = frame[60:120, 0:160]

    # Convert to grayscale
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Color thresholding
    ret, thresh1 = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)

    # Erode and dilate to remove accidental line detections
    mask = cv2.erode(thresh1, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find the contours of the frame
    contours, hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        cv2.line(crop_img, (cx, 0), (cx, 720), (255, 0, 0), 1)
        cv2.line(crop_img, (0, cy), (1280, cy), (255, 0, 0), 1)

        cv2.drawContours(crop_img, contours, -1, (0, 255, 0), 1)

        # Calculate area of the contour
        contour_area = cv2.contourArea(c)

        if contour_area > 2000 :
            # Dừng lại khi phát hiện vùng đen lớn
            pwm_left.ChangeDutyCycle(0)  # Dừng motor trái
            GPIO.output(6, GPIO.LOW)
            pwm_right.ChangeDutyCycle(0)  # Dừng motor phải
            GPIO.output(26, GPIO.LOW)
            print(cv2.contourArea(c))
        else:
            print("cx: ", cx)
            print("cy: ", cy)
            if cx >= 120:
                pwm_left.ChangeDutyCycle(50)
                pwm_right.ChangeDutyCycle(50)
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                print("Phai")
                print("contour_area ", cv2.contourArea(c))
            if 120 > cx > 50:
                pwm_left.ChangeDutyCycle(50)
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                pwm_right.ChangeDutyCycle(50)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                print("Thang")
                print("contour_area ", cv2.contourArea(c))
            if cx <= 50:
                pwm_left.ChangeDutyCycle(50)
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                pwm_right.ChangeDutyCycle(50)
                GPIO.output(in3, GPIO.HIGH)
                GPIO.output(in4, GPIO.LOW)
                print("Trai")
                print("contour_area ", cv2.contourArea(c))
                
    # Display the resulting frame
    cv2.imshow('frame2', crop_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
pwm_left.stop()
pwm_right.stop()
GPIO.cleanup()
