######
Events
######


.. _signals:

Signals
=======

.. _signals-builtin:

Built-in Signals
----------------

Facility comes pre-packaged with some global signals, stored in a singleton. These signals emit when various
:ref:`abstract` components and methods are invoked. Tools and expansions should use these

.. rubric:: Connecting to and emitting signals

.. code-block:: python

    from facility import events

    # Make a test function to connect to a signal. The signature of
    # this function must match the signature of the connected signal.
    def signalTest(value):
        print 'Heard a signal:', value

    # Connect the test function to the signal
    events.Signals().NewSceneFinished.connect(signalTest)

    # Emit the signal
    events.Signals().NewSceneFinished.emit(True)

    # Alternative way of connecting to a signal and emitting:
    #
    # events.Signals.NewSceneFinished.connect(appStartTest)
    # events.Signals.NewSceneFinished.emit(True)

Result::

    >>> ThreeDX: DEBUG:	Signal Emitted: NewSceneFinished()
    >>> Heard a signal: True


.. rubric:: Signal List

.. autoautosummary:: sprout.events.signals.Signals
    :attributes:


.. _signals-custom:

Custom Signals
--------------

The Facility signal objects are structured similar to a :class:`PySide.QtCore.Signal`. This allows for a familiar
interface when connecting events and their handlers.

Signals are a basic implementation of the `Observer Pattern <https://en.wikipedia.org/wiki/Observer_pattern>`_. Each
signal stores the args and types it is responsible to emit. It also keeps a list of functions connected to it and when
:func:`~facility.signals.Signal_.emit` is called, it iterates over each and executes the command with the supplied args.
There is some signature checking that takes place at run time to make sure the arguments supplied during
:func:`~facility.signals.Signal_.emit` matches the original argument list provided at initialization.

.. autoclass:: sprout.events.signals.Signal_