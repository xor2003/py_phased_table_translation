# *
# * Obtains default value.
# 

from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext


class Defaulter(AbstractState):
    class ClosureAnonymousInnerClass:

        def __init__(self, outerInstance, field, mappingContext):
            super().__init__()
            self._outerInstance = outerInstance
            self._field = field
            self._mappingContext = mappingContext

        def __call__(self, it):
            return self._outerInstance.callWithDelegate(self._field.defaulter, self._mappingContext)

        def doCall(self):
            return self.doCall()

    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        return self.safely(field, mappingContext, machineContext, True,
                           self.callWithDelegate(field.defaulter, mappingContext))

    def isDefined(self, field):
        return field.defaulter is not None
