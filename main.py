from time import sleep

from tools import Events, gui_path

# https://deusyss.developpez.com/tutoriels/RaspberryPi/PythonEtLeGpio/

import selenium.webdriver as selenium
# https://www.selenium.dev/projects/
# https://pypi.org/project/selenium/

import selenium.webdriver.support.events as events

# https://chercher.tech/python/listeners-selenium-python

browser = selenium.Chrome()
browser.get(gui_path())

events_manager = Events(browser)

from pressureSensor import PressureSensorManager

pressure_sensor_manager = PressureSensorManager(browser)


def update():
    pressure_sensor_manager.update()
    match browser.execute_script('return get_current_page()'):
        case 'main':
            pass
        case 'pressure_sensor':
            pressure_sensor_manager.plot()
        case _:
            print('Unknown page')


while True:
    update()
    sleep(.2)
