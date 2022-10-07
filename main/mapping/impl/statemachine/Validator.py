#*
# * Validates result value.
# 

from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext
class Validator(AbstractState):

    class ClosureAnonymousInnerClass:

        def __init__(self, outerInstance, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
            super().__init__()
            self._outerInstance = outerInstance
            self._field = field
            self._mappingContext = mappingContext
            self._machineContext = machineContext

        def doCall(self, it):
            return self._outerInstance.callWithDelegate(self._field.validator, self._mappingContext, self._machineContext.resultValue)

        def doCall(self):
            return self.doCall(None)

    def process(self, field, mappingContext, machineContext):
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        return self.safely(field, mappingContext, machineContext, False, self.callWithDelegate(field.validator, mappingContext, machineContext.resultValue))



    def isDefined(self, field):
        return field.validator is not None

    def isNull(self, value):
        return bool(not value)

