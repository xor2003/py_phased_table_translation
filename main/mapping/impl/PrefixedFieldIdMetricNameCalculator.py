#*
# * Uses field identifier as metric name.
# * <p>
# * This metric name calculator create a metric for each field allowing
# * to track how much time it takes to map each field.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class PrefixedFieldIdMetricNameCalculator<OO, RO, P> extends GroovyObjectSupport implements MetricNameCalculator<OO, RO, P>
class PrefixedFieldIdMetricNameCalculator(GroovyObjectSupport, MetricNameCalculator):
    #    *
    #     * Creates instance.
    #     *
    #     * @param prefix Prefix for metric names.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public PrefixedFieldIdMetricNameCalculator(@Nonnull String prefix)
    def __init__(self, prefix):
        #instance fields found by Java to Python Converter:
        self._prefix = None

        self._prefix = prefix

    class WarnAnonymousInnerClass2(Warn):
        def __init__(self, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: @Override protected String createMessage(Field field, MappingContext mappingContext, final MachineContext machineContext)
        def createMessage(self, field, mappingContext, machineContext):
            return (str((messageFormatter.invokeMethod("formatMessage", [mappingContext, field, "Input value is invalid: \'" + String.invokeMethod("valueOf", []) + "\'"]))))


    class WarnAnonymousInnerClass3(Warn):

        def __init__(self, outerInstance, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self.outerInstance = outerInstance

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: @Override protected String createMessage(Field field, MappingContext mappingContext, final MachineContext machineContext)
        def createMessage(self, field, mappingContext, machineContext):
            return (str((messageFormatter.invokeMethod("formatMessage", [mappingContext, field, "Input value cannot be validated: \'" + String.invokeMethod("valueOf", []) + "\'"]))))


    class WarnAnonymousInnerClass(Warn):

        def __init__(self, outerInstance, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self.outerInstance = outerInstance

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: @Override protected String createMessage(Field field, MappingContext mappingContext, final MachineContext machineContext)
        def createMessage(self, field, mappingContext, machineContext):
            return (str((messageFormatter.invokeMethod("formatMessage", [mappingContext, field, "Input value cannot be mapped: \'" + String.invokeMethod("valueOf", []) + "\'"]))))


#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public String calculateMetricName(@Nonnull Field field, @Nonnull MappingContext mappingContext)
    def calculateMetricName(self, field, mappingContext):
        return (str((self._prefix + field.id)))

