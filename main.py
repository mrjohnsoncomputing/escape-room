import RPi.GPIO as GPIO

# PINOUT
# Switch 11 (GPIO 17)
# LED 13 (GPIO 27)
# A+B 16 (GPIO 23)
# C+D 18 (GPIO 24)

# Initiate Latching Switch
AB = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(AB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)