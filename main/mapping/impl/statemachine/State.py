#*
# * State in field translation state machine.
# 
class State(GroovyObjectSupport):
    #    *
    #     * Is current step configured in field configuration?
    #     *
    #     * @param field Field configuration.
    #     * @return true if current step is configured for a field.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public abstract boolean isDefined(@Nonnull Field field);
    def isDefined(self, field):
        pass

    #    *
    #     * Do the work related to the step.
    #     *
    #     * @param field          Definition of the field.
    #     * @param mappingContext Mapping context.
    #     * @param machineContext State machine context.
    #     * @return Result of current step evaluation.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nullable public abstract Object process(@Nonnull Field field, @Nonnull MappingContext mappingContext, @Nonnull MachineContext machineContext);
    def process(self, field, mappingContext, machineContext):
        pass
