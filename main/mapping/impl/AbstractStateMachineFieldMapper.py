from typing import TypeVar, Any
from abc import ABC, abstractmethod

from .statemachine.MachineContext import MachineContext
from .. import Field, MappingContext
from ..FieldMapper import FieldMapper
from ...IllegalStateException import IllegalStateException

#*
# * Field mapper based on state machine.
# * <p>
# * Child classes should define their state machine using {@link AbstractStateMachineFieldMapper#getStateMachine()}.
# * <p>
# * This base class will check for incorrect configuration combinations:
# * <ul>
# * <li>If there is no setter then defaulter and translation are useless and should not be set.</li>
# * <li>If there is no getter then it's pointless to set
# *      validator or translator because they won't be called anyway.</li>
# * </ul>
# * <p>
# * OO - Original object type.
# * RO - Resulting object type.
# * P - Type of parameters object.
#
OO = TypeVar('OO')
RO = TypeVar('RO')
P = TypeVar('P')

class AbstractStateMachineFieldMapper(ABC, FieldMapper[OO, RO, P]):

    def mapField(self, field: Field[OO, RO, Any, Any, P], mappingContext: MappingContext[OO, RO, P]):
        if (not field.setter) and (field.defaulter or field.translator):
            raise IllegalStateException("Since there is no setter, defaulter and translator make no sense" + " as their result will be ignored.")

        if (not field.getter) and (field.validator or field.translator):
            raise IllegalStateException("If there is no getter then it's pointless to set " + "validator or translator because they won't be called anyway.")

        if mappingContext is None:
            raise IllegalStateException("Translation context must be set")

        if field is None:
            raise IllegalStateException("Field descriptor must be set")

        self.getStateMachine(field).invokeMethod("process", [field, mappingContext, MachineContext()])

    #    *
    #     * Gets state machine for this field mapper.
    #     *
    #     * @param field Field to be translated.
    #     * @return Starting state of state machine.
    #     
    @abstractmethod
    def getStateMachine(self, field: Field[OO, RO, Any, Any, P]):
        pass
