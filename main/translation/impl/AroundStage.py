#*
# * Defines what to do for each translation stage.
# *
# * @see AroundStage#applyStage
# 
class AroundStage(GroovyObjectSupport):
    #    *
    #     * Applies specified translation stage to a batch of elements.
    #     *
    #     * @param stageName Name of translation stage to be applied.
    #     * @param stageCode Code of translation stage to be applied.
    #     * @param elements  Batch of elements to be translated.
    #     * @param context   Translation context or null if not specified.
    #     * @return Result of translating elements using specified stage.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public abstract List<?> applyStage(@Nonnull String stageName, @Nonnull Closure<List<?>> stageCode, @Nonnull List<?> elements, @Nullable C context);
    def applyStage(self, stageName, stageCode, elements, context):
        pass

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue
