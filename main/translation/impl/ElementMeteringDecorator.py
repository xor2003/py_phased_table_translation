#*
# * Decorates another {@link AroundElement} to report how long it took to process individual element on each stage.
# * <p>
# * The time is reported per element per stage rather than per batch per stage.
# * <p>
# * Metrics will be published in {@link ElementMeteringDecorator#metricRegistry} with
# * {@link ElementMeteringDecorator#metricsBaseName} being the prefix for the name of
# * all metrics.
# * <p>
# * It is possible to override default metric names via
# * {@link ElementMeteringDecorator#timerName}.
# * <p>
# * Parameters of metric can be customized via {@link ElementMeteringDecorator#metricTimerFactory}.
# * <p>
# * C - type of translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class ElementMeteringDecorator<C> extends GroovyObjectSupport implements AroundElement<C>
class ElementMeteringDecorator(GroovyObjectSupport, AroundElement):
    #    *
    #     * Creates new instance.
    #     *
    #     :param next:            Translator to decorate.
    #     :param metricRegistry:  Registry where to report metrics.
    #     :param metricsBaseName: Prefix for metric names.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public ElementMeteringDecorator(@Nonnull AroundElement<C> next, @Nonnull MetricRegistry metricRegistry, @Nonnull String metricsBaseName)
    def __init__(self, next, metricRegistry, metricsBaseName):
        self.next = next
        self.metricRegistry = metricRegistry
        self.metricsBaseName = metricsBaseName

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public List<?> translateElement(@Nonnull final String stageName, @Nonnull final Closure<List<?>> stageCode, @Nullable final Object element, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def translateElement(self, stageName, stageCode, element, context):
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        return ((List<?>)(metricRegistry.invokeMethod("timer", new Object[]{getTimerName(), getMetricTimerFactory()}).invokeMethod("time", new Object[]{(Callable) new Closure(self, self)

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, stageName, stageCode, element, context):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._stageName = stageName
            self._stageCode = stageCode
            self._element = element
            self._context = context

        def doCall(self, it):
            return getNext().invokeMethod("translateElement", [self._stageName, self._stageCode, self._element, self._context])

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

    def getTimerName(self):
        return timerName

    def setTimerName(self, timerName):
        self.timerName = timerName

    def getMetricTimerFactory(self):
        return metricTimerFactory

    def setMetricTimerFactory(self, metricTimerFactory):
        self.metricTimerFactory = metricTimerFactory

    #    *
    #     * Translator to be decorated.
    #     
    #    *
    #     * Metric registry to which metrics should be reported.
    #     
    #    *
    #     * Base name for reported metrics.
    #     
    #    *
    #     * Name of the metric that will report time it took to process single element on each stage.
    #     * <p>
    #     * The closure should take stage name as parameter and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}STAGENAME.one.
    #     
    #    *
    #     * Factory that is to be used to create timer metrics.
    #     * <p>
    #     * By default, uses default parameters of {@link com.codahale.metrics.Timer#Timer()}.
    #     
