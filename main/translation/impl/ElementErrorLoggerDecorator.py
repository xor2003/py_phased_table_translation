#*
# * Logs error generated by decorated translator.
# * <p>
# * Once error is logged, it will be thrown again
# * so it can be caught to be reported as metric or ignored or propagated.
# * <p>
# * C - type of translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Log4j2 @CompileStatic public class ElementErrorLoggerDecorator<C> extends GroovyObjectSupport implements AroundElement<C>
class ElementErrorLoggerDecorator(GroovyObjectSupport, AroundElement):
    #    *
    #     * Creates instance.
    #     *
    #     * @param next Translator to be decorated.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public ElementErrorLoggerDecorator(@Nonnull AroundElement<C> next)
    def __init__(self, next):
        #instance fields found by Java to Python Converter:
        self._next = None

        self._next = next

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override @SuppressWarnings("CatchThrowable") public List<?> translateElement(@Nonnull String stageName, @Nonnull Closure<List<?>> stageCode, @Nullable Object element, @Nullable C context)
    def translateElement(self, stageName, stageCode, element, context):
        try:
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
            return ((List<?>)(next.invokeMethod("translateElement", new Object[]{stageName, stageCode, element, context})));
        except Throwable as e:
            log.invokeMethod("error", [String.invokeMethod("valueOf", []) + " has failed." + " Reason: " + String.invokeMethod("valueOf", []) + "." + " On: ~~~>" + String.invokeMethod("valueOf", []) + "<~~~" + " Context: " + String.invokeMethod("valueOf", []), e])
            raise e


    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    #    *
    #     * Translator to be decorated.
    #     

    @staticmethod
    def _setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue