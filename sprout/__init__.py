"""

"""

import tempfile
import logging
import sys

import classes
import config

# Build up logging handlers
__consoleFormat = logging.Formatter(config.LOG_CONSOLE_FORMAT)
__consoleHandler = logging.StreamHandler(sys.stdout)
__consoleHandler.setFormatter(__consoleFormat)
__consoleHandler.setLevel(config.LOG_CONSOLE_LEVEL)

__fileFormat = logging.Formatter(config.LOG_FILE_FORMAT)
__fileHandler = logging.FileHandler('%s/%s' % (tempfile.gettempdir(), 'sproutLog.log'), mode='w')
__fileHandler.setFormatter(__fileFormat)
__fileHandler.setLevel(config.LOG_FILE_LEVEL)

# Put it all together
LOG = logging.getLogger('Sprout')
LOG.setLevel(logging.DEBUG)
LOG.addHandler(__fileHandler)
LOG.addHandler(__consoleHandler)

# Store the current application so it may always be accessed from this module
__intApp = '__sproutApp'

# "Que" object to keep track of anything that is done with an application
# before the application is set in this module.
__que = '__sproutTemp'


class _SproutQue(object):
    def __init__(self):
        super(_SproutQue, self).__init__()

        self.__menuItems = []

    def addMenuItem(self, menuName, itemName, function, **kwargs):
        self.__menuItems.append((menuName, itemName, function, kwargs))

    def menuItems(self):
        return self.__menuItems


def _excepthook(type, value, traceback):
    LOG.critical('Unhandled Exception: %s. See log for details.\n' % value,
                 exc_info=(type, value, traceback))


def application():
    import sprout

    if sprout.__intApp not in sprout.__dict__:
        LOG.warn('The sprout application is not set. A que object will be provided '
                 'to store UI elements until an application is provided.')

        if sprout.__que not in sprout.__dict__:
            sprout.__dict__[sprout.__que] = _SproutQue()
        return sprout.__dict__[sprout.__que]

    return sprout.__dict__[sprout.__intApp]


def setApplication(app):
    import abstract
    import sprout

    app = app()
    if not isinstance(app, abstract.Application):
        LOG.error('Application must be %s. Received %s.' % (abstract.Base, type(app)))
        return

    # If a que object exists, read through it and modify the new
    # application accordingly.
    if sprout.__que in sprout.__dict__:
        for mi in sprout.__dict__[sprout.__que].menuItems():
            app.addMenuItem(mi[0], mi[1], mi[2], **mi[3])

    LOG.info('Seed planted: %s' % type(app))
    sprout.__dict__[sprout.__intApp] = app


sys.excepthook = _excepthook
