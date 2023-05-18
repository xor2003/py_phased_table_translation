# pylint: disable=invalid-name
from .AbstractState import AbstractState
from .MachineContext import MachineContext
from ...Field import Field
from ...MappingContext import MappingContext


class Defaulter(AbstractState):
    """Obtains default value."""

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
            self.callWithDelegate(field.defaulter, mappingContext),
        )

    def isDefined(self, field):
        return field.defaulter is not None
