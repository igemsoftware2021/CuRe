from devices import pressure_sensor, valve
from datetime import datetime, timedelta
from tools import get_current_page
from config import PLOT_N, THRESHOLD_HIGH, THRESHOLD_MIDDLE, THRESHOLD_LOW, WAIT_TIME_FOR_EMPTY_ALL


class Manager():
    def background_update(self):
        """
        Executed in background to collect informations
        """
        raise Exception(f'You must override the update function of {self.__class__}')

    def live_update(self):
        """
        Executed while the page is currently running
        """
        raise Exception(f'You must override the display function of {self.__class__}')


class PressureSensorManager(Manager):
    def __init__(self, browser):
        self.browser = browser
        self.pressures = []
        self.temperatures = []

    def background_update(self):
        self.pressures.append(pressure_sensor.pressure)
        self.temperatures.append(pressure_sensor.temperature)

    def live_update(self):
        try:
            self.browser.execute_script(
                f'plot_datasets({[self.pressures[-PLOT_N:]]}, {list(range(PLOT_N))}, ["pressure", "temperature"])')
        finally:
            pass


class BioReactorManager(Manager):
    threshold_low, threshold_middle, threshold_high = THRESHOLD_LOW, THRESHOLD_MIDDLE, THRESHOLD_HIGH  # unit = pascal
    mode = 'fill'

    counter = None

    def __init__(self, browser):
        self.browser = browser
        self.pressures = []
        self.temperatures = []

    def background_update(self):
        self.pressures.append(pressure_sensor.pressure)
        self.temperatures.append(pressure_sensor.temperature)
        if not self.master: return
        if self.counter is not None and self.counter - datetime.now() > timedelta(seconds=WAIT_TIME_FOR_EMPTY_ALL):
            self.mode = 'empty all'

        if self.mode == 'fill':
            valve.off()
            if pressure_sensor.pressure > self.threshold_high:
                self.mode = 'empty'
                self.counter = None
        elif self.mode == 'empty':
            valve.on()
            if pressure_sensor.pressure < self.threshold_middle:
                self.mode = 'fill'
                self.counter = datetime.now()
        elif self.mode == 'empty all':
            valve.on()
            if pressure_sensor.pressure < self.threshold_low:
                self.mode = 'fill'
                self.counter = None

    @property
    def master(self):
        return get_current_page(self.browser) == 'bioreactor'

    def live_update(self):
        try:
            self.browser.execute_script(
                f'set_default_thresholds({self.threshold_high},{self.threshold_middle},{self.threshold_low})')
            self.browser.execute_script(
                f'plot_datasets({[self.pressures[-PLOT_N:]]}, {list(range(PLOT_N))}, ["pressure", "temperature"])')
        finally:
            pass
