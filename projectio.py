import RPi.GPIO as GPIO
from time import sleep as wait
import datetime


class Projectio:
    def __init__(self):
        ### PINOUT ###
        # Switch 11 (GPIO 17)
        # LED 13 (GPIO 27)
        # A+B 16 (GPIO 23)
        # C+D 18 (GPIO 24)

        # Initiate Latching Switch
        self.AB = 23
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.AB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.testBridge()

        self.LED = 27
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

    def LED_on(self):
        GPIO.output(self.LED, GPIO.HIGH)

    def LED_off(self):
        GPIO.output(self.LED, GPIO.LOW)

    def test_LED(self):
        for i in range(10):
            self.LED_on()
            wait(1)
            self.LED_off()
            wait(1)

    def test_bridge(self):
 
        def my_callback(channel):
            if GPIO.input(channel) == GPIO.HIGH:
                print('\n▼  at ' + str(datetime.datetime.now()))
            else:
                print('\n ▲ at ' + str(datetime.datetime.now()))
        
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.AB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(self.AB, GPIO.BOTH, callback=my_callback)
        
            message = raw_input('\nPress any key to exit.\n')
        
        finally:
            GPIO.cleanup()
        
        print("Goodbye!")