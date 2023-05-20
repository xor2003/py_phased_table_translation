//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

class MeteringFieldMapperDecoratorTest(Specification):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._metricRegistry = MetricRegistry()
        self._delegate = invokeMethod("Mock", [])
        self._metricNameCalculator = invokeMethod("Mock", [])
        self._instance = MeteringFieldMapperDecorator(self._delegate, self._metricRegistry, self._metricNameCalculator)
        self._fieldDescriptor = invokeMethod("Mock", [])
        self._mappingContext = invokeMethod("Mock", [])


    class ClosureAnonymousInnerClass(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            pass

        def doCall(self):
            doCall(None)


    class ClosureAnonymousInnerClass2(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            pass

        def doCall(self):
            doCall(None)


    class ClosureAnonymousInnerClass4(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            pass

        def doCall(self):
            doCall(None)


    class ClosureAnonymousInnerClass6(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return True

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass8(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            pass

        def doCall(self):
            doCall(None)


    class ClosureAnonymousInnerClass10(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            pass

        def doCall(self):
            doCall(None)


    class ClosureAnonymousInnerClass11(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            pass

        def doCall(self):
            doCall(None)


    class ClosureAnonymousInnerClass12(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            pass

        def doCall(self):
            doCall(None)

    def delegates_and_times(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        self._instance.invokeMethod("mapField", [self.getFieldDescriptor(), self.getMappingContext()])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        1 * self._metricNameCalculator.invokeMethod("calculateMetricName", [self.getFieldDescriptor(), self.getMappingContext()]) >> "foo"
        1 * self._delegate.invokeMethod("mapField", [self.getFieldDescriptor(), self.getMappingContext()])
        return self._metricRegistry.invokeMethod("timer", ["foo"]).count == 1

    def can_customize_reservoir(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        timerFactory = invokeMethod("Mock", [])
        self._instance.metricTimerFactory = timerFactory
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        self._instance.invokeMethod("mapField", [self.getFieldDescriptor(), self.getMappingContext()])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        self._metricNameCalculator.invokeMethod("calculateMetricName", [self.getFieldDescriptor(), self.getMappingContext()]) >> "foo"
        self._delegate.invokeMethod("mapField", [self.getFieldDescriptor(), self.getMappingContext()])
        return 1 * timerFactory.invokeMethod("newMetric", []) >> Timer(LockFreeExponentiallyDecayingReservoir.invokeMethod("builder", []).invokeMethod("build", []))

    def metric_name_is_per_field(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        self._instance.invokeMethod("mapField", [self.getFieldDescriptor(), self.getMappingContext()])
        self._instance.invokeMethod("mapField", [self.getFieldDescriptor(), self.getMappingContext()])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's unsigned right shift operator:
        2 * self._metricNameCalculator.invokeMethod("calculateMetricName", [self.getFieldDescriptor(), self.getMappingContext()]) >>> list(java.util.Arrays.asList("foo", "moo"))
        2 * self._delegate.invokeMethod("mapField", [self.getFieldDescriptor(), self.getMappingContext()])
        self._metricRegistry.invokeMethod("timer", ["foo"]).count == 1
        return self._metricRegistry.invokeMethod("timer", ["moo"]).count == 1

    def getMetricRegistry(self):
        return self._metricRegistry

    def setMetricRegistry(self, metricRegistry):
        self._metricRegistry = metricRegistry

    def getDelegate(self):
        return self._delegate

    def setDelegate(self, delegate):
        self._delegate = delegate

    def getMetricNameCalculator(self):

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
