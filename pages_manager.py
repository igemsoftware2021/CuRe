from devices import pressure_sensor
from tools import Updatable


class PressureSensorPageManager(Updatable):
    def __init__(self, browser):
        self.browser = browser
        self.pressures = []
        self.temperatures = []

    def update(self):
        self.pressures.append(pressure_sensor.pressure)
        self.temperatures.append(pressure_sensor.temperature)

    def plot(self, n=10):
        try:
            self.browser.execute_script(
                f'plot_datasets({[self.pressures[-n:]]}, {list(range(n))}, ["pressure", "temperature"])')
        finally:
            pass


class BioReactor1PageManager: pass


class BioReactor2PageManager: pass
