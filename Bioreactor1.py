from datetime import datetime, timedelta
from devices import pressure_sensor, valve
from tools import Updatable

threshold_low, threshold_x, threshold_high = 924, 928, 930  # unit = pascal


class Bioreactor1Manager(Updatable):
    mode = 'fill'
    counter = None

    def __init__(self, browser):
        self.browser = browser
        self.pressures = []
        self.temperatures = []

    def update(self):
        if self.counter is not None and self.counter - datetime.now() > timedelta(hours=2):
            self.mode = 'empty all'
        match self.mode:
            case 'fill':
                valve.off()
                if pressure_sensor.pressure > threshold_high:
                    self.mode = 'empty'
                    self.counter = None
            case 'empty':
                valve.on()
                if pressure_sensor.pressure < threshold_x:
                    self.mode = 'fill'
                    self.counter = datetime.now
            case 'empty all':
                valve.on()
                if pressure_sensor.pressure < threshold_low:
                    self.mode = 'fill'
                    self.counter = None

    def plot(self, n=10):
        pass  # plot useful informations



