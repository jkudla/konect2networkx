import networkx as nx

class Parser:
    """
    This is where the magic happens!

    Attributes:
        file_contents   Stores the entire network file in memory
        logging         Stores whether printed status messages are desired
        metadata        Information from 1st line of the network file
        bipartite       Whether the graph is bipartite or not
        directed        Whether the graph is directed or not
        weighted        Whether the graph has edge weights or not
        multigraph      Whether multiple edges between nodes or permitted or not
        m               Number of edges
        n               Number of nodes
        nleft           Number of nodes in left partition (or total number of nodes if not bipartite)
        nright          Number of right in right partition (or total number of nodes if not bipartite)
        payload         Actual description of the graph's structure (i. e. edge list)
    """


    def __init__(self, file_contents, logging = True):
        self.file_contents = file_contents
        self.logging = logging

    """ Used to print status messages """
    def log(self, message):
        if self.logging:
            print('[Parser] {message}'.format(message = message))

    """ Contructs the networkx graph, invoked by parse """
    def build_graph(self):
        G = None
        if self.multigraph:
            if self.directed:
                G = nx.MultiDiGraph()
            else:
                G = nx.MultiGraph()
        else:
            if self.directed:
                G = nx.DiGraph()
            else:
                G = nx.Graph()

        if self.bipartite:
            # if bipartite, partitions are [1..nleft] and [nleft+1..n]
            G.add_nodes_from(range(1, self.nleft + 1), bipartite = 0)
            G.add_nodes_from(range(self.nleft + 1, self.n + 1), bipartite = 1)
        else:
            G.add_nodes_from(range(1, self.n + 1))

        for edge in self.payload:
            edge = edge.split(' ')
            x = int(edge[0])
            y = int(edge[1])
            w = None
            if self.weighted:
                w = float(edge[2]) # TODO: maybe introduce option to enforce integral weights

            if self.bipartite:
                G.add_edge(x, y + self.nleft, weight = w) # node transform in bipartite case
            else:
                G.add_edge(x, y, weight = w)

        return G

    """
    Launches the parsing process
    1) Gather general information (metadata, size etc.) of the network
    2) Get everything ready for build_graph to construct the networkx graph
    """
    def parse(self):
        lines = self.file_contents
        self.metadata = lines[0].split(' ')
        self.bipartite = 'bip' in self.metadata;
        self.directed = 'asym' in self.metadata;

        multigraph_types = ['positive', 'multisigned', 'multiweighted', 'dynamic', 'multiposweighted']
        weighted_types = ['posweighted', 'signed', 'multisigned', 'weighted', 'multiweighted', 'multiposweighted']
        for d in self.metadata:
            self.multigraph = d in multigraph_types
            self.weighted = d in weighted_types

        sizedata = lines[1].split(' ')
        self.m = int(sizedata[1])
        self.nleft = int(sizedata[2])
        self.nright = int(sizedata[3])

        if self.bipartite:
            self.n = self.nleft + self.nright
        else:
            self.n = self.nleft

        self.payload = lines[2:]

        return self.build_graph()
