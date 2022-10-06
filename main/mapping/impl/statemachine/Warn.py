#*
# * Pushes a warning to log and then delegates to another step.
# 
from .AbstractState import AbstractState
from .State import State
from ..MessageFormatter import MessageFormatter
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext

import logging

logger=logging.getLogger(__name__)

class Warn(AbstractState):
    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        if machineContext.error:
            logger.warning(self.createMessage(field, mappingContext, machineContext) + machineContext.error)
        else:
            logger.warning(self.createMessage(field, mappingContext, machineContext))

        return self._delegate.process(field, mappingContext, machineContext)

    def isDefined(self, field: Field):
        return bool(self._delegate.isDefined(field))

    #    *
    #     * Creates instance.
    #     *
    #     * @param delegate Step to delegate to after logging.
    #     * @param mapper   Mapper used to log message.
    #     
    def __init__(self, delegate: State, messageFormatter: MessageFormatter):
        assert delegate
        assert messageFormatter
        self._delegate = delegate
        self._messageFormatter = messageFormatter

    #    *
    #     * Create message to be logged.
    #     *
    #     * @param field          Field configuration.
    #     * @param mappingContext Translation context.
    #     * @param machineContext State machine context.
    #     * @return Message to be logged.
    #     
    def createMessage(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        pass

