"""
This class is the overall container for interacting with third-party clients.
This includes scene creation and destruction and GUI interactions.

This class will emit the following signals:

    - :attr:`~sprout.events.signals.Signals.NewSceneRequested`
    - :attr:`~sprout.events.signals.Signals.NewSceneFinished`
    - :attr:`~sprout.events.signals.Signals.OpenSceneRequested`
    - :attr:`~sprout.events.signals.Signals.OpenSceneFinished`

.. seealso::
    :ref:`signals-builtin`
"""


from abstractBase import *
from abstractScene import *
from sprout import events


class Application(Base):
    """

    """

    def __init__(self):
        super(Application, self).__init__()

        self.__menuItems = []
        events.Signals.ApplicationStart.emit()

    @abc.abstractmethod
    def _addMenuItem(self, menuName, itemName, function, **kwargs):
        """
        ``Protected Abstract Method`` Add a menu and menu item to an application

        Each custom implementation is responsible for making sure duplicate
        menus and menu items are not created.

        :param menuName: the menu label to add the item to
        :type menuName: str
        :param itemName: the label of the new menu item
        :type itemName: str
        :param function: the command to run when the menu item is activated
        :type function: callable
        :param kwargs: any additional arguments required per client
        :return: if the menu item was successfully added
        :rtype bool:
        """

        pass

    def addMenuItem(self, menuName, itemName, function, **kwargs):
        """
        The command called from any tool to add a menu and menu item to an application

        Signals emitted::

            sprout.Signals.MenuItemAdded

        :param menuName: the menu label to add the item to
        :type menuName: str
        :param itemName: the label of the new menu item
        :type itemName: str
        :param function: the command to run when the menu item is activated
        :type function: callable
        :param kwargs: any additional arguments required per client
        :return:
        """

        if self._addMenuItem(menuName, itemName, function, **kwargs):
            events.Signals.MenuItemAdded.emit(menuName, itemName)

    @abc.abstractmethod
    def currentScene(self):
        """
        ``Abstract Method`` Get the current open or active scene
        in the application.

        This function is expected to return a new instance of a
        :class:`~sprout.abstract.Scene` when called. By default, the
        scene will not be persisted.

        :return: The open or active scene
        :rtype: :class:`~sprout.abstract.Scene`
        """

        pass

    @abc.abstractmethod
    def _newScene(self, **kwargs):
        """
        ``Protected Abstract Method`` Template pattern new scene

        The custom implementation of what happens when an application calls
        for a new scene. This is where any "do you want to save?" dialogs
        should happen. The pass/fail returned by this function will be
        reflected in the final signal emitted when a new scene is created
        or is not created due to cancellation or failure.

        :param kwargs: any keywords required for the client
        :return: if the operation was successful
        :rtype: bool
        """

        pass

    def newScene(self, **kwargs):
        """
        The command called from the client to create a new scene

        Signals emitted::

            sprout.Signals.NewSceneRequested
            sprout.Signals.NewSceneFinished

        :param kwargs: any keywords required for the client
        :return:
        """

        events.Signals.NewSceneRequested.emit()
        result = self._newScene(**kwargs)
        events.Signals.NewSceneFinished.emit(result)

    @abc.abstractmethod
    def _openScene(self, **kwargs):
        """
        ``Protected Abstract Method`` Template pattern open scene

        The custom implementation of what happens when an application calls
        to open a scene. This method is responsible for getting the scene open.
        The pass/fail returned by this function will be reflected in the final
        signal emitted when a scene is opened or in case the scene was not opened
        due to cancellation or failure.

        :param kwargs: any keywords required for the client
        :return: if the operation was successful
        :rtype: bool
        """

        pass

    def openScene(self, **kwargs):
        """
        The command called from the client to open a scene

        Signals emitted::

            sprout.Signals.OpenSceneRequested
            sprout.Signals.OpenSceneFinished

        :param kwargs: any keywords required for the client
        :return:
        """

        events.Signals.OpenSceneRequested.emit()
        result = self._openScene(**kwargs)
        events.Signals.OpenSceneFinished.emit(result)

    @abc.abstractmethod
    def _quit(self, **kwargs):
        """
        ``Protected Abstract Method`` Template pattern quit application

        The custom implementation of what happens when an application calls
        to quit. This method is responsible for any final scene checks - such
        as saving modifications - as well as actually closing the client.

        This method (or it's client-level counterpart) will not emit any signals.

        :param kwargs: any keywords required for the client
        :return:
        """

        pass

    def quit(self, **kwargs):
        """
        The command called from the client to close the application

        :param kwargs: any keywords required for the client
        :return:
        """

        self._quit(**kwargs)
