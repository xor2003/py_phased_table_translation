#*
# * Translates result value.
# 
from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext
class Translator(AbstractState):

    class ClosureAnonymousInnerClass:

        def __init__(self, outerInstance, field, mappingContext, machineContext):
            super().__init__()
            self._outerInstance = outerInstance
            self._field = field
            self._mappingContext = mappingContext
            self._machineContext = machineContext

        def doCall(self, it):
            return self._outerInstance.callWithDelegate(self._field.translator, self._mappingContext,
                                                        self._machineContext.resultValue)

        def doCall(self):
            return self.doCall(None)

    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        return self.safely(field, mappingContext, machineContext, True, Translator.ClosureAnonymousInnerClass(self, field, mappingContext, machineContext))


    def isDefined(self, field):
        return field.translator is not None

