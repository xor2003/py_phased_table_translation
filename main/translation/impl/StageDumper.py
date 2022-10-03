#*
# * Dumps to string a batch of elements at specified stage.
# * <p>
# * C - type of translation context.
# *
# * @see StageDumper#dumpBeforeStage
# * @see StageDumper#dumpAfterStage
# 
class StageDumper(GroovyObjectSupport):
    #    *
    #     * Dumps batch before specified stage.
    #     *
    #     * @param stageName Name of stage.
    #     * @param batch     Batch of elements or null if none.
    #     * @param context   Translation context or null if none.
    #     * @return String representation of parameters.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public abstract String dumpBeforeStage(@Nonnull String stageName, @Nullable List<?> batch, @Nullable C context);
    def dumpBeforeStage(self, stageName, batch, context):
        pass

    #    *
    #     * Dumps batch after specified stage.
    #     *
    #     * @param stageName Name of stage.
    #     * @param batch     Batch of elements or null if none.
    #     * @param context   Translation context or null if none.
    #     * @return String representation of parameters.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public abstract String dumpAfterStage(@Nonnull String stageName, @Nullable List<?> batch, @Nullable C context);
    def dumpAfterStage(self, stageName, batch, context):
        pass

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue
