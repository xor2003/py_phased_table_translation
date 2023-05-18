# pylint: disable=invalid-name
from .AbstractState import AbstractState
from .MachineContext import MachineContext
from ..MessageFormatter import MessageFormatter
from ...Field import Field
from ...MappingContext import MappingContext
from ....IllegalStateException import IllegalStateException


class CodeError(AbstractState):
    """Represents code error.
    Does not need to be configured.
    """

    def __init__(self, errorDescription: str, messageFormatter: MessageFormatter):
        """Creates new instance.

        :param errorDescription: Explanation of error.
        :param messageFormatter: Formatter of error message.
        """
        super().__init__()
        assert errorDescription is not None
        assert messageFormatter is not None
        self.errorDescription = errorDescription.format(**locals())
        self.messageFormatter = messageFormatter

    def process(
        self,
        field: Field,
        mappingContext: MappingContext,
        machineContext: MachineContext,
    ):
        raise IllegalStateException(
            machineContext.error,
            self.messageFormatter.formatMessage(
                mappingContext, field, self.errorDescription
            ),
        )

    def isDefined(self, field: Field):
        return True
