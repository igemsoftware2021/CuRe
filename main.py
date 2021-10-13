from time import sleep
from tools import Events, gui_path, get_current_page
import selenium.webdriver as selenium
from devices import pump, valve
from managers import *
from config import TIME_UNIT

browser = selenium.Chrome()
browser.get(gui_path())

events_catcher = Events(browser)

pressure_sensor_manager = PressureSensorManager(browser)
bioreactor_manager = BioReactorManager(browser)
managers = pressure_sensor_manager, bioreactor_manager

event_to_action = {'pump_on': pump.on, 'pump_off': pump.off, 'valve_on': valve.on, 'valve_off': valve.off}
page_to_manager = {'pressure_sensor': pressure_sensor_manager, 'bioreactor': bioreactor_manager}


def update():
    for manager in managers:
        manager.background_update()
    for event in events_catcher.get_waiting_and_clean():
        if event in event_to_action: event_to_action[event]()
        if 'set_thresholds:' in event:
            threshold_high, threshold_middle, threshold_low = (float(i) if i != '' else 0 for i in
                                                               event.split(':')[1].split(
                                                                   ';'))
            bioreactor_manager.threshold_low = threshold_low
            bioreactor_manager.threshold_middle = threshold_middle
            bioreactor_manager.threshold_high = threshold_high

    page = get_current_page(browser)
    if page in page_to_manager: page_to_manager[page].live_update()


while True:
    update()
    sleep(TIME_UNIT)
