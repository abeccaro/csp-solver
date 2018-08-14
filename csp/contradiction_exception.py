class ContradictionException(Exception):
    """Exception raised for any Contradiction (unfeasability) happening during propagation or assignments.
    
    :param message: The message to print
    :type message: str
    """
    
    def __init__(self, message):
        self.message = message


    def __str(self):
        return 'ContradictionException: ' + self.message
