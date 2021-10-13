from os.path import realpath


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
    path = realpath('GUI/main.html')
    if '/' in path: path = 'file://' + path
    return path


def get_current_page(browser):
    # browser.current_url.replace('\\', '/').split('/')[-1].replace('.html', '')
    return browser.execute_script('return page')
