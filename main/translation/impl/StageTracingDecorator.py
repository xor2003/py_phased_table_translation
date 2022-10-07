#*
# * Decorates another {@link AroundStage}
# * to trace a batch before and after each stage.
# * <p>
# * Level of logging before and after a stage can be controlled via
# * {@link StageTracingDecorator#inLevel} and {@link StageTracingDecorator#outLevel}.
# * <p>
# * How a batch is dumped is controlled via {@link StageTracingDecorator#dumper}.
# * <p>
# * Which logger is used to to trace before and after each stage is controlled via
# * {@link StageTracingDecorator#findLoggerForStageAndMode}.
# * <p>
# * C - type of translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Log4j2 @CompileStatic public class StageTracingDecorator<C> extends GroovyObjectSupport implements AroundStage<C>
class StageTracingDecorator(GroovyObjectSupport, AroundStage):
    #    *
    #     * Creates new instance.
    #     *
    #     :param next:   Translator to be decorated.
    #     :param dumper: Stage dumper.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public StageTracingDecorator(@Nonnull AroundStage<C> next, @Nonnull StageDumper<C> dumper)
    def __init__(self, next, dumper):
        #instance fields found by Java to Python Converter:
        self._next = None
        self._inLevel = Level.TRACE
        self._outLevel = Level.TRACE
        self._dumper = None
        self._loggers = None
        self._findLoggerForStageAndMode = None

        self._next = next
        self._dumper = dumper

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public List<?> applyStage(@Nonnull String stageName, @Nonnull Closure<List<?>> stageCode, @Nonnull List<?> elements, @Nullable C context)
    def applyStage(self, stageName, stageCode, elements, context):
        self.traceIn(stageName, elements, context)
        result = self._next.invokeMethod("applyStage", [stageName, stageCode, elements, context])
        self.traceOut(stageName, result, context)
        return result

    #    *
    #     * Traces input elements.
    #     *
    #     :param stageName: Name of stage being traced.
    #     :param elements:  Stage input elements.
    #     :param context:   Translation context.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: protected void traceIn(@Nonnull String stageName, @Nonnull List<?> elements, @Nullable C context)
    def traceIn(self, stageName, elements, context):
        inLogger = self.getFindLoggerForStageAndMode()
        if inLogger.invokeMethod("isEnabled", [self.getInLevel()]).asBoolean():
            inLogger.invokeMethod("log", [self.getInLevel(), self.getDumper().invokeMethod("dumpBeforeStage", [])])


    #    *
    #     * Traces output elements.
    #     *
    #     :param stageName: Name of stage being traced.
    #     :param elements:  Stage output elements.
    #     :param context:   Translation context.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: protected void traceOut(@Nonnull String stageName, @Nonnull List<?> elements, @Nullable C context)
    def traceOut(self, stageName, elements, context):
        outLogger = self.getFindLoggerForStageAndMode()
        if outLogger.invokeMethod("isEnabled", [self.getOutLevel()]).asBoolean():
            outLogger.invokeMethod("log", [self.getOutLevel(), self.getDumper().invokeMethod("dumpAfterStage", [])])


    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    def getInLevel(self):
        return self._inLevel

    def setInLevel(self, inLevel):
        self._inLevel = inLevel

    def getOutLevel(self):
        return self._outLevel

    def setOutLevel(self, outLevel):
        self._outLevel = outLevel

    def getDumper(self):
        return self._dumper

    def setDumper(self, dumper):
        self._dumper = dumper

    def getLoggers(self):
        return self._loggers

    def setLoggers(self, loggers):
        self._loggers = loggers

    def getFindLoggerForStageAndMode(self):
        return self._findLoggerForStageAndMode

    def setFindLoggerForStageAndMode(self, findLoggerForStageAndMode):
        self._findLoggerForStageAndMode = findLoggerForStageAndMode

    #    *
    #     * Translator being decorated.
    #     
    #    *
    #     * Level at which batch will be traced before translation stage is applied.
    #     * <p>
    #     * This is TRACE by default.
    #     
    #    *
    #     * Level at which batch will be traced after translation stage is applied.
    #     * <p>
    #     * This is TRACE by default.
    #     
    #    *
    #     * Dumper for all stages.
    #     
    #    *
    #     * Mapping between stages and loggers.
    #     * <p>
    #     * See {@link #findLoggerForStageAndMode} for details.
    #     
    #    *
    #     * Controls which logger to be used to trace before and after each stage.
    #     * <p>
    #     * The closure should take two parameters:
    #     * <ol>
    #     *     <li>String stage - name of stage being traced.</li>
    #     *     <li>boolean isIn - true if tracing before stage, false if tracing after stage.</li>
    #     * </ol>
    #     * <p>
    #     * The closure should return a logger that should be used to trace a batch.
    #     * <p>
    #     * By default, it will look for logger in {@link #loggers}. If not found then
    #     * logger for {@link StageTracingDecorator} will be used. By default, the key should be
    #     * stageName.in for logger to be used before stage with name stageName and
    #     * stageName.out for logger to be used after stage with name stageName.
    #     

    @staticmethod
    def _setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue

    class ClosureAnonymousInnerClass(Closure):
        def __init__(self):
            super().__init__(outerInstance, outerInstance)

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public Object doCall(@Nonnull String stage, boolean isIn)
        def doCall(self, stage, isIn):
            if not outerInstance.getLoggers().asBoolean():
                return log

#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final java.lang.Object var = getLoggers().getAt(stage + (isIn ? ".in" : ".out"));
            var = outerInstance.getLoggers().getAt(stage + (".in" if isIn else ".out"))
            return var if var else log

