#*
# * Represents code error.
# * Does not need to be configured.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class CodeError extends AbstractState
class CodeError(AbstractState):
    #    *
    #     * Creates new instance.
    #     *
    #     * @param errorDescription Explanation of error.
    #     * @param messageFormatter Formatter of error message.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public CodeError(@Nonnull String errorDescription, @Nonnull MessageFormatter messageFormatter)
    def __init__(self, errorDescription, messageFormatter):
        #instance fields found by Java to Python Converter:
        self._errorDescription = None
        self._messageFormatter = None

        assert errorDescription
        assert messageFormatter
        self._errorDescription = errorDescription
        self._messageFormatter = messageFormatter

    def process(self, field, mappingContext, machineContext):
        raise IllegalStateException(self._messageFormatter.invokeMethod("formatMessage", [mappingContext, field, self._errorDescription]), machineContext.error)

    def isDefined(self, field):
        return True

