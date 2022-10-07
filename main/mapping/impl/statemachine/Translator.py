#*
# * Translates result value.
# 
from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext
class Translator(AbstractState):

    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        return self.safely(field, mappingContext, machineContext, True, self.callWithDelegate(field.translator, mappingContext, machineContext.resultValue))


    def isDefined(self, field):
        return field.translator is not None

