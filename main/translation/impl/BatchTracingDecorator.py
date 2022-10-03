#*
# * Decorates another {@link BatchTranslator} to trace incoming and resulting batches to Log4J2.
# * <p>
# * Level for original and resulting batches can be controlled via
# * {@link BatchTracingDecorator#inLevel} and {@link BatchTracingDecorator#outLevel}.
# * <p>
# * Logger for original and resulting batches can be controlled via
# * {@link BatchTracingDecorator#inLogger} and {@link BatchTracingDecorator#outLogger}.
# * <p>
# * How original and resulting batches are dumped is controlled via
# * {@link BatchTracingDecorator#inDumper} and {@link BatchTracingDecorator#outDumper}.
# * <p>
# * A batch will be dumped only if corresponding log level is enabled for corresponding logger.
# * <p>
# * O - type of elements in original batch.
# * R - type of elements in resulting batch.
# * C - type of translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class BatchTracingDecorator<O, R, C> extends GroovyObjectSupport implements BatchTranslator<O, R, C>
class BatchTracingDecorator(GroovyObjectSupport, BatchTranslator):
    #    *
    #     * Creates new instance.
    #     *
    #     * @param next      Translator to be decorated.
    #     * @param inDumper  Dumper for original batch.
    #     * @param outDumper Dumper for resulting batch.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public BatchTracingDecorator(@Nonnull BatchTranslator<O, R, C> next, @Nonnull BatchDumper<O, C> inDumper, @Nonnull BatchDumper<R, C> outDumper)
    def __init__(self, next, inDumper, outDumper):
        #instance fields found by Java to Python Converter:
        self._next = None
        self._inDumper = None
        self._outDumper = None
        self._inLevel = Level.TRACE
        self._outLevel = Level.TRACE
        self._inLogger = LogManager.invokeMethod("getLogger", [com.hpe.amce.translation.impl.BatchTracingDecorator])
        self._outLogger = LogManager.invokeMethod("getLogger", [com.hpe.amce.translation.impl.BatchTracingDecorator])

        self._next = next
        self._inDumper = inDumper
        self._outDumper = outDumper

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public List<R> translateBatch(@Nullable List<O> elements, @Nullable C context)
    def translateBatch(self, elements, context):
        self.traceIn(elements, context)
        result = self._next.invokeMethod("translateBatch", [elements, context])
        self.traceOut(result, context)
        return result

    #    *
    #     * Traces input elements.
    #     *
    #     * @param elements Input elements.
    #     * @param context  Translation context.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: protected void traceIn(@Nullable List<O> elements, @Nullable C context)
    def traceIn(self, elements, context):
        if self._inLogger.invokeMethod("isEnabled", [self.getInLevel()]).asBoolean():
            self._inLogger.invokeMethod("log", [self.getInLevel(), self.getInDumper().invokeMethod("dumpBatch", [])])


    #    *
    #     * Traces output elements.
    #     *
    #     * @param elements Output elements.
    #     * @param context  Translation context.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: protected void traceOut(@Nullable List<R> elements, @Nullable C context)
    def traceOut(self, elements, context):
        if self._outLogger.invokeMethod("isEnabled", [self.getOutLevel()]).asBoolean():
            self._outLogger.invokeMethod("log", [self.getOutLevel(), self.getOutDumper().invokeMethod("dumpBatch", [])])


    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    def getInDumper(self):
        return self._inDumper

    def setInDumper(self, inDumper):
        self._inDumper = inDumper

    def getOutDumper(self):
        return self._outDumper

    def setOutDumper(self, outDumper):
        self._outDumper = outDumper

    def getInLevel(self):
        return self._inLevel

    def setInLevel(self, inLevel):
        self._inLevel = inLevel

    def getOutLevel(self):
        return self._outLevel

    def setOutLevel(self, outLevel):
        self._outLevel = outLevel

    def getInLogger(self):
        return self._inLogger

    def setInLogger(self, inLogger):
        self._inLogger = inLogger

    def getOutLogger(self):
        return self._outLogger

    def setOutLogger(self, outLogger):
        self._outLogger = outLogger

    #    *
    #     * Translator that is being decorated.
    #     
    #    *
    #     * Dumper for original batch.
    #     
    #    *
    #     * Dumper for resulting batch.
    #     
    #    *
    #     * Log level for original batch.
    #     * <p>
    #     * This is TRACE by default.
    #     
    #    *
    #     * Log level for resulting batch.
    #     * <p>
    #     * This is TRACE by default.
    #     
    #    *
    #     * Logger for original batch.
    #     * <p>
    #     * This is {@link BatchTracingDecorator} by default.
    #     
    #    *
    #     * Logger for resulting batch.
    #     * <p>
    #     * This is {@link BatchTracingDecorator} by default.
    #     

    @staticmethod
    def _setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue
