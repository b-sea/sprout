.. _abstract:

###############
Abstract Module
###############

.. toctree::
    :maxdepth: 2

    abstractApp
    abstractScene
    abstractRender
    abstractObject
    abstractBase


The abstract module follows the `template design pattern <https://en.wikipedia.org/wiki/Template_method_pattern>`_.
This allows each client implementation to be defined separately, while each tool or extension interacts with the same
higher-level interface. In some (probably rare) cases, this can allow multiple clients to share tools or extensions.

This pattern is enforced by publicly exposing calls to be used by different clients, and then providing protected
methods for specific implementation. The main reason for this public/protected layering is to allow activity signals
to be emitted. Any extensions or tools can connect and use these signals to stay updated with the clients.

.. note::
    All of the protected template functions are abstract at this point. This means that to implement a new client, the
    entire abstract module should be integrated. This may change in the future depending on various needs.


.. rubric:: Template Pattern Example

.. code-block:: python

    class TemplateExample():
        CommandRequested = Signal() # Qt Signal
        CommandCompleted = Signal(bool) # Qt Signal - command pass/fail

        def _command(self, **kwargs):
            # This function must be implemented for the specific client.
            return True

        def command(self, **kwargs):
            self.CommandRequested.emit()
            result = self._command(**kwargs)
            self.CommandCompleted.emit(result)

    # Inside the client
    TemplateExample().command()



.. seealso::
    :ref:`signals`
