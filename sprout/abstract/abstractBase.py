import abc


class Base(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super(Base, self).__init__()
