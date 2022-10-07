#*
# * Represents code error.
# * Does not need to be configured.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class CodeError extends AbstractState
from .AbstractState import AbstractState
from ....IllegalStateException import IllegalStateException
from .MachineContext import MachineContext
from ..MessageFormatter import MessageFormatter
from ...Field import Field
from ...MappingContext import MappingContext


class CodeError(AbstractState):
    #    *
    #     * Creates new instance.
    #     *
    #     * @param errorDescription Explanation of error.
    #     * @param messageFormatter Formatter of error message.
    #     

    def __init__(self, errorDescription: str, messageFormatter: MessageFormatter):
        assert errorDescription is not None
        assert messageFormatter is not None
        self.errorDescription = errorDescription.format(**locals())
        self.messageFormatter = messageFormatter

    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        raise IllegalStateException(self.messageFormatter.formatMessage(mappingContext, field, self.errorDescription), machineContext.error)

    def isDefined(self, field: Field):
        return True

