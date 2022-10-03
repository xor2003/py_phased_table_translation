#*
# * {@link StageTracingDecorator} that reports how long it took to do the tracing.
# * <p>
# * Both in and out tracing for all stages is tracked using a single {@link com.codahale.metrics.Timer}.
# * <p>
# * C - type of translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class StageTracingMeteredDecorator<C> extends StageTracingDecorator<C>
class StageTracingMeteredDecorator(StageTracingDecorator):
    #    *
    #     * Creates new instance.
    #     *
    #     * @param next           Translator to be decorated.
    #     * @param dumper         Stage dumper.
    #     * @param metricRegistry Registry where to report metric.
    #     * @param metricName     Name of metric that will hold tracing time.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public StageTracingMeteredDecorator(AroundStage<C> next, StageDumper<C> dumper, MetricRegistry metricRegistry, String metricName)
    def __init__(self, next, dumper, metricRegistry, metricName):
        self(next, dumper, metricRegistry, metricName, MetricSupplierAnonymousInnerClass(self))

    class MetricSupplierAnonymousInnerClass(MetricSupplier):

        def __init__(self, outerInstance):
            self._outerInstance = outerInstance

        def newMetric(self):
            return Timer()


    #    *
    #     * Creates new instance.
    #     *
    #     * @param next           Translator to be decorated.
    #     * @param dumper         Stage dumper.
    #     * @param metricRegistry Registry where to report metric.
    #     * @param metricName     Name of metric that will hold tracing time.
    #     * @param timerFactory   Factory to be used to create timer metric.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public StageTracingMeteredDecorator(AroundStage<C> next, StageDumper<C> dumper, MetricRegistry metricRegistry, String metricName, MetricSupplier<Timer> timerFactory)
    def __init__(self, next, dumper, metricRegistry, metricName, timerFactory):
        super().__init__(next, dumper)
        timer = ((metricRegistry.invokeMethod("timer", [metricName, timerFactory])))

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override protected void traceIn(@Nonnull final String stageName, @Nonnull final List<?> elements, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def traceIn(self, stageName, elements, context):
        timer.invokeMethod("time", [ClosureAnonymousInnerClass(self, stageName, elements, context)])

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, stageName, elements, context):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._stageName = stageName
            self._elements = elements
            self._context = context

        def doCall(self, it):
            return com.hpe.amce.translation.impl.StageTracingMeteredDecorator.this.invokeMethod("traceIn", [self._stageName, self._elements, self._context])

        def doCall(self):
            return self.doCall(None)


#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override protected void traceOut(@Nonnull final String stageName, @Nonnull final List<?> elements, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def traceOut(self, stageName, elements, context):
        timer.invokeMethod("time", [ClosureAnonymousInnerClass2(self, stageName, elements, context)])

    class ClosureAnonymousInnerClass2(Closure):


        def __init__(self, outerInstance, stageName, elements, context):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._stageName = stageName
            self._elements = elements
            self._context = context

        def doCall(self, it):
            return com.hpe.amce.translation.impl.StageTracingMeteredDecorator.this.invokeMethod("traceOut", [self._stageName, self._elements, self._context])

        def doCall(self):
            return self.doCall(None)


