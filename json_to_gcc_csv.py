import json

import networkx as nx

VERSIONS = ["v0.0.1", "v0.0.2", "v0.0.3", "v0.0.4", "v0.1.0", "v0.2.0", "v1.0.0"]
for v in VERSIONS:
    with open(f"train-ticket-releases/{v}.json", 'r') as f:
        g = json.load(f)
    G = nx.node_link_graph(g, edges="edges", nodes="nodes", name="name", source="sender", target="receiver",
                           multigraph=False, directed=True)
    gcc = max(nx.weakly_connected_components(G), key=len)  # Get the nodes in the weakly g.c.c.
    not_gcc = set(G.nodes()) - set(gcc)  # Get the set of nodes that are not in the g.c.c
    G.remove_nodes_from(not_gcc)  # Keep only the g.c.c.
    g = nx.node_link_data(G, edges="edges", nodes="nodes", name="name", source="sender", target="receiver")
    del g["multigraph"]
    del g["directed"]
    del g["graph"]
    with open(f"train-ticket-releases/{v}gcc.json", 'w') as f:
        json.dump(g, f, indent=4)