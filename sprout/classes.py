class MetaSingleton(type):
    """
    Singleton metaclass
    """
    def __init__(cls, name, bases, dict):
        super(MetaSingleton, cls).__init__(name, bases, dict)
        cls.__instance__ = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance__


class Singleton(object):
    def __init__(self):
        globals()[self.__class__.__name__] = self
        print globals()[self.__class__.__name__]

    def __call__(cls):
        print cls.__class__.__name__ in globals()
        print 'call'
        return '  ', globals()[cls.__class__.__name__]


class MetaConstant(type):
    """
    Low-level meta class that will mark
    all attributes read only.
    """

    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise ValueError('Property is read-only.')


class Enum(object):
    """
    Enum class. Once the class is declared,
    the properties become read only.
    """

    __metaclass__ = MetaConstant

    @classmethod
    def hash(cls):
        hDict = {}

        for a in cls.__dict__:
            if a.startswith('__') and a.endswith('__'):
                continue
            hDict[a] = cls.__dict__[a]

        return hDict

    @classmethod
    def hashKeys(cls):
        return cls.hash().keys()

    @classmethod
    def hashValues(cls):
        return cls.hash().values()
