import logging


class QtHandler(logging.Handler):
    def __init__(self, statusBar, duration=3000):
        super(QtHandler, self).__init__()
        self._statusBar = statusBar
        self._duration = duration

    def setDuration(self, duration):
        self._duration = duration

    def emit(self, record):
        record = self.format(record)
        self._statusBar.showMessage(record, self._duration)
