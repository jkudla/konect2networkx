class ParseException(Exception):
    """Raised when parser encounters malformed TSV file"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class RetrieveException(Exception):
    """Raised when downloading or unpacking network fails"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        

class LoadException(Exception):
    """Raised when loading network from directory fails"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
