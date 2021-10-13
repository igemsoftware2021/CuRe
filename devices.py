from config import DEBUG_MODE

if DEBUG_MODE:
    import debug_libs.board as board
    import debug_libs.adafruit_lps35hw as adafruit_lps35hw
    import debug_libs.RPi.GPIO as GPIO
else:
    import board
    import adafruit_lps35hw
    import RPi.GPIO as GPIO


class DeviceGPIO():
    def __init__(self, pin: int, start_state='off'):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        if start_state == 'on':
            self.on()
        else:
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
