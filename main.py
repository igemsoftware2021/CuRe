from time import sleep
from tools import Events, gui_path
import selenium.webdriver as selenium
from devices import pump, valve

browser = selenium.Chrome()
browser.get(gui_path())

events_manager = Events(browser)

updatables = []


def update():
    for updatable in updatables:
        updatable.update()
    for event in events_manager.get_waiting_and_clean():
        print(event)
        match event:
            case 'pump_on':
                pump.on()
            case 'pump_off':
                pump.off()
            case 'valve_on':
                valve.on()
            case 'valve_off':
                valve.off()
    match browser.execute_script('return get_current_page()'):
        case 'main':
            pass
        case 'pressure_sensor':
            pass
        # pressure_sensor_manager.plot()
        case _:
            print('Unknown page')


while True:
    update()
    sleep(.2)
