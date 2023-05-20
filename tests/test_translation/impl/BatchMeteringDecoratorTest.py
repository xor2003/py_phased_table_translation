//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

class BatchMeteringDecoratorTest(Specification):
    def delegates_and_publishes_metrics(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        baseName = invokeMethod("getClass", []).name
        decorated = invokeMethod("Mock", [])
        metricRegistry = MetricRegistry()
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final List<Boolean> context = (List<Boolean>) new ArrayList<Boolean>(java.util.Arrays.asList(true));
        context = list(java.util.Arrays.asList(True))
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final List<List<String>> original = (List<List<String>>) new ArrayList<List<String>>(java.util.Arrays.asList(new ArrayList<String>(java.util.Arrays.asList("1", "2", "3", "4")), new ArrayList<String>(java.util.Arrays.asList("5", "6", "7")), new ArrayList<String>(java.util.Arrays.asList("8", "9"))));
        original = list(java.util.Arrays.asList(list(java.util.Arrays.asList("1", "2", "3", "4")), list(java.util.Arrays.asList("5", "6", "7")), list(java.util.Arrays.asList("8", "9"))))
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final BatchMeteringDecorator<String, Integer, List<Boolean>> instance = (BatchMeteringDecorator<String, Integer, List<Boolean>>) new BatchMeteringDecorator<>(decorated, metricRegistry, baseName);
        instance = BatchMeteringDecorator(decorated, metricRegistry, baseName)
        result = original.invokeMethod("collect", [ClosureAnonymousInnerClass15(self, context, instance)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        "returns result from delegate"
        decorated.invokeMethod("translateBatch", [_, _]) >> ClosureAnonymousInnerClass16(self)
        result is original.invokeMethod("collect", [ClosureAnonymousInnerClass17(self)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        "publishes 'Received number of batches - meter' using base name"
        metricRegistry.invokeMethod("meter", [baseName + ".batches.count"]).count == original.invokeMethod("size", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        "publishes 'Size of incoming batches - histogram' using base name"
        metricRegistry.invokeMethod("histogram", [baseName + ".in.batch_size"]).invokeMethod("with", [ClosureAnonymousInnerClass18(self, original)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        "publishes 'Total number of incoming elements across all batches - meter' using base name"
        metricRegistry.invokeMethod("meter", [baseName + ".in.events"]).count == original.invokeMethod("size", []).invokeMethod("sum", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        "publishes 'Time it takes to translate a batch - timer' using base name"
        metricRegistry.invokeMethod("timer", [baseName + ".translate_batch"]).count == original.invokeMethod("size", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        "publishes 'Size of resulting batches - histogram' using base name"
        metricRegistry.invokeMethod("histogram", [baseName + ".out.batch_size"]).invokeMethod("with", [ClosureAnonymousInnerClass19(self, original)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        "publishes 'Total number of resulting elements across all batches - meter' using base name"
        return metricRegistry.invokeMethod("meter", [baseName + ".out.events"]).count == original.invokeMethod("size", []).invokeMethod("sum", []) + original.invokeMethod("size", [])

    class ClosureAnonymousInnerClass(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, event, params):
            if event.getNum() == 1.asBoolean():
                npe = None
                npe.invokeMethod("trim", [])

            return [event]


    class ClosureAnonymousInnerClass2(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, event, params):
            if event.getNum() == 2.asBoolean():
                assert False

            map1 = LinkedHashMap(1)
            map1.put("num", event.num)
            return [com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent(map1)]


    class ClosureAnonymousInnerClass3(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, event, params):
            if event.getNum() == 3.asBoolean():
                (File("/ d o e s n o t e x i s t _ @ # ! \$ , :")).invokeMethod("getText", [])

            return [event]


    class ClosureAnonymousInnerClass4(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, raw, context):
            map1 = LinkedHashMap(1)
            map1.put("num", raw.num + 1)
            return [com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent(map1)]


    class ClosureAnonymousInnerClass5(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, raw, context):
            map1 = LinkedHashMap(1)
            map1.put("num", raw.num + 1)
            return [com.hpe.amce.translation.ResilientBatchTranslatorTest.RawEvent(map1)]


    class ClosureAnonymousInnerClass6(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, raw, context):
            map1 = LinkedHashMap(1)
            map1.put("num", raw.num + 1)
            return [com.hpe.amce.translation.ResilientBatchTranslatorTest.TranslatedEvent(map1)]


    class ClosureAnonymousInnerClass7(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return it.loggerName.invokeMethod("startsWith", [getInstance().name])

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass8(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return it.level == getInstance().traceLevel

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass9(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return it.message.formattedMessage.invokeMethod("contains", ["ems"])

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass10(Closure):


//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
