class SingleLineMesasgeFormatterTest(Specification):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._formatter = SingleLineMesasgeFormatter()

    def tells_if_field_is_mandatory(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        self._formatter.mandatory = True
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        result = self._formatter.invokeMethod("formatMessage", [invokeMethod("Mock", []), invokeMethod("Mock", []), "message"])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        java.util.regex.Pattern.compile("(?i)mandatory").matcher(result)

    def tells_if_field_is_optional(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        result = self._formatter.invokeMethod("formatMessage", [invokeMethod("Mock", []), invokeMethod("Mock", []), "message"])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        java.util.regex.Pattern.compile("(?i)optional").matcher(result)

    def dumps_all_info(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        mappingContext = invokeMethod("Mock", [])
        field = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        result = self._formatter.invokeMethod("formatMessage", [mappingContext, field, "message"])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        1 * mappingContext.originalObject >> "original"
        1 * mappingContext.parameters >> "parameters"
        1 * field.id >> "fieldId"
        result.invokeMethod("contains", ["original"])
        result.invokeMethod("contains", ["parameters"])
        result.invokeMethod("contains", ["fieldId"])
        return result.invokeMethod("contains", ["message"])

    def produces_single_line(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        result = self._formatter.invokeMethod("formatMessage", [invokeMethod("Mock", []), invokeMethod("Mock", []), "message"])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        result.invokeMethod("readLines", []).invokeMethod("size", []) == 1

    def getFormatter(self):
        return self._formatter

    def setFormatter(self, formatter):
        self._formatter = formatter

