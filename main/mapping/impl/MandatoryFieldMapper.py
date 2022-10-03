#*
# * State machine based mapper for mandatory fields.
# * <p>
# * Mandatory means that corresponding field in the resulting object must be set.
# * However, in pure validation mode when there is no field to set in
# * resulting object, mandatory means that input value must be present and must be valid.
# * <p>
# * It is considered to be data error if mandatory field is absent in input
# * or has an invalid value (as per validator) or can't be translated.
# * Data error means that an exception will be raised.
# * <p>
# * If there is default value then it will be used if input field is missing,
# * invalid or causes translation error. However, warning message will still
# * be generated.
# * <p>
# * If either getter not defaulter are set - no way to obtain value to validate/translate/set.
# * This is treated as code error.
# * <p>
# * If we have a getter then there supposed to be either validator to check input value or
# * setter to propagate it to output. If there are none then the field should not be mandatory.
# * <p>
# * Absence means null.
# * <p>
# * OO - Original object type.
# * RO - Resulting object type.
# * P - Type of parameters object.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class MandatoryFieldMapper<OO, RO, P> extends AbstractStateMachineFieldMapper<OO, RO, P>
class MandatoryFieldMapper(AbstractStateMachineFieldMapper):
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @SuppressWarnings public MandatoryFieldMapper(Closure<MessageFormatter> messageFormatterFactory)
    def __init__(self, messageFormatterFactory):
        map = LinkedHashMap(1)
        map.put("mandatory", True)
        messageFormatter = messageFormatterFactory.call() if messageFormatterFactory.asBoolean() else SingleLineMesasgeFormatter(map)
        getter = Getter()
        validator = Validator()
        translator = Translator()
        defaulter = Defaulter()
        setter = Setter()
        end = End()
        getter.invokeMethod("configure", {validator, WarnIfDefinedOrDataErrorAnonymousInnerClass(self, defaulter, messageFormatter)
        , WarnIfDefinedOrDataErrorAnonymousInnerClass2(self, defaulter, messageFormatter)
        , defaulter

    class WarnIfDefinedOrDataErrorAnonymousInnerClass(WarnIfDefinedOrDataError):


        def __init__(self, outerInstance, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self._outerInstance = outerInstance
            self._messageFormatter = messageFormatter

        def createMessage(self, field, ctx, machine):
            return (str((self._messageFormatter.invokeMethod("formatMessage", [ctx, field, "Input value absent"]))))


    class WarnIfDefinedOrDataErrorAnonymousInnerClass2(WarnIfDefinedOrDataError):


        def __init__(self, outerInstance, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self._outerInstance = outerInstance
            self._messageFormatter = messageFormatter

        def createMessage(self, field, ctx, machine):
            return (str((self._messageFormatter.invokeMethod("formatMessage", [ctx, field, "Cannot obtain input value"]))))

#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
    );
    validator.invokeMethod("configure", {translator, WarnIfDefinedOrDataErrorAnonymousInnerClass3(defaulter, messageFormatter)
    , WarnIfDefinedOrDataErrorAnonymousInnerClass4(self, defaulter, messageFormatter)
    , translator
)
translator.invokeMethod("configure", {setter, CodeError("Translator returns null", messageFormatter), WarnIfDefinedOrDataErrorAnonymousInnerClass(self, defaulter, messageFormatter)
, setter
}
)
defaulter.invokeMethod("configure", [setter, CodeError("Defaulter returns null, this makes no sense", messageFormatter), CodeError("Defaulter throws exception", messageFormatter), CodeError("Should never see this as should get data error instead" + " by the means of " + String.invokeMethod("valueOf", []), messageFormatter)])
setter.invokeMethod("configure", [end, end, CodeError("Setter throws exception", messageFormatter), end])
self._stateMachine = ((getter))
}

#    *
#     * Creates new instance.
#     *
#     * @param messageFormatterFactory Factory for formatter of error messages or null
#     *                                if {@link SingleLineMesasgeFormatter} should be used.
#     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @SuppressWarnings public MandatoryFieldMapper()
public MandatoryFieldMapper()
    self(None)

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override protected State getStateMachine(@Nonnull Field<OO, RO, ?, ?, P> field)
protected State self.getStateMachine( Field<OO, RO, P> field)
    if (not field.getter) and not field.defaulter.asBoolean():
        raise IllegalStateException("Neither getter not defaulter are set" + " - no way to obtain value to validate/translate/set.")

    if field.getter and (not field.validator) and not field.setter.asBoolean():
        raise IllegalStateException("There is a getter but neither validator, nor setter" + " so we neither validate, nor propagate it - this makes no sense for mandatory field.")

    return self._stateMachine

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private final State stateMachine;
private final State self._stateMachine
}
