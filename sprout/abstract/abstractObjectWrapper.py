import abc

from abstractBase import *


class ObjectWrapper(Base):
    __metaclass__ = abc.ABCMeta

    def __init__(self, nativeObject=None):
        super(ObjectWrapper, self).__init__()

        self._nativeObject = None
        if nativeObject:
            self.fromNative(nativeObject)

    @abc.abstractmethod
    def toNative(self, *args, **kwargs):
        pass

    def fromNative(self, nativeObject, *args, **kwargs):
        pass

    @abc.abstractmethod
    def isValid(self):
        return False

    @abc.abstractmethod
    def name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def addAttribute(self, name, *args, **kwargs):
        pass

    @abc.abstractmethod
    def setAttribute(self, name, value, *args, **kwargs):
        pass

    @abc.abstractmethod
    def attribute(self, name, *args, **kwargs):
        pass