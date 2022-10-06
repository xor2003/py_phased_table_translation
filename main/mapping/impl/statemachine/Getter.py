#*
# * Extracts input value.
# 
from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext
class Getter(AbstractState):
    class ClosureAnonymousInnerClass:

        def __init__(self, _lambda, *args):
            self._lambda = _lambda
            self.args = args

        def __call__(self):
            return self._outerInstance.callWithDelegate(self._lambda, self._mappingContext)

        def doCall(self):
            return self.doCall(None)
    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        return self.safely(field, mappingContext, machineContext, True,
                           self.callWithDelegate(field.getter, mappingContext, mappingContext.originalObject))

    def isDefined(self, field: Field):
        return field.getter is not None

