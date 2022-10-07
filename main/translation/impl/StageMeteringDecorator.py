#*
# * Decorates another {@link AroundStage}
# * to report metrics for each stage.
# * <p>
# * The following metrics will be published:
# * <ul>
# *     <li>Size difference for a batch before and after a stage (how much was filtered out or added)</li>
# *     <li>Time it takes to process a batch on each stage</li>
# * </ul>
# * <p>
# * Metrics will be published in {@link StageMeteringDecorator#metricRegistry} with
# * {@link StageMeteringDecorator#metricsBaseName} being the prefix for the name of
# * all metrics.
# * <p>
# * It is possible to override default metric names via
# * {@link StageMeteringDecorator#deltaBatchSizeMetricName},
# * {@link StageMeteringDecorator#stageTimerMetricName}.
# * <p>
# * Parameters of metrics can be customized via
# * {@link StageMeteringDecorator#metricTimerFactory}
# * and {@link StageMeteringDecorator#metricHistogramFactory}.
# * <p>
# * C - type of translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Log4j2 @CompileStatic public class StageMeteringDecorator<C> extends GroovyObjectSupport implements AroundStage<C>
class StageMeteringDecorator(GroovyObjectSupport, AroundStage):
    #    *
    #     * Creates new instance.
    #     *
    #     :param next:            Translator to decorate.
    #     :param metricRegistry:  Registry where to report metrics.
    #     :param metricsBaseName: Prefix for metric names.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public StageMeteringDecorator(@Nonnull AroundStage<C> next, @Nonnull MetricRegistry metricRegistry, @Nonnull String metricsBaseName)
    def __init__(self, next, metricRegistry, metricsBaseName):
        self.next = next
        self.metricRegistry = metricRegistry
        self.metricsBaseName = metricsBaseName

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public List<?> applyStage(@Nonnull final String stageName, @Nonnull final Closure<List<?>> stageCode, @Nonnull final List<?> elements, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def applyStage(self, stageName, stageCode, elements, context):
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        List<?> result = metricRegistry.invokeMethod("timer", new Object[]{getStageTimerMetricName(), getMetricTimerFactory()}).invokeMethod("time", new Object[]{(Callable<List<?>>) new Closure(self, self)
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final java.lang.Object size = result.invokeMethod("size", new Object[0]);
        size = result.invokeMethod("size", [])
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final java.lang.Object size1 = elements.invokeMethod("size", new Object[0]);
        size1 = elements.invokeMethod("size", [])
        metricRegistry.invokeMethod("histogram", [getDeltaBatchSizeMetricName(), getMetricHistogramFactory()]).invokeMethod("update", [(size if size else 0) - (size1 if size1 else 0)])
        return result

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, stageName, stageCode, elements, context):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._stageName = stageName
            self._stageCode = stageCode
            self._elements = elements
            self._context = context

        def doCall(self, it):
            return getNext().invokeMethod("applyStage", [self._stageName, self._stageCode, self._elements, self._context])

        def doCall(self):
            return self.doCall(None)


    def getNext(self):
        return next

    def setNext(self, next):
        self.next = next

    def getMetricRegistry(self):
        return metricRegistry

    def setMetricRegistry(self, metricRegistry):
        self.metricRegistry = metricRegistry

    def getMetricsBaseName(self):
        return metricsBaseName

    def setMetricsBaseName(self, metricsBaseName):
        self.metricsBaseName = metricsBaseName

    def getDeltaBatchSizeMetricName(self):
        return deltaBatchSizeMetricName

    def setDeltaBatchSizeMetricName(self, deltaBatchSizeMetricName):
        self.deltaBatchSizeMetricName = deltaBatchSizeMetricName

    def getStageTimerMetricName(self):
        return stageTimerMetricName

    def setStageTimerMetricName(self, stageTimerMetricName):
        self.stageTimerMetricName = stageTimerMetricName

    def getMetricHistogramFactory(self):
        return metricHistogramFactory

    def setMetricHistogramFactory(self, metricHistogramFactory):
        self.metricHistogramFactory = metricHistogramFactory

    def getMetricTimerFactory(self):
        return metricTimerFactory

    def setMetricTimerFactory(self, metricTimerFactory):
        self.metricTimerFactory = metricTimerFactory

    #    *
    #     * Translator being decorated.
    #     
    #    *
    #     * Metric registry to which metrics should be reported.
    #     
    #    *
    #     * Base name for reported metrics.
    #     
    #    *
    #     * Name of the metric that will report batch size delta for a stage.
    #     * <p>
    #     * Zero means that stage did not change number of elements. Positive value means that
    #     * stage has added elements. Negative value means that stage has removed elements.
    #     * <p>
    #     * The closure should take stage name as parameter and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}STAGENAME.delta.
    #     
    #    *
    #     * Name of the metric that will report time it took to process a batch on a stage.
    #     * <p>
    #     * The closure should take stage name as parameter and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}STAGENAME.batch.
    #     
    #    *
    #     * Factory that is to be used to create histogram metrics.
    #     * <p>
    #     * By default, uses {@link com.codahale.metrics.ExponentiallyDecayingReservoir}.
    #     
    #    *
    #     * Factory that is to be used to create timer metrics.
    #     * <p>
    #     * By default, uses default parameters of {@link com.codahale.metrics.Timer#Timer()}.
    #     

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue

    class ClosureAnonymousInnerClass2(Closure):
        def __init__(self):
            super().__init__(outerInstance, outerInstance)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: public Object doCall(final String stageName)
        def doCall(self, stageName):
            return String.invokeMethod("valueOf", [getMetricsBaseName()]) + String.invokeMethod("valueOf", [stageName]) + ".delta".invokeMethod("toString", [])


    class ClosureAnonymousInnerClass3(Closure):
        def __init__(self):
            super().__init__(outerInstance, outerInstance)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: public Object doCall(final String stageName)
        def doCall(self, stageName):
            return String.invokeMethod("valueOf", [getMetricsBaseName()]) + String.invokeMethod("valueOf", [stageName]) + ".batch".invokeMethod("toString", []).invokeMethod("toString", [])


    class MetricSupplierAnonymousInnerClass(MetricRegistry.MetricSupplier):
        def newMetric(self):
            return Histogram(ExponentiallyDecayingReservoir())


    class MetricSupplierAnonymousInnerClass2(MetricRegistry.MetricSupplier):
        def newMetric(self):
            return Timer()

