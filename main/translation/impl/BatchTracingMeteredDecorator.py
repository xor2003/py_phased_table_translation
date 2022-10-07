#*
# * {@link BatchTracingDecorator} that reports how long it took to do the tracing.
# * <p>
# * Both in and out tracing is tracked using a single {@link com.codahale.metrics.Timer}.
# * <p>
# * O - type of elements in original batch.
# * R - type of elements in resulting batch.
# * C - type of translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class BatchTracingMeteredDecorator<O, R, C> extends BatchTracingDecorator<O, R, C>
class BatchTracingMeteredDecorator(BatchTracingDecorator):
    #    *
    #     * Creates new instance.
    #     *
    #     :param next:           Translator to be decorated.
    #     :param inDumper:       Dumper for original batch.
    #     :param outDumper:      Dumper for resulting batch.
    #     :param metricRegistry: Registry where to report metric.
    #     :param metricName:     Name of metric that will hold tracing time.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public BatchTracingMeteredDecorator(BatchTranslator<O, R, C> next, BatchDumper<O, C> inDumper, BatchDumper<R, C> outDumper, MetricRegistry metricRegistry, String metricName)
    def __init__(self, next, inDumper, outDumper, metricRegistry, metricName):
        self(next, inDumper, outDumper, metricRegistry, metricName, MetricSupplierAnonymousInnerClass(self))

    class MetricSupplierAnonymousInnerClass(MetricSupplier):

        def __init__(self, outerInstance):
            self._outerInstance = outerInstance

        def newMetric(self):
            return Timer()


    #    *
    #     * Creates new instance.
    #     *
    #     :param next:           Translator to be decorated.
    #     :param inDumper:       Dumper for original batch.
    #     :param outDumper:      Dumper for resulting batch.
    #     :param metricRegistry: Registry where to report metric.
    #     :param metricName:     Name of metric that will hold tracing time.
    #     :param timerFactory:   Factory to be used to create metric.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @SuppressWarnings("ParameterCount") public BatchTracingMeteredDecorator(BatchTranslator<O, R, C> next, BatchDumper<O, C> inDumper, BatchDumper<R, C> outDumper, MetricRegistry metricRegistry, String metricName, MetricSupplier<Timer> timerFactory)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
    def __init__(self, next, inDumper, outDumper, metricRegistry, metricName, timerFactory):
        super().__init__(next, inDumper, outDumper)
        timer = ((metricRegistry.invokeMethod("timer", [metricName, timerFactory])))

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override protected void traceIn(@Nullable final List<O> elements, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def traceIn(self, elements, context):
        timer.invokeMethod("time", [ClosureAnonymousInnerClass(self, elements, context)])

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, elements, context):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._elements = elements
            self._context = context

        def doCall(self, it):
            return com.hpe.amce.translation.impl.BatchTracingMeteredDecorator.this.invokeMethod("traceIn", [self._elements, self._context])

        def doCall(self):
            return self.doCall(None)


#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override protected void traceOut(@Nullable final List<R> elements, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def traceOut(self, elements, context):
        timer.invokeMethod("time", [ClosureAnonymousInnerClass2(self, elements, context)])

    class ClosureAnonymousInnerClass2(Closure):


        def __init__(self, outerInstance, elements, context):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._elements = elements
            self._context = context

        def doCall(self, it):
            return com.hpe.amce.translation.impl.BatchTracingMeteredDecorator.this.invokeMethod("traceOut", [self._elements, self._context])

        def doCall(self):
            return self.doCall(None)


