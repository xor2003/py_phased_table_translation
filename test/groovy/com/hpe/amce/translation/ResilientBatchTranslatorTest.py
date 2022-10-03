//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

import math

class ResilientBatchTranslatorTest(Specification):
    def setup(self):
        instance = ((ResilientBatchTranslator()))
        instance.name = invokeMethod("getClass", []).name
        instance.traceLevel = Level.INFO
        instance.metricRegistry = MetricRegistry()
        listAppender.invokeMethod("clear", [])

    def simple_case_with_context(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        map = LinkedHashMap(3)
        map.put("pre", ClosureAnonymousInnerClass41(self))
        map.put("trans", ClosureAnonymousInnerClass42(self))
        map.put("post", ClosureAnonymousInnerClass43(self))
        instance.processingStages = map
        instance.invokeMethod("lookupLoggers", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        map1 = LinkedHashMap(1)
        map1.put("param", "ems")
        translated = instance.invokeMethod("translateBatch", [list(java.util.Arrays.asList(com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent())), com.hpe.amce.translation.ResilientBatchTranslatorTest.Context(map1)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        assert translated
        assert translated.invokeMethod("size", []) == 1
        assert translated.getAt(0) and isinstance(translated.getAt(0), com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent)

    class ClosureAnonymousInnerClass41(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, event, context):
            assert event and isinstance(event, com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent)
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
            assert (context is None ? None : context.getParam()) == "ems";
            return [event]


    class ClosureAnonymousInnerClass42(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, raw, context):
            assert raw and isinstance(raw, com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent)
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
            assert (context is None ? None : context.getParam()) == "ems";
            return [com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent()]


    class ClosureAnonymousInnerClass43(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, event, context):
            assert event and isinstance(event, com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent)
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
            assert (context is None ? None : context.getParam()) == "ems";
            return [event]


    def context_is_optional(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        map = LinkedHashMap(3)
        map.put("pre", ClosureAnonymousInnerClass44(self))
        map.put("trans", ClosureAnonymousInnerClass45(self))
        map.put("post", ClosureAnonymousInnerClass46(self))
        instance.processingStages = map
        instance.invokeMethod("lookupLoggers", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        translated = instance.invokeMethod("translateBatch", [list(java.util.Arrays.asList(com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent()))])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        assert translated
        assert translated.invokeMethod("size", []) == 1
        assert translated.getAt(0) and isinstance(translated.getAt(0), com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent)

    class ClosureAnonymousInnerClass44(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, event, context):
            assert event and isinstance(event, com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent)
            assert not context
            return [event]


    class ClosureAnonymousInnerClass45(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, raw, context):
            assert raw and isinstance(raw, com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent)
            assert not context
            return [com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent()]


    class ClosureAnonymousInnerClass46(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, event, context):
            assert event and isinstance(event, com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent)
            assert not context
            return [event]


    def errors_on_elements_are_ignored(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        map = LinkedHashMap(3)
        map.put("pre", ClosureAnonymousInnerClass47(self))
        map.put("trans", ClosureAnonymousInnerClass48(self))
        map.put("post", ClosureAnonymousInnerClass49(self))
        instance.processingStages = map
        instance.invokeMethod("lookupLoggers", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        map1 = LinkedHashMap(1)
        map1.put("num", 1)
        map2 = LinkedHashMap(1)
        map2.put("num", 2)
        map3 = LinkedHashMap(1)
        map3.put("num", 3)
        map4 = LinkedHashMap(1)
        map4.put("num", 4)
        map5 = LinkedHashMap(1)
        map5.put("param", "ems")
        translated = instance.invokeMethod("translateBatch", [list(java.util.Arrays.asList(com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent(map1), com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent(map2), com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent(map3), com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent(map4))), com.hpe.amce.translation.ResilientBatchTranslatorTest.Context(map5)]).invokeMethod("asType", [com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        assert translated
        assert translated.invokeMethod("size", []) == 1

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
