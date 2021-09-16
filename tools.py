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


class Updatable():
    def update(self):
        raise Exception(f'You must override the update function of {self.__class__}')
