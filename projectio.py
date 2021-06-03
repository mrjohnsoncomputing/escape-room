import RPi.GPIO as GPIO

class Projectio:
    def __init__(self):
        ### PINOUT ###
        # Switch 11 (GPIO 17)
        # LED 13 (GPIO 27)
        # A+B 16 (GPIO 23)
        # C+D 18 (GPIO 24)

        # Initiate Latching Switch
        self.AB = 16
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.AB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.LED = 13
        # Assign LED
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED, GPIO.OUT)




    def switch_is_on(self, switch):
        if GPIO.input(switch) == GPIO.HIGH:
            return True
        else:
            return False


    def switch_is_off(self, switch):
        if GPIO.input(switch) == GPIO.LOW:
            return True
        else:
            return False

    def LED_on(self, pin=self.LED):
        GPIO.output(pin, GPIO.HIGH)

    def LED_off(self, pin=self.LED):
        GPIO.output(pin, GPIO.LOW)