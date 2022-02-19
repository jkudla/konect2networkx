import requests
import shutil
import networkx as nx

from .Loader import *
from .Parser import *
from .exceptions import *

def log(message, logging):
    if logging:
        print('[KONECT2NetworkX] {message}'.format(message = message))

def download_network(id, logging = True):
    # Perform download via HTTP
    url = 'http://konect.cc/files/download.tsv.{id}.tar.bz2'.format(id = id)
    filename = '{id}.tar.bz2'.format(id = id)

    log('Attemping to download network to {filename}'.format(filename = filename), logging)

    try:
        res = requests.get(url, allow_redirects = True)
    except requests.exceptions.RequestException:
        raise RetrieveException('failed downloading the network with id {id}'.format(id = id))
    else:
        if res.ok:
            log('HTTP request successful, writing network to {filename}'.format(filename = filename), logging)
            try:
                open(filename, 'wb').write(res.content)
                shutil.unpack_archive(filename)
                log('Network successfully unpacked!', logging)
            except (IOError, ValueError):
                raise RetrieveException('failed unpacking network {id}'.format(id = id))
        else:
            raise RetrieveException('failed downloading the network with id {id}'.format(id = id))


def get(id, download = True, logging = True):
    if download:
        log('Downloading network {id}'.format(id = id), logging)
        download_network(id) # might raise RetrieveException  (which is fine)
    else:
        log('Skipping download', logging)

    lines = None
    try:
        log('Seeking main network file', logging)
        loader = Loader(id)
        filepath = loader.seek_out_file()
        file = open(filepath, 'r')

        # file = open('{id}/out.{id}'.format(id = id), 'r')
        # log('Main network file found under standard name {id}/out.{id}'.format(id = id), logging)
        lines = file.read().splitlines()
        file.close()
        if len(lines) < 2:
            raise LoadException('network file for network {id} too short'.format(id = id))
    except (IOError, EOFError):
        raise LoadException('failed reading network {id} from file'.format(id = id))
    else:
        log('Main network file successfully read, launching parser', logging)
        p = Parser(lines, logging)
        return p.parse() # go!
