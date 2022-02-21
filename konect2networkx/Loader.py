from zipfile import ZipFile
from .exceptions import LoadException

class Loader:

    def __init__(self, id):
        self.id = id

    def load_network(self):
        pass

    def load_network_metadata(self):
        pass
