#*
# * Pushes a warning to log and then delegates to another step.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Log4j2 @CompileStatic public abstract class Warn extends AbstractState
class Warn(AbstractState):
    def process(self, field, mappingContext, machineContext):
        if machineContext.error.asBoolean():
            log.invokeMethod("warn", [self.createMessage(field, mappingContext, machineContext), machineContext.error])
        else:
            log.invokeMethod("warn", [self.createMessage(field, mappingContext, machineContext)])

        return ((self._delegate.invokeMethod("process", [field, mappingContext, machineContext])))

    def isDefined(self, field):
        return (bool((self._delegate.invokeMethod("isDefined", [field]))))

    #    *
    #     * Creates instance.
    #     *
    #     * @param delegate Step to delegate to after logging.
    #     * @param mapper   Mapper used to log message.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: protected Warn(@Nonnull State delegate, @Nonnull MessageFormatter messageFormatter)
    def __init__(self, delegate, messageFormatter):
        #instance fields found by Java to Python Converter:
        self._delegate = None
        self._messageFormatter = None

        assert delegate
        assert messageFormatter
        self._delegate = delegate
        self._messageFormatter = messageFormatter

    #    *
    #     * Create message to be logged.
    #     *
    #     * @param field          Field configuration.
    #     * @param mappingContext Translation context.
    #     * @param machineContext State machine context.
    #     * @return Message to be logged.
    #     
    def createMessage(self, field, mappingContext, machineContext):
        pass

