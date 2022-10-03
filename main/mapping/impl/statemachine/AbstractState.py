#*
# * Base class for steps in state machine for a field translation.
# * <p>
# * Since steps reference each other and can hardly be created without
# * egg-chicken problem, {@link AbstractState#configure} should be used
# * to configure a state once it is created.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic @SuppressWarnings("AbstractClassWithoutAbstractMethod") public abstract class AbstractState extends GroovyObjectSupport implements State
class AbstractState(GroovyObjectSupport, State):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._onException = None
        self._onNull = None
        self._onNonNull = None
        self._onUndefined = None

    #    *
    #     * Configures this step.
    #     *
    #     * @param onNonNull   Where to transition if current step returns not null.
    #     * @param onNull      Where to transition if current steps returns null.
    #     * @param onException Where to transition when exception happens during current step.
    #     * @param onUndefined Where to transition if current step is not configured.
    #     *                    Like when validator is not defined.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public void configure(@Nonnull State onNonNull, @Nonnull State onNull, @Nonnull State onException, @Nonnull State onUndefined)
    def configure(self, onNonNull, onNull, onException, onUndefined):
        assert onNonNull
        assert onNull
        assert onException
        assert onUndefined
        self._onException = onException
        self._onNull = onNull
        self._onNonNull = onNonNull
        self._onUndefined = onUndefined

    #    *
    #     * Is resulting value null?
    #     *
    #     * @param value Result of current step evaluation.
    #     * @return true if should transition to {@link AbstractState#onNull}.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: protected boolean isNull(@Nullable Object value)
    def isNull(self, value):
        return value is None

    #    *
    #     * Perform an action.
    #     *
    #     * @param field          Field we're working on.
    #     * @param mappingContext Mapping context.
    #     * @param machineContext State of translation machine.
    #     * @param propagate      Should current step propagate it's result as input to next step?
    #     * @param action         Action to perform.
    #     * @return Result of calling next step on result returned by action.
    #     * If current step is not configured for a field as per {@link AbstractState#isDefined}
    #     * then next step is {@link AbstractState#onUndefined}.
    #     * In case of action throwing exception, next step will be {@link AbstractState#onException}.
    #     * If action returns null as per {@link AbstractState#isNull} then next step will be {@link AbstractState#onNull}.
    #     * Otherwise, next step is {@link AbstractState#onNonNull}.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nullable @SuppressWarnings("CatchThrowable") protected Object safely(@Nonnull Field field, @Nonnull MappingContext mappingContext, @Nonnull MachineContext machineContext, boolean propagate, @Nonnull Closure action)
    def safely(self, field, mappingContext, machineContext, propagate, action):
        if not invokeMethod("isDefined", [field]).asBoolean():
            if self._onUndefined is not None.asBoolean():
                return ((self._onUndefined.invokeMethod("process", [field, mappingContext, machineContext])))

            raise IllegalStateException(self + " is undefined for " + String.invokeMethod("valueOf", [field]) + " and onUndefined is not set")

        result = None
        try:
            result = ((action.call()))
        except Throwable as e:
            machineContext.error = e
            return ((self._onException.invokeMethod("process", [field, mappingContext, machineContext])))

        if propagate:
            machineContext.resultValue = result

        if self.isNull(result):
            return ((self._onNull.invokeMethod("process", [field, mappingContext, machineContext])))
        else:
            return ((self._onNonNull.invokeMethod("process", [field, mappingContext, machineContext])))


    #    *
    #     * Calls closure with specified delegate.
    #     * <p>
    #     * Creates closure clone so this method is safe to use in multithreaded environment.
    #     *
    #     * @param closure  Closure to call.
    #     * @param delegate Delegate to use.
    #     * @param args     Closure parameters.
    #     * @return Whatever closure returns.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: protected <T> T callWithDelegate(@Nonnull Closure<T> closure, @Nonnull Object delegate, @Nonnull Object... args)
     def callWithDelegate(self, closure, delegate, *args):
        clonedClosure = closure.invokeMethod("clone", [])
        clonedClosure.resolveStrategy = Closure.DELEGATE_FIRST
        clonedClosure.delegate = delegate
        return ((clonedClosure.invokeMethod("call", [None]) if args is None.asBoolean() else clonedClosure.invokeMethod("call", []) if len(args) == 0.asBoolean() else clonedClosure.invokeMethod("call", [args[0]]) if len(args) == 1.asBoolean() else clonedClosure.invokeMethod("call", [args])))

