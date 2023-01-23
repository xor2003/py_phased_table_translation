from .AbstractState import AbstractState
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext


class Getter(AbstractState):
    """
    Extracts input value.
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
                field.getter, mappingContext, mappingContext.originalObject
            ),
        )

    def isDefined(self, field: Field):
        return field.getter is not None
