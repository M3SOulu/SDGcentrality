import os
import json

import networkx as nx
import pandas as pd

all_dfs = []
for file in os.listdir(os.getcwd()):
    if not file.endswith("noDB.json"):
        continue
    name = file.split('--')[0]
    with open(file, 'r') as f:
        g = json.load(f)
    G = nx.node_link_graph(g, edges="edges", nodes="nodes", name="name", source="sender", target="receiver",
                           multigraph=False, directed=True)  # Load the graph

    graph_df = pd.DataFrame(columns=["MS_system", "node"])
    for node in G.nodes:
        graph_df.loc[len(graph_df)] = [name, node]
    graph_df["degree_centrality"] = graph_df["node"].map(nx.degree_centrality(G))
    graph_df["in_degree_centrality"] = graph_df["node"].map(nx.in_degree_centrality(G))
    graph_df["out_degree_centrality"] = graph_df["node"].map(nx.out_degree_centrality(G))
    graph_df["eigenvector_centrality"] = graph_df["node"].map(nx.eigenvector_centrality(G, max_iter=1000))
    graph_df["closeness_centralty"] = graph_df["node"].map(nx.closeness_centrality(G))
    graph_df["betweenness_centrality"] = graph_df["node"].map(nx.betweenness_centrality(G))
    graph_df["load_centrality"] = graph_df["node"].map(nx.load_centrality(G))
    graph_df["harmonic_centrality"] = graph_df["node"].map(nx.harmonic_centrality(G))
    G = nx.Graph(G)
    graph_df["information_centrality"] = graph_df["node"].map(nx.current_flow_closeness_centrality(G))
    graph_df["currrent_flow_centrality"] = graph_df["node"].map(nx.current_flow_betweenness_centrality(G))
    graph_df["subgraph_centrality"] = graph_df["node"].map(nx.subgraph_centrality(G))

    all_dfs.append(graph_df)

all_dfs = sorted(all_dfs, key=lambda d: d["MS_system"].iloc[0].casefold())
df = pd.concat(all_dfs)
df.to_csv("centrality_metrics.csv", index=False, header=True)