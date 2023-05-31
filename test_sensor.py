import RPi.GPIO as GPIO
import time

def distance_measurement(trigger_pin, echo_pin):
    # Thiết lập chế độ của các chân GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

    # Đặt chân Trigger lên mức cao trong 10 μs
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    # Ghi thời điểm bắt đầu
    pulse_start = time.time()

    # Đợi cho đến khi chân Echo lên mức cao
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    # Đợi cho đến khi chân Echo xuống mức thấp
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    # Tính thời gian trôi qua
    pulse_duration = pulse_end - pulse_start

    # Tính khoảng cách dựa trên thời gian và vận tốc âm thanh
    speed_of_sound = 343.0  # Vận tốc âm thanh trong m/s
    distance = (pulse_duration * speed_of_sound) / 2

    # Chuyển đổi khoảng cách thành cm
    distance = round(distance, 2)

    # Đặt chế độ GPIO về trạng thái ban đầu
    GPIO.cleanup()

    return distance

while(1==1):
# Sử dụng hàm distance_measurement
	trigger_pin = 11  # Chân GPIO sử dụng làm Trigger
	echo_pin = 8  # Chân GPIO sử dụng làm Echo

	distance = distance_measurement(trigger_pin, echo_pin)
	print(distance)
	
