#*
# * Iterates over elements of batch and delegates to {@link AroundElement#translateElement} to actually
# * process each element.
# * <p>
# * C - type of translation context.
# *
# * @see ActualStageProcessor#aroundElement
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class ActualStageProcessor<C> extends GroovyObjectSupport implements AroundStage<C>
class ActualStageProcessor(GroovyObjectSupport, AroundStage):
    #    *
    #     * Creates an instance.
    #     *
    #     * @param aroundElement Processing to apply to each element of a batch.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public ActualStageProcessor(@Nonnull AroundElement<C> aroundElement)
    def __init__(self, aroundElement):
        self.aroundElement = aroundElement

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override @Nonnull public List<?> applyStage(@Nonnull final String stageName, @Nonnull final Closure<List<?>> stageCode, @Nonnull List<?> elements, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def applyStage(self, stageName, stageCode, elements, context):
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        return ((List<?>)(elements.invokeMethod("collectMany", new Object[]{new Closure(self, self)

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, stageName, stageCode, context):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._stageName = stageName
            self._stageCode = stageCode
            self._context = context

        def doCall(self, element):
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final java.lang.Object element1 = getAroundElement().invokeMethod("translateElement", new Object[]{stageName, stageCode, element, context});
            element1 = getAroundElement().invokeMethod("translateElement", [self._stageName, self._stageCode, element, self._context])
            return element1 if element1 else Collections.invokeMethod("emptyList", [])


    def getAroundElement(self):
        return aroundElement

    #    *
    #     * Applies translation to each element.
    #     

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue
