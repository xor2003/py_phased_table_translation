# pylint: disable=invalid-name
from .AbstractState import AbstractState


class Validator(AbstractState):
    """Validates result value."""

    def process(self, field, mappingContext, machineContext):
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        return self.safely(
            field,
            mappingContext,
            machineContext,
            False,
            self.callWithDelegate(
                field.validator, mappingContext, machineContext.resultValue
            ),
        )

    def isDefined(self, field):
        return field.validator is not None

    def isNull(self, value):
        return not value
