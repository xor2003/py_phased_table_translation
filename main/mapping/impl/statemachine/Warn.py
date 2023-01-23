from .AbstractState import AbstractState
from .State import State
from ..MessageFormatter import MessageFormatter
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext

import logging

logger = logging.getLogger(__name__)


class Warn(AbstractState):
    """
    Pushes a warning to log and then delegates to another step.
    """

    def process(
            self,
            field: Field,
            mappingContext: MappingContext,
            machineContext: MachineContext,
    ):
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        if machineContext.error:
            logger.warning(
                "%s %s",
                self.createMessage(field, mappingContext, machineContext),
                machineContext.error,
            )
        else:
            logger.warning(
                "%s", self.createMessage(field, mappingContext, machineContext)
            )

        return self._delegate.process(field, mappingContext, machineContext)

    def isDefined(self, field: Field):
        return bool(self._delegate.isDefined(field))

    def __init__(self, delegate: State, messageFormatter: MessageFormatter):
        """
        Creates instance.

        :param delegate: Step to delegate to after logging.
        """
        super().__init__()
        assert delegate is not None
        assert messageFormatter is not None
        self._delegate = delegate
        self._messageFormatter = messageFormatter

    def createMessage(
            self,
            field: Field,
            mappingContext: MappingContext,
            machineContext: MachineContext,
    ):
        """
        Create message to be logged.

        :param field:          Field configuration.
        :param mappingContext: Translation context.
        :param machineContext: State machine context.
        :return: Message to be logged.
        """
        pass
