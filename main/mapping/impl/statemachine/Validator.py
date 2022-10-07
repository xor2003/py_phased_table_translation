#*
# * Validates result value.
# 

from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext
class Validator(AbstractState):

    def process(self, field, mappingContext, machineContext):
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        return self.safely(field, mappingContext, machineContext, False, self.callWithDelegate(field.validator, mappingContext, machineContext.resultValue))



    def isDefined(self, field):
        return field.validator is not None

    def isNull(self, value):
        return bool(not value)

