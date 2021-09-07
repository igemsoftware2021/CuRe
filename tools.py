from os import getcwd


class Events:
    def __init__(self, browser):
        self.browser = browser

    def get_waiting_events(self):
        return self.browser.execute_script('return waiting_events()')

    def clean_waiting_events(self):
        self.browser.execute_script('clean_events()')

    def get_waiting_and_clean(self):
        e = self.get_waiting_events()
        self.clean_waiting_events()
        return e


def gui_path():
    is_linux = '/' in getcwd()
    path_end = '/GUI/main.html'
    if not is_linux: path_end = path_end.replace('/', '\\')
    return getcwd() + path_end


def normalize_array(array, expected_length, blank_val=0):
    if len(array) > expected_length:
        return array[-expected_length:]
    else:
        return [blank_val] * (expected_length - len(array)) + array