import os
from .Loader import Loader
from .exceptions import LoadException

class DiskLoader(Loader):

    def __init__(self, id):
        super().__init__(id)


    def load_network(self):
        lines = None
        # log('Seeking main network file', logging)
        filepath = self.seek_out_file()
        try:
            file = open(filepath, 'r')
            lines = file.read().splitlines()
            file.close()
        except (IOError, EOFError):
            raise LoadException('failed reading network {id} from file'.format(id = self.id))
        else:
            if len(lines) < 2:
                raise LoadException('network file for network {id} too short'.format(id = self.id))
            return lines


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

        raise LoadException('failed seeking main network file on disk') # give up
