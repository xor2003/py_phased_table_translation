class PrefixedFieldIdMetricNameCalculatorTest(Specification):
    def metric_name_is_a_prefixed_field_id(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        instance = PrefixedFieldIdMetricNameCalculator("foo")
        mappingContext = invokeMethod("Mock", [])
        field = Field("moo")
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        result = instance.invokeMethod("calculateMetricName", [field, mappingContext])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        result is "foomoo"

    def survives_not_set_field_id(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        instance = PrefixedFieldIdMetricNameCalculator("foo")
        mappingContext = invokeMethod("Mock", [])
        name = None
        field = Field(name)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        result = instance.invokeMethod("calculateMetricName", [field, mappingContext])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        result.invokeMethod("contains", ["foo"])
        return result is not "foo"

