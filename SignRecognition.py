import cv2
import numpy as np
import time
from imutils.perspective import four_point_transform
import RPi.GPIO as GPIO
#from imutils import contours
import imutils

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

pwm_left.start(40)
pwm_right.start(40)

hz=50

def findTrafficSign():
    '''
    This function find blobs with blue color on the image.
    After blobs were found it detects the largest square blob, that must be the sign.
    '''
    # define range HSV for blue color of the traffic sign
    lower_blue = np.array([20,100,100])
    upper_blue = np.array([40,255,255])

    while True:
        # grab the current frame
        (grabbed, frame) = camera.read()

        if not grabbed:
            print("No input image")
            break

        frame = imutils.resize(frame, width=500)
        frameArea = frame.shape[0]*frame.shape[1]

        # convert color image to HSV color scheme
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define kernel for smoothing
        kernel = np.ones((3,3),np.uint8)
        # extract binary image with active blue regions
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # morphological operations
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # find contours in the mask
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        # defite string variable to hold detected sign description
        detectedTrafficSign = None

        # define variables to hold values during loop
        largestArea = 0
        largestRect = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            for cnt in cnts:
                # Rotated Rectangle. Here, bounding rectangle is drawn with minimum area,
                # so it considers the rotation also. The function used is cv2.minAreaRect().
                # It returns a Box2D structure which contains following detals -
                # ( center (x,y), (width, height), angle of rotation ).
                # But to draw this rectangle, we need 4 corners of the rectangle.
                # It is obtained by the function cv2.boxPoints()
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                # count euclidian distance for each side of the rectangle
                sideOne = np.linalg.norm(box[0]-box[1])
                sideTwo = np.linalg.norm(box[0]-box[3])
                # count area of the rectangle
                area = sideOne*sideTwo
                # find the largest rectangle within all contours
                if area > largestArea:
                    largestArea = area
                    largestRect = box


        # draw contour of the found rectangle on  the original image
        if largestArea > frameArea*0.02:
            cv2.drawContours(frame,[largestRect],0,(0,0,255),2)



        #if largestRect is not None:
            # cut and warp interesting area
            warped = four_point_transform(mask, [largestRect][0])

            # show an image if rectangle was found
            #cv2.imshow("Warped", cv2.bitwise_not(warped))

            # use function to detect the sign on the found rectangle
            detectedTrafficSign = identifyTrafficSign(warped)
            print(detectedTrafficSign)
            if detectedTrafficSign=="Forward":
                #Di thang
                pwm_left.ChangeDutyCycle(hz)
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                pwm_right.ChangeDutyCycle(hz)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                time.sleep(2)
            elif detectedTrafficSign=="Turn Left":
                #Quay trai
                pwm_left.ChangeDutyCycle(hz)
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                pwm_right.ChangeDutyCycle(hz)
                GPIO.output(in3, GPIO.HIGH)
                GPIO.output(in4, GPIO.LOW)
                time.sleep(0.75)
                #Di thang
                pwm_left.ChangeDutyCycle(hz)
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                pwm_right.ChangeDutyCycle(hz)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                time.sleep(2)
            elif detectedTrafficSign=="Turn Right":
                #Quay phai
                pwm_left.ChangeDutyCycle(hz)
                pwm_right.ChangeDutyCycle(hz)
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                time.sleep(0.75)
                #Di thang
                pwm_left.ChangeDutyCycle(hz)
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                pwm_right.ChangeDutyCycle(hz)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                time.sleep(2)
            elif detectedTrafficSign=="Turn Back":
                #Quay phai
                pwm_left.ChangeDutyCycle(hz + 5)
                pwm_right.ChangeDutyCycle(hz + 5)
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                time.sleep(0.75)
                pwm_left.ChangeDutyCycle(hz + 5) 
                pwm_right.ChangeDutyCycle(hz +5)
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                time.sleep(0.75)
                #Di thang
                pwm_left.ChangeDutyCycle(hz)
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                pwm_right.ChangeDutyCycle(hz)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                time.sleep(2)
            elif detectedTrafficSign=="Stop":
                #Stop
                pwm_left.ChangeDutyCycle(0)  # Dừng motor trái
                GPIO.output(6, GPIO.LOW)
                pwm_right.ChangeDutyCycle(0)  # Dừng motor phải
                GPIO.output(26, GPIO.LOW)
            else:
                print('None')


            # write the description of the sign on the original image
            cv2.putText(frame, detectedTrafficSign, tuple(largestRect[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)

        # show original image
        cv2.imshow("Original", frame)

        # if the `q` key was pressed, break from the loop
        if cv2.waitKey(1) & 0xFF is ord('q'):
            cv2.destroyAllWindows()
            print("Stop programm and close all windows")
            break

def identifyTrafficSign(image):
    '''
    In this function we select some ROI in which we expect to have the sign parts. If the ROI has more active pixels than threshold we mark it as 1, else 0
    After path through all four regions, we compare the tuple of ones and zeros with keys in dictionary SIGNS_LOOKUP
    '''

    # define the dictionary of signs segments so we can identify
    # each signs on the image
    SIGNS_LOOKUP = {
        (1, 0, 0, 1): 'Turn Right', 
        (0, 0, 1, 1): 'Turn Left', 
        (0, 1, 0, 1): 'Forward', # 'Move Straight', 
        (1, 0, 1, 1): 'Turn Back', 
        (1, 1, 1, 0): 'Stop' # 'Stop', 
    }

    THRESHOLD = 150

    image = cv2.bitwise_not(image)
    # (roiH, roiW) = roi.shape
    #subHeight = thresh.shape[0]/10
    #subWidth = thresh.shape[1]/10
    (subHeight, subWidth) = np.divide(image.shape, 20)
    subHeight = int(subHeight)
    subWidth = int(subWidth)

    # mark the ROIs borders on the image
    cv2.rectangle(image, ( 3*subWidth, 8*subHeight), ( 7*subWidth, 14*subHeight), (0,255,0),2) # left block
    cv2.rectangle(image, ( 9*subWidth, 8*subHeight), (13*subWidth, 14*subHeight), (0,255,0),2) # center block
    cv2.rectangle(image, (15*subWidth, 8*subHeight), (19*subWidth, 14*subHeight), (0,255,0),2) # right block
    cv2.rectangle(image, ( 7*subWidth, 4*subHeight), (15*subWidth,  8*subHeight), (0,255,0),2) # top block

    # substract 5 ROI of the sign thresh image
    leftBlock   = image[8*subHeight:14*subHeight,  3*subWidth: 7*subWidth]
    centerBlock = image[8*subHeight:14*subHeight,  9*subWidth:13*subWidth]
    rightBlock  = image[8*subHeight:14*subHeight, 15*subWidth:19*subWidth]
    topBlock    = image[4*subHeight: 8*subHeight,  7*subWidth:15*subWidth]

    # we now track the fraction of each ROI
    leftFraction = np.sum(leftBlock)/(leftBlock.shape[0]*leftBlock.shape[1])
    centerFraction = np.sum(centerBlock)/(centerBlock.shape[0]*centerBlock.shape[1])
    rightFraction = np.sum(rightBlock)/(rightBlock.shape[0]*rightBlock.shape[1])
    topFraction = np.sum(topBlock)/(topBlock.shape[0]*topBlock.shape[1])

    segments = (leftFraction, centerFraction, rightFraction, topFraction)
    segments = tuple(1 if segment > THRESHOLD else 0 for segment in segments)

    cv2.imshow("Warped", image)

    if segments in SIGNS_LOOKUP:
        return SIGNS_LOOKUP[segments]
    else:
        return None


def main():
    findTrafficSign()


if __name__ == '__main__':
    main()
