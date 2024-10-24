import networkx as nx

import json

VERSIONS = ["v0.0.1", "v0.0.2", "v0.0.3", "v0.0.4", "v0.1.0", "v0.2.0", "v1.0.0"]
for v in VERSIONS:
    with open(f"train-ticket-releases/{v}gcc.json", 'r') as f:
        g = json.load(f)
    G = nx.node_link_graph(g, edges="edges", nodes="nodes", name="name", source="sender", target="receiver",
                           multigraph=False, directed=True)
    nodes = set(G.nodes)
    for node in nodes:
        if ("mongo" in node or "database" in node) and G.in_degree(node)+G.out_degree(node) == 1:
            G.remove_node(node)
    g = nx.node_link_data(G, edges="edges", nodes="nodes", name="name", source="sender", target="receiver")
    del g["multigraph"]
    del g["directed"]
    del g["graph"]
    with open(f"train-ticket-releases/{v}gcc_nodb.json", 'w') as f:
        json.dump(g, f, indent=4)