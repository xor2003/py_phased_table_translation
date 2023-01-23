from .Warn import Warn


class IllegalArgumentException(ValueError):
    pass


class WarnIfDefinedOrDataError(Warn):
    """
    Warn if next step is defined, throw otherwise.

    If next (delegate) step is configured then works like {@link Warn}.
    If next step is not defined then instead it throws data error with the same message
    as would be logged.
    """

    def __init__(self, delegate, messageFactory):
        """
        Creates instance.

        :param delegate: Step to delegate to after logging.
        """
        super().__init__(delegate, messageFactory)

    def process(self, field, mappingContext, machineContext):
        if not self.isDefined(field):
            raise IllegalArgumentException(
                self.createMessage(field, mappingContext, machineContext),
                machineContext.error,
            )

        return super().process(field, mappingContext, machineContext)
