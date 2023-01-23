from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext


class Setter(AbstractState):
    """
    Pushes result value to setter.
    """

    def process(
            self,
            field: Field,
            mappingContext: MappingContext,
            machineContext: MachineContext,
    ):
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        return self.safely(
            field,
            mappingContext,
            machineContext,
            True,
            self.callWithDelegate(
                field.setter, mappingContext, machineContext.resultValue
            ),
        )

    def isDefined(self, field):
        return field.setter is not None
