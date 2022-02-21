import io
import tarfile

from .Loader import Loader
from .exceptions import LoadException

class MemLoader(Loader):

    def __init__(self, id, zip):
        super().__init__(id)
        self.zip = zip


    def load_network(self):
        lines = self.extract_zip().splitlines()
        if len(lines) < 2:
            raise LoadException('network file for network {id} too short'.format(id = self.id))
        return lines # done :-)


    def extract_zip(self):
        tf = tarfile.open(mode = 'r:bz2', fileobj = io.BytesIO(self.zip))
        mainfilename = None
        standardfilename = '{id}/out.{id}'.format(id = self.id)

        if standardfilename in tf.getnames():
            mainfilename = standardfilename
        else:
            for filename in tf.getnames():
                if 'out.' in filename:
                    mainfilename = filename
                    break

        if mainfilename == None:
            raise LoadException('failed seeking main network file in archive')

        outfile = tf.extractfile(mainfilename.format(id = self.id))
        outfile.seek(0)
        return outfile.read().decode('UTF-8')
