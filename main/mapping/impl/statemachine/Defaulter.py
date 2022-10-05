# *
# * Obtains default value.
# 

from AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from MachineContext import MachineContext


class Defaulter(AbstractState):
    class ClosureAnonymousInnerClass:

        def __init__(self, outerInstance, field, mappingContext):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._field = field
            self._mappingContext = mappingContext

        def doCall(self, it):
            return self._outerInstance.callWithDelegate(self._field.defaulter, self._mappingContext)

        def doCall(self):
            return self.doCall(None)

    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        return self.safely(field, mappingContext, machineContext, True,
                           Defaulter.ClosureAnonymousInnerClass(self, field, mappingContext))

    def isDefined(self, field):
        return field.defaulter is not None
