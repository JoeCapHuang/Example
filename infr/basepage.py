from infr.driver import Driver


class BasePage:
    # url должен переопределятся для каждой страницы.
    url = None

    def __init__(self):
        super().__init__()

    def open(self):
        Driver().get(self.url)
        return self

    def refresh(self):
        Driver().refresh()
        return self
