#*
# * Obtains default value.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class Defaulter extends AbstractState
class Defaulter(AbstractState):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: @Override public Object process(final Field field, final MappingContext mappingContext, MachineContext machineContext)
    def process(self, field, mappingContext, machineContext):
        return ((invokeMethod("safely", [field, mappingContext, machineContext, True, ClosureAnonymousInnerClass(self, field, mappingContext)])))

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, field, mappingContext):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._field = field
            self._mappingContext = mappingContext

        def doCall(self, it):
            return invokeMethod("callWithDelegate", [self._field.defaulter, self._mappingContext])

        def doCall(self):
            return self.doCall(None)


    def isDefined(self, field):
        return field.defaulter is not None

