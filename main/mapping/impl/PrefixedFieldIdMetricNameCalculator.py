#*
# * Uses field identifier as metric name.
# * <p>
# * This metric name calculator create a metric for each field allowing
# * to track how much time it takes to map each field.
# 


class PrefixedFieldIdMetricNameCalculator(MetricNameCalculator):
    #    *
    #     * Creates instance.
    #     *
    #     :param prefix: Prefix for metric names.
    #     


    def __init__(self, prefix):

        self._prefix = None

        self._prefix = prefix

    class WarnAnonymousInnerClass2(Warn):
        def __init__(self, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)



        def createMessage(self, field, mappingContext, machineContext):
            return (str((messageFormatter.invokeMethod("formatMessage", [mappingContext, field, "Input value is invalid: \'" + String.invokeMethod("valueOf", []) + "\'"]))))


    class WarnAnonymousInnerClass3(Warn):

        def __init__(self, outerInstance, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self.outerInstance = outerInstance



        def createMessage(self, field, mappingContext, machineContext):
            return (str((messageFormatter.invokeMethod("formatMessage", [mappingContext, field, "Input value cannot be validated: \'" + String.invokeMethod("valueOf", []) + "\'"]))))


    class WarnAnonymousInnerClass(Warn):

        def __init__(self, outerInstance, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self.outerInstance = outerInstance



        def createMessage(self, field, mappingContext, machineContext):
            return (str((messageFormatter.invokeMethod("formatMessage", [mappingContext, field, "Input value cannot be mapped: \'" + String.invokeMethod("valueOf", []) + "\'"]))))




    def calculateMetricName(self, field, mappingContext):
        return (str((self._prefix + field.id)))

