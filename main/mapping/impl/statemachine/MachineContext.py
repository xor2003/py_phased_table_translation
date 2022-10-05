#*
# * Intermediate state of a state machine as we transition between states.
# 

class MachineContext:

    #    *
    #     * Current result.
    #
    #    *
    #     * An error that has happened.
    #
    def __init__(self):
        self.resultValue = None
        self.error = None


