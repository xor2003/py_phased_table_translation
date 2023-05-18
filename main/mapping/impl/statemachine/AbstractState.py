# pylint: disable=invalid-name
import logging
from collections.abc import Callable
from typing import Optional

from .MachineContext import MachineContext
from .State import State
from ...Field import Field
from ...MappingContext import MappingContext
from ....IllegalStateException import IllegalStateException

logger = logging.getLogger(__name__)


class Closure:
    """Helps to simulate Groovy's closure on Python."""

    def __init__(self, lambda_: Optional[Callable], delegate, *args):
        self.lambda_ = lambda_
        if lambda_:
            assert delegate is not None
            self.delegate = delegate
            if not args:
                args = (None,)
            self.args = args

    def __call__(self):
        return self.lambda_(self.delegate, *self.args)


class AbstractState(State):
    """Base class for steps in state machine for a field translation.

    Since steps reference each other and can hardly be created without
    egg-chicken problem, {@link AbstractState#configure} should be used
    to configure a state once it is created.
    """

    def configure(
            self, onNonNull: State, onNull: State, onException: State, onUndefined: State
    ):
        """Configures this step.

        :param onNonNull:   Where to transition if current step returns not null.
        :param onNull:      Where to transition if current steps returns null.
        :param onException: Where to transition when exception happens during current step.
        :param onUndefined: Where to transition if current step is not configured.
                                 Like when validator is not defined.
        """
        assert onNonNull is not None
        assert onNull is not None
        assert onException is not None
        assert onUndefined is not None
        self.onException = onException
        self.onNull = onNull
        self.onNonNull = onNonNull
        self.onUndefined = onUndefined

    def isNull(self, value):
        """Is resulting value null?.

        :param value: Result of current step evaluation.
        :return: true if should transition to {@link AbstractState#onNull}.
        """
        return value is None

    def safely(
            self,
            field: Field,
            mappingContext: MappingContext,
            machineContext: MachineContext,
            propagate: bool,
            action: Closure,
    ):
        """Perform an action.

        :param field:          Field we're working on.
        :param mappingContext: Mapping context.
        :param machineContext: State of translation machine.
        :param propagate:      Should current step propagate it's result as input to next step?
        :param action:         Action to perform.
        :return: Result of calling next step on result returned by action.
        If current step is not configured for a field as per {@link AbstractState#isDefined}
        then next step is {@link AbstractState#onUndefined}.
        In case of action throwing exception, next step will be {@link AbstractState#onException}.
        If action returns null as per {@link AbstractState#isNull} then next step will be {@link AbstractState#onNull}.
        Otherwise, next step is {@link AbstractState#onNonNull}.
        """
        assert field is not None
        assert mappingContext is not None
        assert machineContext is not None
        # assert action
        if not self.isDefined(field):
            if self.onUndefined:
                return self.onUndefined.process(field, mappingContext, machineContext)

            raise IllegalStateException(
                f"{self} is undefined for {field.id} and onUndefined is not set"
            )

        result = None
        try:
            logger.debug("Processing field %s", field.id)
            result = action()
        except Exception as e:
            logger.error(e)
            machineContext.error = e
            return self.onException.process(field, mappingContext, machineContext)

        if propagate:
            machineContext.resultValue = result

        if self.isNull(result):
            return self.onNull.process(field, mappingContext, machineContext)
        return self.onNonNull.process(field, mappingContext, machineContext)

    def callWithDelegate(self, closure: Optional[Callable], delegate, *args):
        """Calls closure with specified delegate.

        Creates closure clone so this method is safe to use in multithreaded environment.

        :param closure:  Closure to call.
        :param delegate: Delegate to use.
        :param args:     Closure parameters.
        :return: Whatever closure returns.
        """
        return Closure(closure, delegate, *args)
