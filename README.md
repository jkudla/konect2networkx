# KONECT2NetworkX
![](https://github.com/jkudla/konect2networkx/workflows/Unit%20Tests/badge.svg)

## Bridging the gap between KONECT and NetworkX
The [KONECT project](http://konect.cc/) (Koblenz Network Collection) has

> the goal to collect network datasets, analyse them, and make available all analyses online.

This project, KONECT2NetworkX, aims to make these network datasets even more accessible and easier to use by providing a Python package that transforms them into [NetworkX](https://networkx.org/) graph objects. To this end, KONECT2NetworkX features functions to download networks by their names given on the KONECT website and parse them into NetworkX graph objects.

### Example
Suppose we want to download a network, use NetworkX to draw it and save the figure to a PNG file. This merely requires three lines of essential code, each line doing of the steps.
```python
import networkx as nx
import konect2networkx as k2n
import matplotlib.pyplot as plt

G = k2n.get('ucidata-zachary') # get the Zachary karate club network
nx.draw(G)
plt.savefig('karate.png', format = 'PNG')
```
For reference, the Zachary karate club network can be found [here](http://konect.cc/networks/ucidata-zachary/).

With logging enabled, the console output will look like this:
```
[KONECT2NetworkX] Downloading network ucidata-zachary
[KONECT2NetworkX] Attemping to download network to ucidata-zachary.tar.bz2
[KONECT2NetworkX] HTTP request successful, writing network to ucidata-zachary.tar.bz2
[KONECT2NetworkX] Network successfully unpacked!
[KONECT2NetworkX] Seeking main network file
[KONECT2NetworkX] Main network file found under standard name ucidata-zachary/out.ucidata-zachary
[KONECT2NetworkX] Main network file successfully read, launching parser
[KONECT2NetworkX] Network metadata parsed: unipartite, undirected, unweighted, no multigraph
[KONECT2NetworkX] Parsing size information
[KONECT2NetworkX] Network has 34 nodes and 78 edges in total
[KONECT2NetworkX] Building NetworkX graph object
[KONECT2NetworkX] NetworkX graph object built
```

### Installation
Clone this repository:
```
git clone https://github.com/jkudla/konect2networkx
```
Navigate into the resulting directory and install the package using pip:
```
pip install -e .
```
Voilà – now you should be able to use KONECT2NetworkX just like in the example above :)

**Note**: This package will shortly be published on PyPI.

## Documentation
All features are encapsulated in just two functions.

### Downloading Networks
```python
download_network(id, logging = True)
```
This will download a network from the KONECT website and unpack the archive file. The logging option toggles printing status messages to the standard output. A `RetrieveException` is raised if

+ HTTP request failed (e. g. cannot connect to the KONECT website), or
+ Network with specific ID does not exist, or
+ Archive cannot be unpacked due to IO issues.

The `RetrieveException` comes with a message stating the scenario that applies.

### Getting Networks into NetworkX
```python
get(id, download = True, logging = True)
```
This is where the magic happens! It will parse the specific network from KONECT format to a NetworkX graph object, which is returned upon success. If the download option is enabled (as by default), `download_network` is invoked to first download the network. If the download option is disabled, the function assumes an unpacked network directory is present. The logging option toggles printing status messages to the standard output.

Two exceptions may be raised:
+ `LoadException` if the network file cannot read or is too short such that it cannot contain a network.
+ `ParseException` if the network file is malformed, i. e., does not follow the specification outlined in the [KONECT Handbook](https://raw.githubusercontent.com/kunegis/konect-handbook/master/konect-handbook.pdf).

Both exceptions will contain a message describing the circumstances.


## Contributing
This project has just been launched and any kind of contribution is warmly welcomed. Have a look at the [issue tracker](https://github.com/jkudla/konect2networkx/issues) for bug reports and feature requests.
