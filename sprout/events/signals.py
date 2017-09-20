"""

"""
# test test
import inspect

from sprout import classes


class Signal_(object):
    """

    """

    def __init__(self, *args):
        """

        :param args: the signature that will be emitted from this signal
        """

        # Use inspect to try to figure out what this signal is called.
        # This name will be reflected in logs for emissions.
        # If this fails, just fall back to logging the class name.
        try:
            name = inspect.stack()[1][4][0].strip()
            name = name.split(self.__class__.__name__)[0]
            name = name.split('.')[-1]
            name = name.split('=')[0]
            self._name = name.strip()

        except:
            self._name = self.__class__.__name__

        self._connected = []
        self._args = args

    def connect(self, function):
        """
        .

        The signature of any function passed to connect should match the
        signature given when constructing the signal.

        :param function: the command to run when the signal is emitted
        :type function: callable
        :return:
        """

        self._connected.append(function)

    def disconnect(self, function):
        """

        :param function: the command to remove from this signal
        :type function: callable
        :return:
        """

        if function not in self._connected:
            return

        self._connected.remove(function)

    def emit(self, *args):
        """
        .
        The arguments provided need to match the arguments provided
        when this signal was initialized.

        :param args: the values to send all connected functions
        :return:
        """

        import sprout

        # Match the args provided to the ones set when this class was created
        if len(args) != len(self._args):
            raise ValueError('%s takes %s arguments, %s provided' %
                             (self._name, len(self._args), len(args)))
            return

        for i in range(len(self._args)):
            if isinstance(args[i], self._args[i]):
                continue

            raise ValueError('%s parameter %s must be a %s, %s provided' %
                             (self._name, i, self._args[i], type(args[i])))
            return

        sigArgs = [str(x) for x in args]
        sprout.LOG.debug('Signal Emitted: %s(%s)' % (self._name, ', '.join(sigArgs)))

        for c in self._connected:
            c(*args)


class Signals(object):
    """
    Singleton class to access all signals available for sprout
    """

    __metaclass__ = classes.MetaSingleton

    ApplicationStart = Signal_()
    """
    Emitted when :class:`~sprout.abstract.abstractApplication.Application` is created
    """

    MenuItemAdded = Signal_(str, str)
    """
    Emits the ``menu`` and ``menuItem`` when :class:`~sprout.abstract.abstractApplication.Application.addMenuItem` is called
    """

    NewSceneRequested = Signal_()
    """
    Emitted when :func:`~sprout.abstract.abstractApplication.Application.newScene` is called
    """

    NewSceneFinished = Signal_(bool)
    """
    Emits a success/fail ``bool`` after a client creates a new scene
    """

    OpenSceneRequested = Signal_()
    """
    Emitted when :func:`~sprout.abstract.abstractApplication.Application.openScene` is called
    """

    OpenSceneFinished = Signal_(bool)
    """
    Emits a success/fail ``bool`` after a client opens a scene
    """

    SaveSceneRequested = Signal_()
    """
    Emitted when :func:`~sprout.abstract.abstractScene.Scene.save` is called
    """

    SaveSceneFinished = Signal_(bool)
    """
    Emits a success/fail ``bool`` after a client saves a scene
    """

    SaveSceneAsRequested = Signal_()
    """
    Emitted when :func:`~sprout.abstract.abstractScene.Scene.saveAs` is called
    """

    SaveSceneAsFinished = Signal_(bool)
    """
    Emits a success/fail ``bool`` after a client creates saves a copy of a scene
    """

    PublishSceneRequested = Signal_()
    """
    Emitted when :func:`~sprout.abstract.abstractScene.Scene.publish` is called
    """

    PublishSceneFinished = Signal_(bool)
    """
    Emits a success/fail ``bool`` after a client publishes a scene
    """

    CloseSceneRequested = Signal_()
    """
    Emitted when :func:`~sprout.abstract.abstractScene.Scene.close` is called
    """

    CloseSceneFinished = Signal_(bool)
    """
    Emits a success/fail ``bool`` after a client closes a scene
    """
