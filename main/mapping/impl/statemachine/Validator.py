#*
# * Validates result value.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class Validator extends AbstractState
class Validator(AbstractState):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: @Override public Object process(final Field field, final MappingContext mappingContext, final MachineContext machineContext)
    def process(self, field, mappingContext, machineContext):
        return ((invokeMethod("safely", [field, mappingContext, machineContext, False, ClosureAnonymousInnerClass(self, field, mappingContext, machineContext)])))

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, field, mappingContext, machineContext):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._field = field
            self._mappingContext = mappingContext
            self._machineContext = machineContext

        def doCall(self, it):
            return invokeMethod("callWithDelegate", [self._field.validator, self._mappingContext, self._machineContext.resultValue])

        def doCall(self):
            return self.doCall(None)


    def isDefined(self, field):
        return field.validator is not None

    def isNull(self, value):
        return (bool(((not value))))
