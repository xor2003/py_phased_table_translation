//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

import math

#*
# * Test that new API can be used to achieve alike functionality as was done by legacy code.
# 
class OnParWithLegacyTest(Specification):
    def createInstance(self, processingStages):
        aroundElement = (ElementMeteringDecorator(ElementErrorSuppressorDecorator(ElementErrorMeteringDecorator(ElementErrorLoggerDecorator(StageCaller()), metricRegistry, invokeMethod("getClass", []).name + ".")), metricRegistry, invokeMethod("getClass", []).name)).invokeMethod("tap", [ClosureAnonymousInnerClass(self)])
        aroundStage = (StageTracingDecorator(StageMeteringDecorator(ActualStageProcessor(aroundElement), metricRegistry, invokeMethod("getClass", []).name + "."), FormattingToStringDumper())).invokeMethod("tap", [ClosureAnonymousInnerClass2(self)])
#JAVA TO PYTHON CONVERTER TODO TASK: The following assignment within expression was not converted by Java to Python Converter:
#ORIGINAL LINE: return ((BatchTranslator<com.hpe.amce.translation.impl.OnParWithLegacyTest.RawEvent, com.hpe.amce.translation.impl.OnParWithLegacyTest.TranslatedEvent, com.hpe.amce.translation.impl.OnParWithLegacyTest.Context>)(new BatchTracingDecorator<RawEvent, TranslatedEvent, Context>(new BatchMeteringDecorator<RawEvent, TranslatedEvent, Context>(new StagesCaller<RawEvent, TranslatedEvent, Context>(processingStages, aroundStage), metricRegistry, invokeMethod("getClass", new Object[0]).name).invokeMethod("tap", new Object[]{new Closure(this, this)
        return ((BatchTranslator)((BatchTracingDecorator((BatchMeteringDecorator(StagesCaller(processingStages, aroundStage), metricRegistry, invokeMethod("getClass", []).name)).invokeMethod("tap", [ClosureAnonymousInnerClass3(self)]), FormattingToStringDumper(), FormattingToStringDumper())).invokeMethod("tap", {Closure(self, self){public Object doCall(Object it){it.inLevel = Level.INFO
        it.outLevel = Level.INFO
        # Force legacy logger name
        it.inLogger = LogManager.invokeMethod("getLogger", [com.hpe.amce.translation.impl.OnParWithLegacyTest.class.name + ".input"])
        return it.outLogger = LogManager.invokeMethod("getLogger", [com.hpe.amce.translation.impl.OnParWithLegacyTest.class.name + ".output"])

    class ClosureAnonymousInnerClass(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, it):
            # Force legacy metric names
            return it.timerName = ClosureAnonymousInnerClass4(self, DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this, it)

        class ClosureAnonymousInnerClass4(Closure):


            def __init__(self, outerInstance, self, self, it):
                super().__init__(self, self)
                self._outerInstance = outerInstance
                self._it = it

            def doCall(self, stageName):
                return String.invokeMethod("valueOf", [self._it.metricsBaseName]) + ".one." + String.invokeMethod("valueOf", [stageName])


        def doCall(self):
            return self.doCall(None)


    class ClosureAnonymousInnerClass2(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, it):
            # Force legacy behaviour: trace out only with legacy logger name
            it.outLevel = Level.INFO
            return it.findLoggerForStageAndMode = ClosureAnonymousInnerClass5(self, DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this)

        class ClosureAnonymousInnerClass5(Closure):

            def __init__(self, outerInstance, self, self):
                super().__init__(self, self)
                self._outerInstance = outerInstance

            def doCall(self, stage, isIn):
                return LogManager.invokeMethod("getLogger", [com.hpe.amce.translation.impl.OnParWithLegacyTest.class.name + (".in" if isIn else "") + "." + String.invokeMethod("valueOf", [])])


        def doCall(self):
            return self.doCall(None)


    class ClosureAnonymousInnerClass3(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, decorator):
            # Force legacy metric names
            return decorator.incomingBatchCountMetricName = ClosureAnonymousInnerClass6(self, DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this, decorator)

        class ClosureAnonymousInnerClass6(Closure):


            def __init__(self, outerInstance, self, self, decorator):
                super().__init__(self, self)
                self._outerInstance = outerInstance
                self._decorator = decorator

            def doCall(self, it):
                return String.invokeMethod("valueOf", [self._decorator.metricsBaseName]) + ".batches"

            def doCall(self):
                return self.doCall(None)



    def doCall(self):
        return doCall(None)

}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
)));
}

def setup(self):
    self._metricRegistry = MetricRegistry()
    self._listAppender.invokeMethod("clear", [])

def simple_case_with_context(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    given:
    map = LinkedHashMap(3)
    map.put("pre", ClosureAnonymousInnerClass(self))
    map.put("trans", ClosureAnonymousInnerClass2(self))
    map.put("post", ClosureAnonymousInnerClass3(self))
    self._instance = createInstance(map)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    when:
    map1 = LinkedHashMap(1)
    map1.put("param", "ems")
    translated = self._instance.invokeMethod("translateBatch", [list(java.util.Arrays.asList(com.hpe.amce.translation.impl.OnParWithLegacyTest.RawEvent())), com.hpe.amce.translation.impl.OnParWithLegacyTest.Context(map1)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    then:
    assert translated
    assert translated.invokeMethod("size", []) == 1
    assert translated.getAt(0) and isinstance(translated.getAt(0), com.hpe.amce.translation.impl.OnParWithLegacyTest.TranslatedEvent)

class ClosureAnonymousInnerClass(Closure):

    def __init__(self, outerInstance):
        super().__init__(outerInstance, outerInstance)
        self._outerInstance = outerInstance

    def doCall(self, event, context):
        assert event and isinstance(event, com.hpe.amce.translation.impl.OnParWithLegacyTest.RawEvent)
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        assert (context is None ? None : context.getParam()) == "ems";
        return [event]


class ClosureAnonymousInnerClass2(Closure):

    def __init__(self, outerInstance):
        super().__init__(outerInstance, outerInstance)
        self._outerInstance = outerInstance

    def doCall(self, raw, context):
        assert raw and isinstance(raw, com.hpe.amce.translation.impl.OnParWithLegacyTest.RawEvent)
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        assert (context is None ? None : context.getParam()) == "ems";
        return [com.hpe.amce.translation.impl.OnParWithLegacyTest.TranslatedEvent()]


class ClosureAnonymousInnerClass3(Closure):

    def __init__(self, outerInstance):
        super().__init__(outerInstance, outerInstance)
        self._outerInstance = outerInstance

    def doCall(self, event, context):
        assert event and isinstance(event, com.hpe.amce.translation.impl.OnParWithLegacyTest.TranslatedEvent)
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        assert (context is None ? None : context.getParam()) == "ems";
        return [event]


def context_is_optional(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    given:
    map = LinkedHashMap(3)
    map.put("pre", ClosureAnonymousInnerClass4(self))
    map.put("trans", ClosureAnonymousInnerClass5(self))

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
