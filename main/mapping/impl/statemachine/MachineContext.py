class MachineContext:
    """
    Intermediate state of a state machine as we transition between states.
    """

    def __init__(self):
        """
        Current result.

        An error that has happened.
        """
        self.resultValue = None
        self.error = None
