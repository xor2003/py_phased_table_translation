# pylint: disable=invalid-name
from .AbstractState import AbstractState
from .MachineContext import MachineContext
from ...Field import Field
from ...MappingContext import MappingContext


class End(AbstractState):
    """Ends processing.
    Does not need to be configured.
    """

    def process(
            self,
            field: Field,
            mappingContext: MappingContext,
            machineContext: MachineContext,
    ):
        assert machineContext is not None
        return machineContext.resultValue

    def isDefined(self, field: Field):
        return True
