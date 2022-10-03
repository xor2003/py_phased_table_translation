#*
# * Ends processing.
# * Does not need to be configured.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class End extends AbstractState
class End(AbstractState):
    def process(self, field, mappingContext, machineContext):
        return ((machineContext.resultValue))

    def isDefined(self, field):
        return True

