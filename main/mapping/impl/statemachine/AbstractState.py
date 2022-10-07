# *
# * Base class for steps in state machine for a field translation.
# * <p>
# * Since steps reference each other and can hardly be created without
# * egg-chicken problem, {@link AbstractState#configure} should be used
# * to configure a state once it is created.
# 


from abc import ABC
from collections.abc import Callable

from .State import State
from ....IllegalStateException import IllegalStateException
from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext


class AbstractState(State):

    def __init__(self):

        self.onException: State = None
        self.onNull: State = None
        self.onNonNull: State = None
        self.onUndefined: State = None

    '''
    #     * Configures this step.
    #     *
    #     :param onNonNull:   Where to transition if current step returns not null.
    #     :param onNull:      Where to transition if current steps returns null.
    #     :param onException: Where to transition when exception happens during current step.
    #     :param onUndefined: Where to transition if current step is not configured.
    #     *                    Like when validator is not defined.
    '''
    def configure(self, onNonNull: State, onNull: State, onException: State, onUndefined: State):
        assert onNonNull is not None
        assert onNull is not None
        assert onException is not None
        assert onUndefined is not None
        self.onException: State = onException
        self.onNull: State = onNull
        self.onNonNull: State = onNonNull
        self.onUndefined: State = onUndefined

    '''
    #     * Is resulting value null?
    #     *
    #     :param value: Result of current step evaluation.
    #     * @return true if should transition to {@link AbstractState#onNull}.
    '''
    def isNull(self, value=None):
        return value is None

    #    *
    #     * Perform an action.
    #     *
    #     :param field:          Field we're working on.
    #     :param mappingContext: Mapping context.
    #     :param machineContext: State of translation machine.
    #     :param propagate:      Should current step propagate it's result as input to next step?
    #     :param action:         Action to perform.
    #     * @return Result of calling next step on result returned by action.
    #     * If current step is not configured for a field as per {@link AbstractState#isDefined}
    #     * then next step is {@link AbstractState#onUndefined}.
    #     * In case of action throwing exception, next step will be {@link AbstractState#onException}.
    #     * If action returns null as per {@link AbstractState#isNull} then next step will be {@link AbstractState#onNull}.
    #     * Otherwise, next step is {@link AbstractState#onNonNull}.
    #     


    def safely(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext, propagate: bool,
               action: Callable):
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        # assert action
        if not self.isDefined(field):
            if self.onUndefined:
                return self.onUndefined.process(field, mappingContext, machineContext)

            raise IllegalStateException(f"{self} is undefined for {field.id} and onUndefined is not set")

        result = None
        try:
            print(f"{field.id} {action}")
            result = action(action.delegate, *action.args)
        except Exception as e:
            print(e)
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
        #     :param closure:  Closure to call.
        #     :param delegate: Delegate to use.
        #     :param args:     Closure parameters.
        #     * @return Whatever closure returns.
        #

    def callWithDelegate(self, closure, delegate, *args):
        # clonedClosure = closure.invokeMethod("clone", [])  TODO
        # clonedClosure.resolveStrategy = Closure.DELEGATE_FIRST
        if closure:
            assert delegate is not None
            closure.delegate = delegate
            if len(args) == 0:
                args = [None]
            closure.args = args
        return closure
