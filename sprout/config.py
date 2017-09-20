import logging

import classes


# Console logging
LOG_CONSOLE_FORMAT = '%(levelname)s: %(message)s'
LOG_CONSOLE_LEVEL = logging.DEBUG

# File logging
LOG_FILE_FORMAT = '%(asctime)s: %(name)s: %(levelname)-8s: %(message)s'
LOG_FILE_LEVEL = logging.INFO


class FileKeys(classes.Enum):
    BaseName = '<basename>'
    User = '<userkey>'
    Version = '<version>'
    Ext = '<ext>'


# File save formatting
FILE_VERSION_PAD = 3
FILE_SAVE_FORMAT = '%s_%s.%s.%s' % (FileKeys.BaseName, FileKeys.User,
                                    FileKeys.Version, FileKeys.Ext)
