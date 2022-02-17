import requests
import shutil
import networkx as nx

from .Parser import *
from .exceptions import *

def download_network(id, logging = True):
    # Perform download via HTTP
    url = 'http://konect.cc/files/download.tsv.{id}.tar.bz2'.format(id = id)
    filename = '{id}.tar.bz2'.format(id = id)

    try:
        res = requests.get(url, allow_redirects = True)
    except requests.exceptions.RequestException:
        raise RetrieveException('failed downloading the network with id {id}'.format(id = id))
    else:
        if res.ok:
            try:
                open(filename, 'wb').write(res.content)
                shutil.unpack_archive(filename)
            except (IOError, ValueError):
                raise RetrieveException('failed unpacking network {id}'.format(id = id))
        else:
            raise RetrieveException('failed downloading the network with id {id}'.format(id = id))


def get(id, download = True, logging = True):
    if download:
        download_network(id) # might raise RetrieveException  (which is fine)

    lines = None
    try:
        file = open('{id}/out.{id}'.format(id = id), 'r')
        lines = file.read().splitlines()
        file.close()
        if len(lines) < 2:
            raise LoadException('network file for network {id} too short'.format(id = id))
    except (IOError, EOFError):
        raise LoadException('failed reading network {id} from file'.format(id = id))
    else:
        p = Parser(lines, logging)
        return p.parse() # go!
