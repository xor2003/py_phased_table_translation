#*
# * State in field translation state machine.
#
from abc import abstractmethod, ABC

from ...Field import Field
from ...MappingContext import MappingContext
from .MachineContext import MachineContext


class State(ABC):
    #    *
    #     * Is current step configured in field configuration?
    #     *
    #     :param field: Field configuration.
    #     * @return true if current step is configured for a field.
    #     
    @abstractmethod
    def isDefined(self, field: Field):
        pass

    #    *

    #     * Do the work related to the step.
    #     *
    #     :param field:          Definition of the field.
    #     :param mappingContext: Mapping context.
    #     :param machineContext: State machine context.
    #     * @return Result of current step evaluation.
    #     

    @abstractmethod
    def process(self, field: Field, mappingContext: MappingContext, machineContext: MachineContext):
        pass
