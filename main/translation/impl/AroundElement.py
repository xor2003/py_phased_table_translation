#*
# * Defines what to do for each element of a batch.
# * <p>
# * C - type of translation context.
# *
# * @see AroundElement#translateElement
# 
class AroundElement(GroovyObjectSupport):
    #    *
    #     * Applies specified translation stage to a batch of elements.
    #     *
    #     * @param stageName Name of translation stage to be applied.
    #     * @param stageCode Code of translation stage to be applied.
    #     * @param element   Element to be translated. Can be null if null was passed.
    #     * @param context   Translation context or null if not specified.
    #     * @return Result of translating specified element using specified stage.
    #     * See {@link StagesCaller#processingStages}.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public abstract List<?> translateElement(@Nonnull String stageName, @Nonnull Closure<List<?>> stageCode, @Nullable Object element, @Nullable C context);
    def translateElement(self, stageName, stageCode, element, context):
        pass

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue
