import logging

from PySide.QtGui import *
from PySide.QtCore import *

import sprout
from sprout import classes


UI = None


class LogLevels(classes.Enum):
    Critical = logging.CRITICAL
    Error = logging.ERROR
    Warning = logging.WARNING
    Info = logging.INFO
    Debug = logging.DEBUG


class LoggingLevels(QDialog):
    def __init__(self, parent=None):
        super(LoggingLevels, self).__init__(parent=parent)

        self.setWindowTitle('Logging')
        self.setWindowIcon(QIcon())

        self.logLabels = []
        for lvl in sorted(LogLevels.hashValues()):
            self.logLabels.append(LogLevels.hashKeys()[LogLevels.hashValues().index(lvl)])

        self.logLevelBox = QComboBox()
        self.logLevelBox.addItems(self.logLabels)
        self.saveBtn = QPushButton('Save Changes')
        self.saveBtn.setMaximumWidth(150)
        self.saveBtn.clicked.connect(self.saveChanges)

        formLayout = QFormLayout()
        formLayout.setContentsMargins(0, 0, 0, 0)
        formLayout.addRow('Log Level', self.logLevelBox)

        layout = QVBoxLayout()
        layout.addLayout(formLayout)
        layout.addStretch()
        layout.addWidget(self.saveBtn)
        layout.setAlignment(self.saveBtn, Qt.AlignRight)
        self.setLayout(layout)

        self.resize(250, 50)

    def saveChanges(self):
        newLevel = LogLevels.hash()[self.logLevelBox.currentText()]
        sprout.LOG.setLevel(logging.DEBUG)

        sprout.LOG.info('Setting log level to %s' % self.logLevelBox.currentText())
        sprout.LOG.setLevel(newLevel)

        self.close()

    def show(self):
        # Update the log level
        currentLevel = LogLevels.hashKeys()[LogLevels.hashValues().index(sprout.LOG.level)]
        self.logLevelBox.setCurrentIndex(self.logLabels.index(currentLevel))

        super(LoggingLevels, self).show()


def showLoggingLevels():
    global UI

    if UI is None:
        # Find the main window
        mainWindow = None
        for obj in QApplication.instance().allWidgets():
            if not isinstance(obj, QMainWindow):
                continue

            mainWindow = obj
            break

        if not mainWindow:
            sprout.LOG.error('Unable to find a QMainWindow.')
            return

        UI = LoggingLevels(mainWindow)
    UI.show()


sprout.application().addMenuItem('Sprout', 'Logging', showLoggingLevels, test='HAHAHA')
