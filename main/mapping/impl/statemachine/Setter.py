#*
# * Pushes result value to setter.
# 
from AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from MachineContext import MachineContext
class Setter(AbstractState):
    class ClosureAnonymousInnerClass:

        def __init__(self, outerInstance, field, mappingContext, machineContext):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._field = field
            self._mappingContext = mappingContext
            self._machineContext = machineContext

        def doCall(self, it):
            return self._outerInstance.callWithDelegate(self._field.setter, self._mappingContext, self._machineContext.resultValue)

        def doCall(self):
            return self.doCall(None)

    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        return self.safely(field, mappingContext, machineContext, True,
                           Setter.ClosureAnonymousInnerClass(self, field, mappingContext, machineContext))

    def isDefined(self, field):
        return field.setter is not None

