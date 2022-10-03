//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

#*
# * Decorates another {@link BatchTranslator} to publish metrics about incoming and resulting batches.
# * <p>
# * The following metrics will be published:
# * <ul>
# *     <li>Received number of batches - meter</li>
# *     <li>Size of incoming batches - histogram</li>
# *     <li>Total number of incoming elements across all batches - meter</li>
# *     <li>Time it takes to translate a batch - timer</li>
# *     <li>Size of resulting batches - histogram</li>
# *     <li>Total number of resulting elements across all batches - meter</li>
# * </ul>
# * <p>
# * Metrics will be published in {@link BatchMeteringDecorator#metricRegistry} with
# * {@link BatchMeteringDecorator#metricsBaseName} being the prefix for the name of
# * all metrics.
# * <p>
# * It is possible to override default metric names via
# * {@link BatchMeteringDecorator#incomingBatchCountMetricName},
# * {@link BatchMeteringDecorator#incomingBatchSizeMetricName},
# * {@link BatchMeteringDecorator#incomingElementsCountMetricName},
# * {@link BatchMeteringDecorator#translationTimeMetricName},
# * {@link BatchMeteringDecorator#outgoingBatchSizeMetricName},
# * {@link BatchMeteringDecorator#outgoingElementsCountMetricName}.
# * <p>
# * Parameters of metrics (for example, reservoir type) can be customized via
# * {@link BatchMeteringDecorator#metricHistogramFactory},
# * {@link BatchMeteringDecorator#metricMeterFactory},
# * {@link BatchMeteringDecorator#metricTimerFactory}.
# * <p>
# * O - type of elements in original batch.
# * R - type of elements in resulting batch.
# * C - type of translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class BatchMeteringDecorator<O, R, C> extends GroovyObjectSupport implements BatchTranslator<O, R, C>
class BatchMeteringDecorator(GroovyObjectSupport, BatchTranslator):
    #    *
    #     * Creates new instance.
    #     *
    #     * @param next            Translator to be decorated.
    #     * @param metricRegistry  Registry where to publish metrics.
    #     * @param metricsBaseName Base name (prefix) of the metrics.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public BatchMeteringDecorator(@Nonnull BatchTranslator<O, R, C> next, @Nonnull MetricRegistry metricRegistry, @Nonnull String metricsBaseName)
    def __init__(self, next, metricRegistry, metricsBaseName):
        self.next = next
        self.metricRegistry = metricRegistry
        self.metricsBaseName = metricsBaseName

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public List<R> translateBatch(@Nullable final List<O> elements, @Nullable final C context)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def translateBatch(self, elements, context):
        incomingBatchSize = elements.invokeMethod("size", []) if int(elements.asBoolean()) else 0
        metricRegistry.invokeMethod("meter", [getIncomingBatchCountMetricName(), getMetricMeterFactory()]).invokeMethod("mark", [])
        metricRegistry.invokeMethod("histogram", [getIncomingBatchSizeMetricName(), getMetricHistogramFactory()]).invokeMethod("update", [incomingBatchSize])
        metricRegistry.invokeMethod("meter", [getIncomingElementsCountMetricName(), getMetricMeterFactory()]).invokeMethod("mark", [incomingBatchSize])
        result = metricRegistry.invokeMethod("timer", [getTranslationTimeMetricName(), getMetricTimerFactory()]).invokeMethod("time", [ClosureAnonymousInnerClass(self, elements, context)])
        outgoingBatchSize = result.invokeMethod("size", []) if int(result.asBoolean()) else 0
        metricRegistry.invokeMethod("histogram", [getOutgoingBatchSizeMetricName(), getMetricHistogramFactory()]).invokeMethod("update", [outgoingBatchSize])
        metricRegistry.invokeMethod("meter", [getOutgoingElementsCountMetricName(), getMetricMeterFactory()]).invokeMethod("mark", [outgoingBatchSize])
        return result

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, elements, context):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._elements = elements
            self._context = context

        def doCall(self, it):
            return getNext().invokeMethod("translateBatch", [self._elements, self._context])

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

    def getIncomingBatchCountMetricName(self):
        return incomingBatchCountMetricName

    def setIncomingBatchCountMetricName(self, incomingBatchCountMetricName):
        self.incomingBatchCountMetricName = incomingBatchCountMetricName

    def getIncomingBatchSizeMetricName(self):
        return incomingBatchSizeMetricName

    def setIncomingBatchSizeMetricName(self, incomingBatchSizeMetricName):
        self.incomingBatchSizeMetricName = incomingBatchSizeMetricName

    def getIncomingElementsCountMetricName(self):
        return incomingElementsCountMetricName

    def setIncomingElementsCountMetricName(self, incomingElementsCountMetricName):
        self.incomingElementsCountMetricName = incomingElementsCountMetricName

    def getTranslationTimeMetricName(self):
        return translationTimeMetricName

    def setTranslationTimeMetricName(self, translationTimeMetricName):
        self.translationTimeMetricName = translationTimeMetricName

    def getOutgoingBatchSizeMetricName(self):
        return outgoingBatchSizeMetricName

    def setOutgoingBatchSizeMetricName(self, outgoingBatchSizeMetricName):
        self.outgoingBatchSizeMetricName = outgoingBatchSizeMetricName

    def getOutgoingElementsCountMetricName(self):
        return outgoingElementsCountMetricName

    def setOutgoingElementsCountMetricName(self, outgoingElementsCountMetricName):
        self.outgoingElementsCountMetricName = outgoingElementsCountMetricName

    def getMetricMeterFactory(self):
        return metricMeterFactory

    def setMetricMeterFactory(self, metricMeterFactory):
        self.metricMeterFactory = metricMeterFactory

    def getMetricHistogramFactory(self):
        return metricHistogramFactory

    def setMetricHistogramFactory(self, metricHistogramFactory):
        self.metricHistogramFactory = metricHistogramFactory

    def getMetricTimerFactory(self):
        return metricTimerFactory

    def setMetricTimerFactory(self, metricTimerFactory):
        self.metricTimerFactory = metricTimerFactory

    #    *
    #     * Translator that is being decorated.
    #     
    #    *
    #     * Metric registry to which metrics should be reported.
    #     
    #    *
    #     * Base name for reported metrics.
    #     
    #    *
    #     * Name of the metric that will report how many batches have been received.
    #     * <p>
    #     * The closure should take no parameters and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}.batches.count.
    #     
    #    *
    #     * Name of the metric that will report sizes of incoming batches.
    #     * <p>
    #     * The closure should take no parameters and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}.in.batch_size.
    #     
    #    *
    #     * Name of the metric that will report total number of incoming elements.
    #     * <p>
    #     * The closure should take no parameters and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}.in.events.
    #     
    #    *
    #     * Name of the metric that will report time it takes to translate a batch.
    #     * <p>
    #     * The closure should take no parameters and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}.translate_batch.
    #     
    #    *
    #     * Name of the metric that will report sizes of resulting batches.
    #     * <p>
    #     * The closure should take no parameters and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}.out.batch_size.
    #     
    #    *
    #     * Name of the metric that will report total number of resulting elements.
    #     * <p>
    #     * The closure should take no parameters and should return metric name.
    #     * <p>
    #     * By default, this is {@link #metricsBaseName}.out.events.
    #     
    #    *
    #     * Factory that is to be used to create meter metrics.
    #     * <p>
    #     * By default, uses default parameters of {@link Meter#Meter()}.
    #     
    #    *
    #     * Factory that is to be used to create histogram metrics.
    #     * <p>
    #     * By default, uses {@link ExponentiallyDecayingReservoir}.
    #     
    #    *
    #     * Factory that is to be used to create timer metrics.
    #     * <p>
    #     * By default, uses default parameters of {@link Timer#Timer()}.
    #     

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue

    class ClosureAnonymousInnerClass2(Closure):
        def __init__(self):
            super().__init__(outerInstance, outerInstance)

        def doCall(self, it):
            return getMetricsBaseName() + ".batches.count"

        def doCall(self):
            return self.doCall(None)


    class ClosureAnonymousInnerClass3(Closure):
        def __init__(self):
            super().__init__(outerInstance, outerInstance)

        def doCall(self, it):
            return getMetricsBaseName() + ".in.batch_size"

        def doCall(self):
            return self.doCall(None)


    class ClosureAnonymousInnerClass4(Closure):
        def __init__(self):
            super().__init__(outerInstance, outerInstance)

        def doCall(self, it):
            return getMetricsBaseName() + ".in.events"

        def doCall(self):
            return self.doCall(None)


    class ClosureAnonymousInnerClass5(Closure):
        def __init__(self):

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
