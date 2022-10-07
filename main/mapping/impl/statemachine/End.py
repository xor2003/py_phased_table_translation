#*
# * Ends processing.
# * Does not need to be configured.
# 

from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext

class End(AbstractState):
    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        assert machineContext is not None
        return machineContext.resultValue

    def isDefined(self, field: Field):
        return True

