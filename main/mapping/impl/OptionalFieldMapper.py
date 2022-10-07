from typing import Callable, TypeVar, Any

#*
# * State machine based mapper for optional fields.
# * <p>
# * Optional means that corresponding field in the resulting object is optional and is not required to be set.
# * Optional field could be used in pure validation mode when there is no field to set in
# * resulting object to generate a warning if check on input value fails.
# * <p>
# * A warning will be generated if optional field
# * has an invalid value (as per validator) or can't be translated.
# * No exception will be raised and nothing will be injected into resulting object
# * unless default value is specified.
# * <p>
# * If there is default value then it will be used if input field is missing,
# * invalid or causes translation error.
# * <p>
# * Absence of optional field in input is not considered as an error and does not generate a warning.
# * <p>
# * Absence means null.
# * <p>
# * OO - Original object type.
# * RO - Resulting object type.
# * P - Type of parameters object.
# 


from .AbstractStateMachineFieldMapper import AbstractStateMachineFieldMapper
from .MessageFormatter import MessageFormatter
from .statemachine.Getter import Getter
from .statemachine.Validator import Validator
from .statemachine.Translator import Translator
from .statemachine.Defaulter import Defaulter
from .statemachine.Setter import Setter
from .statemachine.End import End
from .statemachine.Warn import Warn
from .SingleLineMesasgeFormatter import SingleLineMesasgeFormatter
from .statemachine.CodeError import CodeError
from .statemachine.State import State
from ..Field import Field
from ...IllegalStateException import IllegalStateException

OO = TypeVar('OO')
RO = TypeVar('RO')
P = TypeVar('P')

class OptionalFieldMapper(AbstractStateMachineFieldMapper[OO, RO, P]):

    def __init__(self):
        self.normalStateMachine: State = None
        self.ignoreInputFieldStateMachine: State = None
        self.ignoreOutputFieldStateMachine: State = None
    class WarnAnonymousInnerClass(Warn):

        def __init__(self, defaulter, messageFormatter, text):
            super().__init__(defaulter, messageFormatter)
            self.messageFormatter = messageFormatter
            self.text = text

        def createMessage(self, field, mappingContext, machineContext):
            return self.messageFormatter.formatMessage(mappingContext, field, self.text.format(**locals()))

    @staticmethod
    def createNormalStateMachine(messageFormatter: MessageFormatter) -> State:
        getter = Getter()
        validator = Validator()
        translator = Translator()
        defaulter: Defaulter = Defaulter()
        setter = Setter()
        end = End()
        getter.configure(validator,
                         defaulter,
                         OptionalFieldMapper.WarnAnonymousInnerClass(defaulter, messageFormatter, 'Cannot obtain input value'),
                         defaulter)

        validator.configure(translator,
                            OptionalFieldMapper.WarnAnonymousInnerClass(defaulter, messageFormatter,"Input value is invalid: '{machineContext.resultValue}'"),
                            OptionalFieldMapper.WarnAnonymousInnerClass(defaulter, messageFormatter,"Input value cannot be validated: '{machineContext.resultValue}'"),
                            translator)
        translator.configure(setter,
                             setter,
                             OptionalFieldMapper.WarnAnonymousInnerClass(defaulter,  messageFormatter,"Input value cannot be mapped: '{machineContext.resultValue}'"),
                             setter)
        defaulter.configure(setter,
                            CodeError("Defaulter returns null, this makes no sense", messageFormatter),
                            CodeError("Defaulter throws exception", messageFormatter),
                            end)
        setter.configure(end,
                         end,
                         CodeError("Setter throws exception", messageFormatter),
                         end)
        return getter

#    *
#     * Create state machine for the case when we just want to highlight that we ignore certain input field.
#     * <p>
#     * We're supposed to have a getter to show that we are aware of the field but nothing else
#     * to show we are ignoring it.
#     *
#     * @return State machine to be executed.
#     
    @staticmethod
    def createIgnoreInputFieldStateMachine() -> State:
        return End()

#    *
#     * Create state machine for the case when we just want to highlight that we ignore certain output field.
#     * <p>
#     * We're supposed to have a setter to show that we are aware of the field but nothing else
#     * to show we are ignoring it.
#     *
#     * @return State machine to be executed.
#     
    @staticmethod
    def createIgnoreOutputFieldStateMachine() -> State:
        return End()

#    *
#     * Creates new instance.
#     *
#     :param messageFormatterFactory: Factory for formatter of error messages or null
#     *                                if {@link SingleLineMesasgeFormatter} should be used.
#     


    def __init__(self, messageFormatterFactory: Callable[...,MessageFormatter]=None):
        messageFormatter:MessageFormatter = messageFormatterFactory() if messageFormatterFactory else SingleLineMesasgeFormatter(mandatory=False)
        self.normalStateMachine = OptionalFieldMapper.createNormalStateMachine(messageFormatter)
        self.ignoreInputFieldStateMachine = OptionalFieldMapper.createIgnoreInputFieldStateMachine()
        self.ignoreOutputFieldStateMachine = OptionalFieldMapper.createIgnoreOutputFieldStateMachine()
        assert self.normalStateMachine
        assert self.ignoreInputFieldStateMachine
        assert self.ignoreOutputFieldStateMachine



    def getStateMachine(self, field: Field[OO, RO, Any, Any, P]) -> State:
        assert field is not None
        if not field.getter and not field.setter:
            raise IllegalStateException("There are neither getter, nor setter. Can`t do anything with such field.")

        if field.getter and (not field.validator) and not field.setter:
            if field.defaulter or field.translator:
                raise IllegalStateException("There is getter but no validator or setter" + " this means we want to show we ignore certain input field." + " This means defaulter or translator make no sense because their result will be ignored")

            return self.ignoreInputFieldStateMachine

        if (not field.getter) and (not field.defaulter) and field.setter:
            return self.ignoreOutputFieldStateMachine

        return self.normalStateMachine
