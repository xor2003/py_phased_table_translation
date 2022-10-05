# *
# * Base class for steps in state machine for a field translation.
# * <p>
# * Since steps reference each other and can hardly be created without
# * egg-chicken problem, {@link AbstractState#configure} should be used
# * to configure a state once it is created.
# 
# JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
# ORIGINAL LINE: @CompileStatic @SuppressWarnings("AbstractClassWithoutAbstractMethod") public abstract class AbstractState extends GroovyObjectSupport implements State
from abc import ABC
from collections.abc import Callable

from State import State
from main.IllegalStateException import IllegalStateException
from main.mapping.Field import Field
from main.mapping.MappingContext import MappingContext
from main.mapping.impl.statemachine.MachineContext import MachineContext


class AbstractState(ABC, State):

    def __init__(self):
        # instance fields found by Java to Python Converter:
        self.onException: State = None
        self.onNull: State = None
        self.onNonNull: State = None
        self.onUndefined: State = None

    #    *
    #     * Configures this step.
    #     *
    #     * @param onNonNull   Where to transition if current step returns not null.
    #     * @param onNull      Where to transition if current steps returns null.
    #     * @param onException Where to transition when exception happens during current step.
    #     * @param onUndefined Where to transition if current step is not configured.
    #     *                    Like when validator is not defined.
    #     
    # JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
    # ORIGINAL LINE: public void configure(@Nonnull State onNonNull, @Nonnull State onNull, @Nonnull State onException, @Nonnull State onUndefined)
    def configure(self, onNonNull: State, onNull: State, onException: State, onUndefined: State):
        assert onNonNull
        assert onNull
        assert onException
        assert onUndefined
        self.onException: State = onException
        self.onNull: State = onNull
        self.onNonNull: State = onNonNull
        self.onUndefined: State = onUndefined

    #    *
    #     * Is resulting value null?
    #     *
    #     * @param value Result of current step evaluation.
    #     * @return true if should transition to {@link AbstractState#onNull}.
    #     
    # JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
    # ORIGINAL LINE: protected boolean isNull(@Nullable Object value)
    def isNull(self, value=None):
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
    # JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
    # ORIGINAL LINE: @Nullable @SuppressWarnings("CatchThrowable") protected Object safely(@Nonnull Field field, @Nonnull MappingContext mappingContext, @Nonnull MachineContext machineContext, boolean propagate, @Nonnull Closure action)
    def safely(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext, propagate: bool,
               action: Callable):
        assert field
        assert mappingContext
        assert machineContext
        assert action
        if not self.isDefined(field):
            if self.onUndefined:
                return self.onUndefined.process(field, mappingContext, machineContext)

            raise IllegalStateException(f"{self} is undefined for {field} and onUndefined is not set")

        result = None
        try:
            result = action()
        except Exception as e:
            machineContext.error = e
            return self.onException.process(field, mappingContext, machineContext)

        if propagate:
            machineContext.resultValue = result

        if self.isNull(result):
            return self.onNull.process(field, mappingContext, machineContext)
        else:
            return self.onNonNull.process(field, mappingContext, machineContext)


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


    def callWithDelegate(self, closure, delegate, *args):
       #clonedClosure = closure.invokeMethod("clone", [])  TODO
       #clonedClosure.resolveStrategy = Closure.DELEGATE_FIRST
       #closure.delegate = delegate
       return closure(delegate, *args)

