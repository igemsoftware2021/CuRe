try:
    import board
    import adafruit_lps35hw
    import RPi.GPIO as GPIO
except:
    print('Impossible to load libraries')
    quit()


class DeviceGPIO():
    def __init__(self, pin: int, start_state='off'):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        match start_state:
            case 'on', True:
                self.on()
            case 'off', False:
                self.off()

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = 'on'

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.state = 'off'

    def is_on(self):
        return self.state == 'on'

    def is_off(self):
        return self.state == 'off'


pressure_sensor = adafruit_lps35hw.LPS35HW(board.I2C())
GPIO.setmode(GPIO.BCM)
valve, pump = DeviceGPIO(23), DeviceGPIO(24)
