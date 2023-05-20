//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

class SimpleObjectMapperTest(Specification):
    def delegates_to_optional_mapper_for_optional_field(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        field = Field()
        map = LinkedHashMap(1)
        map.put(field, False)
        fields = map
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object input = invokeMethod("Mock", new Object[0]);
        input = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object result = invokeMethod("Mock", new Object[0]);
        result = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object parameters = invokeMethod("Mock", new Object[0]);
        parameters = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        objectMapper.invokeMethod("mapAllFields", [input, result, fields, parameters])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        1 * optionalFieldMapper.invokeMethod("mapField", [field, ClosureAnonymousInnerClass(self, input, result, parameters)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        0 * _

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, input, result, parameters):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._input = input
            self._result = result
            self._parameters = parameters

        def doCall(self, context):
            return context is not None and context.parameters is self._parameters and context.originalObject is self._input and context.resultObject is self._result


    def delegates_to_mandatory_mapper_for_mandatory_field(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        field = Field()
        map = LinkedHashMap(1)
        map.put(field, True)
        fields = map
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object input = invokeMethod("Mock", new Object[0]);
        input = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object result = invokeMethod("Mock", new Object[0]);
        result = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object parameters = invokeMethod("Mock", new Object[0]);
        parameters = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        objectMapper.invokeMethod("mapAllFields", [input, result, fields, parameters])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        1 * mandatoryFieldMapper.invokeMethod("mapField", [field, ClosureAnonymousInnerClass2(self, input, result, parameters)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        0 * _

    class ClosureAnonymousInnerClass2(Closure):


        def __init__(self, outerInstance, input, result, parameters):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._input = input
            self._result = result
            self._parameters = parameters

        def doCall(self, context):
            return context is not None and context.parameters is self._parameters and context.originalObject is self._input and context.resultObject is self._result


    def processes_all_fields_in_specified_order(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        field1 = (Field()).invokeMethod("withId", ["b"])
        field2 = (Field()).invokeMethod("withId", ["c"])
        field3 = (Field()).invokeMethod("withId", ["a"])
        map = LinkedHashMap(3)
        map.put(field1, True)
        map.put(field2, False)
        map.put(field3, True)
        fields = map
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object input = invokeMethod("Mock", new Object[0]);
        input = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object result = invokeMethod("Mock", new Object[0]);
        result = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Object parameters = invokeMethod("Mock", new Object[0]);
        parameters = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        objectMapper.invokeMethod("mapAllFields", [input, result, fields, parameters])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        1 * mandatoryFieldMapper.invokeMethod("mapField", [field1, ClosureAnonymousInnerClass3(self, input, result, parameters)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        1 * optionalFieldMapper.invokeMethod("mapField", [field2, ClosureAnonymousInnerClass4(self, input, result, parameters)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        1 * mandatoryFieldMapper.invokeMethod("mapField", [field3, ClosureAnonymousInnerClass5(self, input, result, parameters)])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        0 * _

    class ClosureAnonymousInnerClass3(Closure):


        def __init__(self, outerInstance, input, result, parameters):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._input = input
            self._result = result
            self._parameters = parameters

        def doCall(self, context):
            return context is not None and context.parameters is self._parameters and context.originalObject is self._input and context.resultObject is self._result


    class ClosureAnonymousInnerClass4(Closure):


        def __init__(self, outerInstance, input, result, parameters):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._input = input
            self._result = result
            self._parameters = parameters

        def doCall(self, context):
            return context is not None and context.parameters is self._parameters and context.originalObject is self._input and context.resultObject is self._result


    class ClosureAnonymousInnerClass5(Closure):


        def __init__(self, outerInstance, input, result, parameters):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._input = input
            self._result = result
            self._parameters = parameters

        def doCall(self, context):
            return context is not None and context.parameters is self._parameters and context.originalObject is self._input and context.resultObject is self._result


    def uses_default_field_mappers_by_default(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        objectMapper = SimpleObjectMapper()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        isinstance(objectMapper.mandatoryFieldMapper, MandatoryFieldMapper)
        return isinstance(objectMapper.optionalFieldMapper, OptionalFieldMapper)

    def getMandatoryFieldMapper(self):
        return mandatoryFieldMapper

    def setMandatoryFieldMapper(self, mandatoryFieldMapper):
        self.mandatoryFieldMapper = mandatoryFieldMapper

    def getOptionalFieldMapper(self):
        return optionalFieldMapper

    def setOptionalFieldMapper(self, optionalFieldMapper):
        self.optionalFieldMapper = optionalFieldMapper

    def getObjectMapper(self):
        return objectMapper

    def setObjectMapper(self, objectMapper):

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
