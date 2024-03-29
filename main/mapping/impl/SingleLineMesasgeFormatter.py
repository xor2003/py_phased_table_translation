# pylint: disable=invalid-name
from typing import Any

from .MessageFormatter import MessageFormatter
from ..Field import Field
from ..MappingContext import MappingContext


class SingleLineMesasgeFormatter(MessageFormatter):
    """Message formatter that puts all information on single line.

    Information that is added:
    <ul>
        <li>type of field: optional/mandatory</li>
        <li>input object</li>
        <li>mapping parameters</li>
        <li>field identifier</li>
        <li>provided message</li>
    </ul>
    """

    def __init__(self, mandatory: bool = False):
        """:param mandatory: Indicates if the field is mandatory."""
        self.mandatory: bool = mandatory

    def formatMessage(
            self,
            mappingContext: MappingContext[Any, Any, Any],
            field: Field[Any, Any, Any, Any, Any],
            message: str,
    ) -> str:
        assert field is not None
        assert mappingContext is not None
        assert message is not None
        optionality = "mandatory" if self.mandatory else "optional"
        return (
            f"{message} for {optionality} field {field.id}. "
            + f"On: ~~~>{mappingContext.originalObject}<~~~"
            + f" Parameters: {mappingContext.parameters}."
        )
