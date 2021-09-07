import time
import tools
import board
import adafruit_lps35hw

from tools import normalize_array

i2c = board.I2C()
lps = adafruit_lps35hw.LPS35HW(i2c)


class PressureSensorManager:
    def __init__(self, browser):
        self.browser = browser
        self.pressures = []
        self.temperatures = []

    def update(self):
        self.pressures.append(lps.pressure)
        self.temperatures.append(lps.temperature)

    def plot(self, n=10):
        try:
            self.browser.execute_script(
                f'plot_datasets({[self.pressures[-n:]]}, {list(range(n))}, ["pressure", "temperature"])')
        finally:
            pass
