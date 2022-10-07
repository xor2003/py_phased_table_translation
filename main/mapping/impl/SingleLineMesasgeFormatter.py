# *
# * Message formatter that puts all information on single line.
# * <p>
# * Information that is added:
# * <ul>
# *     <li>type of field: optional/mandatory</li>
# *     <li>input object</li>
# *     <li>mapping parameters</li>
# *     <li>field identifier</li>
# *     <li>provided message</li>
# * </ul>
#
from typing import Any, TypeVar, Generic

from .MessageFormatter import MessageFormatter
from ..Field import Field
from ..MappingContext import MappingContext

OO = TypeVar('OO')
RO = TypeVar('RO')
P = TypeVar('P')

class SingleLineMesasgeFormatter(MessageFormatter):

    def __init__(self, mandatory: bool = False):
        self.mandatory: bool = mandatory


    def formatMessage(self, mappingContext: MappingContext[Any, Any, Any], field: Field[Any, Any, Any, Any, Any],
                      message: str) -> str:
        assert field
        assert mappingContext
        assert message
        optionality = "mandatory" if self.mandatory else "optional"
        return f"{message} for {optionality} field {field.id}. " + f"On: ~~~>{mappingContext.originalObject}<~~~" + f" Parameters: {mappingContext.parameters}."
