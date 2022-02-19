import os
from .exceptions import LoadException

class Loader:

    def __init__(self, id):
        self.id = id

    def seek_out_file(self):
        if os.path.isfile('{id}/out.{id}'.format(id = self.id)):
            return '{id}/out.{id}'.format(id = self.id) # file found under standard path

        # If not under standard path, search through directory
        # Goal: Find file prefixed "out."

        dir = os.fsencode('{id}'.format(id = self.id))
        for file in os.listdir(dir):
            filename = os.fsdecode(file)
            if filename.startswith('out.'):
                return os.path.join(dir, file) # successful

        raise LoadException('failing seeking main network file') # give up
