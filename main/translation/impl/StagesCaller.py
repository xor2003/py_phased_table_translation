#*
# * Iterates over list of processing stages and delegates to {@link AroundStage#applyStage} for each of them.
# * <p>
# * Each next stage gets input produced by previous stage.
# * <p>
# * O - type of source elements.
# * R - type of result elements.
# * C - type of translation context.
# *
# * @see StagesCaller#processingStages
# * @see StagesCaller#aroundStage
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class StagesCaller<O, R, C> extends GroovyObjectSupport implements BatchTranslator<O, R, C>
class StagesCaller(GroovyObjectSupport, BatchTranslator):
    #    *
    #     * Creates an instance.
    #     *
    #     * @param processingStages Definition of processing stages.
    #     * @param aroundStage      What to do for each stage.
    #     * @see StagesCaller#processingStages
    #     * @see StagesCaller#aroundStage
    #     
    def __init__(self, processingStages, aroundStage):
        self.processingStages = processingStages
        self.aroundStage = aroundStage

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public List<R> translateBatch(@Nullable List<O> elements, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def translateBatch(self, elements, context):
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        final Reference<List<?>> result = new groovy.lang.Reference<List<?>>(elements);
        processingStages.invokeMethod("each", [ClosureAnonymousInnerClass(self, context, result)])
        return result.get()

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, context, result):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._context = context
            self._result = result

        def doCall(self, stageName, stageCode):
            return setGroovyRef(self._result,getAroundStage().invokeMethod("applyStage", [stageName, stageCode, self._result.get(), self._context]) if self._result.get() is not None.asBoolean() else [])


    def getProcessingStages(self):
        return processingStages

    def getAroundStage(self):
        return aroundStage

    #    *
    #     * Processing stages.
    #     * <br/>
    #     * Keys are stage names and entries are closures that do the processing.
    #     * <br/>
    #     * The closures should take two parameters.
    #     * Where first parameter is a single event being processed.
    #     * Its type should be a type of raw event for the first stage.
    #     * For the second and further stages, its type should be the same
    #     * as output of previous stage. For example, if previous stage
    #     * is just a filter on raw events then for the current stage,
    #     * the first parameter should also be of raw event type.
    #     * Second parameter has type C and represents context (extra parameters) passed to
    #     * {@link #translateBatch}.
    #     * <br/>
    #     * The closure should return list of processed events (zero if filtered out,
    #     * exactly one for one-to-one translation, more than one if any extra
    #     * events are to be injected).
    #     * <br/>
    #     * Stages are called in whatever order map iterates them so use ordered maps.
    #     
    #    *
    #     * Applies translation stage to a batch of elements.
    #     

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue
