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
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class OptionalFieldMapper<OO, RO, P> extends AbstractStateMachineFieldMapper<OO, RO, P>
class OptionalFieldMapper(AbstractStateMachineFieldMapper):
    @staticmethod
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @SuppressWarnings("MethodSize") private static State createNormalStateMachine(final MessageFormatter messageFormatter)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def _createNormalStateMachine(messageFormatter):
        getter = Getter()
        validator = Validator()
        translator = Translator()
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Defaulter defaulter = new Defaulter();
        defaulter = Defaulter()
        setter = Setter()
        end = End()
        getter.invokeMethod("configure", {validator, defaulter, WarnAnonymousInnerClass(defaulter, messageFormatter)
        , defaulter

    class WarnAnonymousInnerClass(Warn):

        def __init__(self, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self._messageFormatter = messageFormatter

        def createMessage(self, field, mappingContext, machineContext):
            return (str((self._messageFormatter.invokeMethod("formatMessage", [mappingContext, field, "Cannot obtain input value"]))))

#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
    );
    validator.invokeMethod("configure", {translator, WarnAnonymousInnerClass2(defaulter, messageFormatter)
    , WarnAnonymousInnerClass3(self, defaulter, messageFormatter)
    , translator
)
translator.invokeMethod("configure", {setter, setter, WarnAnonymousInnerClass(self, defaulter, messageFormatter)
, setter
}
)
defaulter.invokeMethod("configure", [setter, CodeError("Defaulter returns null, this makes no sense", messageFormatter), CodeError("Defaulter throws exception", messageFormatter), end])
setter.invokeMethod("configure", [end, end, CodeError("Setter throws exception", messageFormatter), end])
return ((getter))
}

#    *
#     * Create state machine for the case when we just want to highlight that we ignore certain input field.
#     * <p>
#     * We're supposed to have a getter to show that we are aware of the field but nothing else
#     * to show we are ignoring it.
#     *
#     * @return State machine to be executed.
#     
private static State com.hpe.amce.mapping.impl._createIgnoreInputFieldStateMachine()
    return ((End()))

#    *
#     * Create state machine for the case when we just want to highlight that we ignore certain output field.
#     * <p>
#     * We're supposed to have a setter to show that we are aware of the field but nothing else
#     * to show we are ignoring it.
#     *
#     * @return State machine to be executed.
#     
private static State com.hpe.amce.mapping.impl._createIgnoreOutputFieldStateMachine()
    return ((End()))

#    *
#     * Creates new instance.
#     *
#     * @param messageFormatterFactory Factory for formatter of error messages or null
#     *                                if {@link SingleLineMesasgeFormatter} should be used.
#     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @SuppressWarnings public OptionalFieldMapper(Closure<MessageFormatter> messageFormatterFactory)
public OptionalFieldMapper(Closure<MessageFormatter> messageFormatterFactory)
    map = LinkedHashMap(1)
    map.put("mandatory", False)
    messageFormatter = messageFormatterFactory.call() if messageFormatterFactory.asBoolean() else SingleLineMesasgeFormatter(map)
    self._normalStateMachine = createNormalStateMachine(messageFormatter)
    self._ignoreInputFieldStateMachine = com.hpe.amce.mapping.impl._createIgnoreInputFieldStateMachine()
    self._ignoreOutputFieldStateMachine = com.hpe.amce.mapping.impl._createIgnoreOutputFieldStateMachine()

#    *
#     * Creates new instance.
#     *
#     * @param messageFormatterFactory Factory for formatter of error messages or null
#     *                                if {@link SingleLineMesasgeFormatter} should be used.
#     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @SuppressWarnings public OptionalFieldMapper()
public OptionalFieldMapper()
    self(None)

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override protected State getStateMachine(@Nonnull Field<OO, RO, ?, ?, P> field)
protected State self.getStateMachine( Field<OO, RO, P> field)
    if (not field.getter) and not field.setter.asBoolean():
        raise IllegalStateException("There are neither getter, nor setter. Can`t do anything with such field.")

    if field.getter and (not field.validator) and not field.setter.asBoolean():
        if field.defaulter or field.translator.asBoolean():
            raise IllegalStateException("There is getter but no validator or setter" + " this means we want to show we ignore certain input field." + " This means defaulter or translator make no sense because their result will be ignored")

        return self._ignoreInputFieldStateMachine

    if (not field.getter) and (not field.defaulter) and field.setter.asBoolean():
        return self._ignoreOutputFieldStateMachine

    return self._normalStateMachine

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private final State normalStateMachine;
private final State self._normalStateMachine
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private final State ignoreInputFieldStateMachine;
private final State self._ignoreInputFieldStateMachine
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private final State ignoreOutputFieldStateMachine;
private final State self._ignoreOutputFieldStateMachine
}
