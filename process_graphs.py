import json
import os

import networkx as nx

for folder in os.listdir(os.getcwd()):
    if not os.path.isdir(folder):  # Loop over MS system folders
        continue
    for commit in os.listdir(folder):
        commit_path = os.path.join(folder, commit)
        if not os.path.isdir(commit_path):  # Loop over commit folders
            continue
        for file in os.listdir(commit_path):
            if file.endswith("_json_architecture.json"):  # Get the json format
                file_path = os.path.join(commit_path, file)
                with open(file_path, 'r') as f:
                    g = json.load(f)
                g = {
                    "nodes": g["microservices"] + g["external_components"],  # Merge all nodes
                    "edges": g["information_flows"]
                }
                G = nx.node_link_graph(g, edges="edges", nodes="nodes", name="name", source="sender", target="receiver",
                       multigraph=False, directed=True)  # Load the graph

                # Filter Greatest Weakly connected component
                gcc = max(nx.weakly_connected_components(G), key=len)  # Get the nodes in the weakly g.c.c.
                not_gcc = set(G.nodes()) - set(gcc)  # Get the set of nodes that are not in the g.c.c
                G.remove_nodes_from(not_gcc)  # Keep only the g.c.c.
                g = nx.node_link_data(G, edges="edges", nodes="nodes", name="name", source="sender", target="receiver")
                del g["multigraph"]
                del g["directed"]
                del g["graph"]
                name = file.split("_json_")[0]
                with open(f"{name}_gwcc.json", 'w') as f:
                    json.dump(g, f, indent=4, sort_keys=True)

                # Remove DB only connected to own service
                nodes = set(G.nodes)
                for node in nodes:
                    if ("mongo" in node or "database" in node) and G.in_degree(node)+G.out_degree(node) == 1:
                        G.remove_node(node)
                g = nx.node_link_data(G, edges="edges", nodes="nodes", name="name", source="sender", target="receiver")
                del g["multigraph"]
                del g["directed"]
                del g["graph"]
                with open(f"{name}_gwcc_noDB.json", 'w') as f:
                    json.dump(g, f, indent=4, sort_keys=True)
