import abc
import glob
import getpass
import os
import re

from abstractBase import *
import sprout
from sprout import config
from sprout import events


class Scene(Base):
    def __init__(self):
        super(Scene, self).__init__()

    @abc.abstractmethod
    def fullName(self, fullPath=False):
        return ''

    def baseName(self):
        fileName = self.fullName()
        lookup = self.__fileNameRegex(config.FileKeys.BaseName)
        found = re.match(lookup, fileName)
        if found:
            return found.group(1)

        return ''

    @abc.abstractmethod
    def _user(self, userKey):
        pass

    def user(self):
        fileName = self.fullName()
        lookup = self.__fileNameRegex(config.FileKeys.User)
        found = re.match(lookup, fileName)
        key = ''
        if found:
            key = found.group(1)

        return self._user(key)

    def userKey(self):
        return getpass.getuser()

    def __fileNameRegex(self, key):
        lookup = config.FILE_SAVE_FORMAT
        lookup = lookup.replace('.', '\\.')

        for x in config.FileKeys.hashValues():
            if x == key:
                lookup = lookup.replace(key, '(.+)')
                continue

            lookup = lookup.replace(x, '\\w+')

        return lookup

    @abc.abstractmethod
    def _save(self, fullPath, **kwargs):
        pass

    def save(self, fileName='', path='', version=False, **kwargs):
        events.Signals.SaveSceneRequested.emit()

        # If no path is given, use the existing file path
        if not path:
            path = os.path.split(self.fullName(True))[0]

            # If there still is no path, bail.
            if not path:
                sprout.LOG.error('No path found for scene.')
                events.Signals.SaveSceneFinished.emit('')
                return

            # If the found path does not exist, bail.
            if not os.path.exists(path):
                sprout.LOG.error('Path does not exist: %s' % path)
                events.Signals.SaveSceneFinished.emit('')
                return

        # If no name was given, use the existing name
        if not fileName:
            fileName = self.fullName()

        # From here, just reconstruct the scene name using the
        # format in sprout.config
        scenePath = ''

        # TODO: I don't like the userkey being on this object. Should it be on application?


        result = self._save(scenePath, **kwargs)
        events.Signals.SaveSceneFinished.emit(result)

    @abc.abstractmethod
    def _saveAs(self, prefix, **kwargs):
        pass

    def saveAs(self, prefix='', **kwargs):
        events.Signals.SaveSceneAsRequested.emit()
        result = self._saveAs(prefix=prefix, **kwargs)
        events.Signals.SaveSceneAsFinished.emit(result)

    @abc.abstractmethod
    def _publish(self, **kwargs):
        pass

    def publish(self, **kwargs):
        events.Signals.PublishSceneRequested.emit()
        result = self._publish(**kwargs)
        events.Signals.PublishSceneFinished.emit(result)

    @abc.abstractmethod
    def _close(self, **kwargs):
        pass

    def close(self, **kwargs):
        events.Signals.CloseSceneRequested()
        result = self._close(**kwargs)
        events.Signals.CloseSceneFinished(result)

    def nextVersion(self, path):
        fileName = self.name()
        lookup = self.__fileNameRegex(config.FileNameKeys.User)
        found = re.match(lookup, fileName)

