import requests
import shutil
import networkx as nx

from .Loader import Loader
from .MemLoader import MemLoader
from .DiskLoader import DiskLoader
from .Parser import *
from .exceptions import *

def log(message, logging):
    if logging:
        print('[KONECT2NetworkX] {message}'.format(message = message))

def download_network(id, store = False, logging = True):
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
            if store:
                # write to disk
                log('HTTP request successful, writing network to {filename}'.format(filename = filename), logging)
                try:
                    open(filename, 'wb').write(res.content)
                    shutil.unpack_archive(filename)
                    log('Network successfully unpacked!', logging)
                except (IOError, ValueError):
                    raise RetrieveException('failed unpacking network {id}'.format(id = id))
            else:
                # keep in memory
                return res.content # further use in get method

        else:
            raise RetrieveException('failed downloading the network with id {id}'.format(id = id))


def get(id, store = False, download = True, logging = True):
    network_zip = None
    loader = None

    if download:
        log('Downloading network {id}'.format(id = id), logging)
        network_zip = download_network(id, store, logging) # might raise RetrieveException  (which is fine)
    else:
        log('Skipping download', logging)


    if store:
        loader = DiskLoader(id)
    elif download:
        loader = MemLoader(id, network_zip)
    else:
        raise LoadException('cannot retrieve network without disk access and without download')

    lines = loader.load_network()
    p = Parser(lines, logging)
    return p.parse() # go!
