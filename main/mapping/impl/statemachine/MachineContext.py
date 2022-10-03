#*
# * Intermediate state of a state machine as we transition between states.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class MachineContext extends GroovyObjectSupport
class MachineContext(GroovyObjectSupport):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._resultValue = None
        self._error = None

    def getResultValue(self):
        return self._resultValue

    def setResultValue(self, resultValue):
        self._resultValue = resultValue

    def getError(self):
        return self._error

    def setError(self, error):
        self._error = error

    #    *
    #     * Current result.
    #     
    #    *
    #     * An error that has happened.
    #     
