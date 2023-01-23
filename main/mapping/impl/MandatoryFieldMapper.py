from typing import Callable, TypeVar, Any, Optional

from .AbstractStateMachineFieldMapper import AbstractStateMachineFieldMapper
from .MessageFormatter import MessageFormatter
from .SingleLineMesasgeFormatter import SingleLineMesasgeFormatter
from ...IllegalStateException import IllegalStateException
from ..Field import Field
from ..MappingContext import MappingContext
from .statemachine.CodeError import CodeError
from .statemachine.Defaulter import Defaulter
from .statemachine.End import End
from .statemachine.Getter import Getter
from .statemachine.MachineContext import MachineContext
from .statemachine.Setter import Setter
from .statemachine.State import State
from .statemachine.Translator import Translator
from .statemachine.Validator import Validator
from .statemachine.WarnIfDefinedOrDataError import WarnIfDefinedOrDataError

OO = TypeVar("OO")
RO = TypeVar("RO")
P = TypeVar("P")


class MandatoryFieldMapper(AbstractStateMachineFieldMapper[OO, RO, P]):
    """
    State machine based mapper for mandatory fields.

    Mandatory means that corresponding field in the resulting object must be set.
    However, in pure validation mode when there is no field to set in
    resulting object, mandatory means that input value must be present and must be valid.

    It is considered to be data error if mandatory field is absent in input
    or has an invalid value (as per validator) or can't be translated.
    Data error means that an exception will be raised.

    If there is default value then it will be used if input field is missing,
    invalid or causes translation error. However, warning message will still
    be generated.

    If either getter not defaulter are set - no way to obtain value to validate/translate/set.
    This is treated as code error.

    If we have a getter then there supposed to be either validator to check input value or
    setter to propagate it to output. If there are none then the field should not be mandatory.

    Absence means null.

    OO - Original object type.

    RO - Resulting object type.

    P - Type of parameters object.
    """

    class WarnIfDefinedOrDataError_InnerClass(WarnIfDefinedOrDataError):
        def __init__(self, defaulter, messageFormatter, text):
            super().__init__(defaulter, messageFormatter)
            self.messageFormatter = messageFormatter
            self.text = text

        def createMessage(
                self, field: Field, ctx: MappingContext, machine: MachineContext
        ):
            return self.messageFormatter.formatMessage(
                ctx, field, self.text.format(**locals())
            )

    def __init__(
        self, messageFormatterFactory: Optional[Callable[..., MessageFormatter]] = None
    ):
        messageFormatter: MessageFormatter = (
            messageFormatterFactory()
            if messageFormatterFactory
            else SingleLineMesasgeFormatter(mandatory=True)
        )
        """
        Creates new instance.

        :param messageFormatterFactory: Factory for formatter of error messages or null
                                         if {@link SingleLineMesasgeFormatter} should be used.
        """
        getter = Getter()
        validator = Validator()
        translator = Translator()
        defaulter = Defaulter()
        setter = Setter()
        end = End()

        getter.configure(
            validator,
            MandatoryFieldMapper.WarnIfDefinedOrDataError_InnerClass(
                defaulter, messageFormatter, "Input value absent"
            ),
            MandatoryFieldMapper.WarnIfDefinedOrDataError_InnerClass(
                defaulter, messageFormatter, "Cannot obtain input value"
            ),
            defaulter,
        )
        validator.configure(
            translator,
            MandatoryFieldMapper.WarnIfDefinedOrDataError_InnerClass(
                defaulter,
                messageFormatter,
                "Input value is invalid: '{machine.resultValue}'",
            ),
            MandatoryFieldMapper.WarnIfDefinedOrDataError_InnerClass(
                defaulter,
                messageFormatter,
                "Input value cannot be validated: '{machine.resultValue}'",
            ),
            translator,
        )
        translator.configure(
            setter,
            CodeError("Translator returns null", messageFormatter),
            MandatoryFieldMapper.WarnIfDefinedOrDataError_InnerClass(
                defaulter,
                messageFormatter,
                "Input value cannot be mapped: '{machine.resultValue}'",
            ),
            setter,
        )

        defaulter.configure(
            setter,
            CodeError("Defaulter returns null, this makes no sense", messageFormatter),
            CodeError("Defaulter throws exception", messageFormatter),
            CodeError(
                "Should never see this as should get data error instead"
                + " by the means of WarnIfDefinedOrDataError.simpleName",
                messageFormatter,
            ),
        )
        setter.configure(
            end, end, CodeError("Setter throws exception", messageFormatter), end
        )
        self.stateMachine = getter

    def getStateMachine(self, field: Field[OO, RO, Any, Any, P]) -> State:
        assert field is not None
        if not field.getter and not field.defaulter:
            raise IllegalStateException(
                "Neither getter not defaulter are set"
                + " - no way to obtain value to validate/translate/set."
            )

        if field.getter and not field.validator and not field.setter:
            raise IllegalStateException(
                "There is a getter but neither validator, nor setter"
                + " so we neither validate, nor propagate it - this makes no sense for mandatory field."
            )

        return self.stateMachine
