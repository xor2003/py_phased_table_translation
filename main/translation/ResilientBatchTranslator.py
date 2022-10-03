//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

#*
# * Translator that resiliently translates batches and supports staged processing.
# * <p>
# * Stages can be used to implement pre and post processing, filtering, etc.
# * Stages are defined using {@link ResilientBatchTranslator#processingStages}.
# * <p>
# * If stage results in an exception then {@link ResilientBatchTranslator#onError}
# * is used to produce result but processing continues with next element.
# * <p>
# * Result of every stage is traced using {@link ResilientBatchTranslator#traceStage}
# * and logger from {@link ResilientBatchTranslator#loggers}.
# * <p>
# * Any null elements and lists are ignored.
# * <p>
# * C - Type of context object.
# *
# * @deprecated Use {@link com.hpe.amce.translation.impl.StagesCaller},
# * {@link com.hpe.amce.translation.impl.ActualStageProcessor}
# * and {@link com.hpe.amce.translation.impl.StageCaller} with desired decorators instead.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Deprecated @Log4j2 @CompileStatic public class ResilientBatchTranslator<C> extends GroovyObjectSupport
class ResilientBatchTranslator(GroovyObjectSupport):
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @PostConstruct public void lookupLoggers()
    def lookupLoggers(self):
        assert processingStages
        loggers = processingStages.invokeMethod("collectEntries", [ClosureAnonymousInnerClass(self)])
        loggerIn = ((LogManager.invokeMethod("getLogger", [String.invokeMethod("valueOf", []) + ".input".invokeMethod("toString", [])])))

    class ClosureAnonymousInnerClass(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, stageName, code):
            return list(java.util.Arrays.asList(stageName, LogManager.invokeMethod("getLogger", [String.invokeMethod("valueOf", []) + "." + String.invokeMethod("valueOf", []).invokeMethod("toString", [])])))


    #    *
    #     * Translates a batch of elements.
    #     *
    #     * @param events  Elements to translate.
    #     * @param context Extra parameters to pass to pre-, post-processor and translator (optional, can be null).
    #     * @return Translated elements.
    #     * @see #processingStages
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public List<?> translateBatch(@Nullable List<?> events, @Nullable C context)
    def translateBatch(self, events, context):
        assert loggers
        assert processingStages
        eventsCount = events.invokeMethod("size", []) if int(events.asBoolean()) else 0
        metricRegistry.invokeMethod("meter", [String.invokeMethod("valueOf", []) + ".batches"]).invokeMethod("mark", [])
        metricRegistry.invokeMethod("histogram", [String.invokeMethod("valueOf", []) + ".in.batch_size"]).invokeMethod("update", [eventsCount])
        metricRegistry.invokeMethod("meter", [String.invokeMethod("valueOf", []) + ".in.events"]).invokeMethod("mark", [eventsCount])
        result = metricRegistry.invokeMethod("timer", [String.invokeMethod("valueOf", []) + ".translate_batch"]).invokeMethod("time", [com.hpe.amce.translation.ResilientBatchTranslator.BatchProcessor(makeSafeList(events), context)])
        outCount = result.invokeMethod("size", []) if int(result.asBoolean()) else 0
        metricRegistry.invokeMethod("histogram", [String.invokeMethod("valueOf", []) + ".out.batch_size"]).invokeMethod("update", [outCount])
        metricRegistry.invokeMethod("meter", [String.invokeMethod("valueOf", []) + ".out.events"]).invokeMethod("mark", [outCount])
        return result

    #    *
    #     * Translates a batch of elements.
    #     *
    #     * @param events  Elements to translate.
    #     * @param context Extra parameters to pass to pre-, post-processor and translator (optional, can be null).
    #     * @return Translated elements.
    #     * @see #processingStages
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public List<?> translateBatch(@Nullable List<?> events)
    def translateBatch(self, events):
        return translateBatch(events, None)

    #    *
    #     * Applies stage to event safely.
    #     * <p>
    #     * If stageCode generates exception then {@link ResilientBatchTranslator#onError}
    #     * will be called and its result will be returned instead.
    #     * <p>
    #     * If {@link ResilientBatchTranslator#onError} also generates exception
    #     * then an empty list will be returned.
    #     * <p>
    #     * The result is made null-safe: is never null and any null elements removed.
    #     *
    #     * @param event     Event to process.
    #     * @param context   Context passed to translator.
    #     * @param stageName Name of processing stage (for logging).
    #     * @param stageCode Code of processing stage.
    #     * @return Result of applying stageCode to event and context.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull @SuppressWarnings("CatchThrowable") public List<?> processEventSafely(@Nullable Object event, @Nullable Object context, @Nonnull String stageName, @Nonnull Closure<List<?>> stageCode)
    def processEventSafely(self, event, context, stageName, stageCode):
        try:
            return makeSafeList(stageCode.invokeMethod("call", [event, context]))
        except Throwable as e:
            try:
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
                return makeSafeList((List<?>) getOnError());
            except Throwable as ee:
                log.invokeMethod("error", ["Failed to process error " + String.invokeMethod("valueOf", []) + " " + "that has been observed for event " + String.invokeMethod("valueOf", []) + " " + "with context " + String.invokeMethod("valueOf", []) + " during stage " + String.invokeMethod("valueOf", []), ee])
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
                return ((List<?>)(new ArrayList()));



    #    *
    #     * Gets safer list.
    #     *
    #     * @param list Source list.
    #     * @return Empty list of source is null. Otherwise, same as source but without null elements.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private List<?> makeSafeList(@Nullable List<?> list)
    def makeSafeList(self, list):
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        return ((List<?>)((list is not None.asBoolean() ? list : new ArrayList()).invokeMethod("findAll", new Object[]{new Closure(self, self)

    class ClosureAnonymousInnerClass2(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, it):
            return it is not None

        def doCall(self):
            return self.doCall(None)


    def getTraceLevel(self):
        return traceLevel

    def setTraceLevel(self, traceLevel):
        self.traceLevel = traceLevel

    def getLoggerIn(self):
        return loggerIn

    def setLoggerIn(self, loggerIn):
        self.loggerIn = loggerIn

    def getMetricRegistry(self):
        return metricRegistry

    def setMetricRegistry(self, metricRegistry):
        self.metricRegistry = metricRegistry

    def getName(self):
        return name

    def setName(self, name):
        self.name = name

    def getDumpBatchToBuffer(self):
        return dumpBatchToBuffer

    def setDumpBatchToBuffer(self, dumpBatchToBuffer):
        self.dumpBatchToBuffer = dumpBatchToBuffer

    def getDumpEventToBuffer(self):
        return dumpEventToBuffer

    def setDumpEventToBuffer(self, dumpEventToBuffer):
        self.dumpEventToBuffer = dumpEventToBuffer

    def getTraceStage(self):
        return traceStage

    def setTraceStage(self, traceStage):
        self.traceStage = traceStage

    def getOnError(self):
        return onError

    def setOnError(self, onError):
        self.onError = onError

    def getProcessingStages(self):
        return processingStages

    def setProcessingStages(self, processingStages):
        self.processingStages = processingStages

    def getLoggers(self):
        return loggers

    def setLoggers(self, loggers):
        self.loggers = loggers

    def getEstimatedDumpedEventSide(self):
        return estimatedDumpedEventSide

    def setEstimatedDumpedEventSide(self, estimatedDumpedEventSide):
        self.estimatedDumpedEventSide = estimatedDumpedEventSide

    #    *
    #     * Level at which to trace processing.
    #     * <p>
    #     * Defaults to {@link org.apache.logging.log4j.Level#TRACE}.
    #     
    #    *
    #     * Logger to be used to trace incoming batch of events.
    #     * <p>
    #     * This is usually initialized in {@link #lookupLoggers()}.
    #     
    #    *
    #     * Metric registry to which metrics should be reported.
    #     
    #    *
    #     * Name of this translator.
    #     
    #    *
    #     * Dumps list of events.
    #     * <p>
    #     * The closure should take two parameters:
    #     * <ol>
    #     *     <li>List<?> events - a batch of events to be dumped</li>
    #     *     <li>StringBuilder buffer - buffer where to dump events to</li>
    #     * </ol>
    #     * <p>
    #     * By default, each event will be placed on a new line.
    #     * <p>
    #     * Individual events are dumped using {@link #dumpEventToBuffer}.
    #     

    #    *
    #     * Dumps event.
    #     * <p>
    #     * The closure should take two parameters:
    #     * <ol>
    #     *     <li>Object event - event to be dumped (could be null)</li>
    #     *     <li>StringBuilder buffer - buffer into which to dump event</li>
    #     * </ol>
    #     * <p>
    #     * By default, uses {@link StringBuilder#append(java.lang.Object)} which
    #     * will call {@link Object#toString()} in most cases.
    #     
    #    *
    #     * Logs events after being processed in specified stage.
    #     * <p>
    #     * The closure should take five parameters:
    #     * <ol>
    #     *     <li>StringBuilder buffer - re-usable buffer of high capacity (could need to be cleaned first)</li>
    #     *     <li>Logger logger - logger to be used for logging</li>
    #     *     <li>String stageName - name of the processing stage</li>
    #     *     <li>List<?> events - batch of events after a processing stage</li>
    #     *     <li>C context - extra parameters that were passed to translator</li>
    #     * </ol>
    #     * <p>
    #     * By default, checks if logger is enabled at {@link #traceLevel} and dumps events
    #     * using {@link #dumpBatchToBuffer} clearing buffer first.
    #     
    #    *
    #     * Closure that's called on event processing error.
    #     * <p>
    #     * The closure should take 4 parameters:
    #     * <ol>
    #     *     <li>C context - extra parameters that were passed to translator</li>
    #     *     <li>String stageName - name of processing stage</li>
    #     *     <li>Object event - event that has caused error</li>
    #     *     <li>Exception e - exception that has happened</li>
    #     * </ol>
    #     * <p>
    #     * The closure should return a list of events that should be returned
    #     * instead of what should have been returned if there was no event.
    #     * <p>
    #     * By default, error is logged, error metric for the particular phase is incremented
    #     * and an empty list is returned.
    #     * <p>
    #     * You can overwrite this closure with another one to return something in case
    #     * of error and call the original closure.
    #     
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
    #     * Loggers to be used on each processing stage.
    #     * <p>
    #     * Keys are stage names as in {@link #processingStages} and
    #     * values are loggers to be used on each stage.
    #     * <p>
    #     * By default, {@link #lookupLoggers()} will initialize this
    #     * so that each stage gets logger name that corresponds to
    #     * stage name.
    #     
    #    *
    #     * Estimated size of text of event dump.
    #     * <p>
    #     * This is used to create buffer of enough capacity to avoid re-sizing
    #     * during event tracing.
    #     * <p>
    #     * Default is 10K.
    #     

    #    *
    #     * Applies all stages to a batch of events.
    #     * <p>
    #     * Before starting any processing, the batch is traced using
    #     * {@link ResilientBatchTranslator#traceStage}.
    #     * <p>
    #     * Then the batch is processed using every stage in {@link ResilientBatchTranslator#processingStages}.
    #     * <p>
    #     * At every stage, each event from a batch is processed in a safe manner
    #     * so that if an exception is generated for one event then other events will
    #     * still be processed.
    #     * <p>
    #     * A metric will be recorded for the time it took to process
    #     * every event and every stage (separate metric for every stage).
    #     
    class BatchProcessor(GroovyObjectSupport, Callable):

        def __init__(self, outerInstance):
            self._outerInstance = outerInstance

        class ClosureAnonymousInnerClass3(Closure):
            def __init__(self):
                super().__init__(self._outerInstance, self._outerInstance)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: public Object doCall(List<?> events, final StringBuilder buffer)
            def doCall(self, events, buffer):
                if events is None.asBoolean():
                    buffer << "null"
                    return


                buffer << "["
                events.invokeMethod("eachWithIndex", [ClosureAnonymousInnerClass7(self, DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this, buffer)])

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
