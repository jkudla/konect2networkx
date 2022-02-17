import networkx as nx
import konect2networkx as k2n
import matplotlib.pyplot as plt

G = k2n.get('ucidata-zachary') # get the Zachary karate club network
nx.draw(G)
plt.savefig('karate.png', format = 'PNG')
