import os
import json

import networkx as nx
import pandas as pd

all_dfs = []
for project in os.listdir(os.path.join(os.getcwd(), "projects")):
    name = os.path.join(os.getcwd(), "raw_data", "graph", f"{project}_gwcc_noDB.json")
    with open(name, 'r') as f:
        g = json.load(f)
    G = nx.node_link_graph(g, edges="edges", nodes="nodes", name="name", source="sender", target="receiver",
                           multigraph=False, directed=True)  # Load the graph

    graph_df = pd.DataFrame(columns=["MS_system", "node"])
    for node in G.nodes:
        graph_df.loc[len(graph_df)] = [project, node]
    graph_df["Degree Centrality"] = graph_df["node"].map(nx.degree_centrality(G))
    graph_df["In-degree Centrality"] = graph_df["node"].map(nx.in_degree_centrality(G))
    graph_df["Out-degree Centrality"] = graph_df["node"].map(nx.out_degree_centrality(G))
    graph_df["Eigenvector Centrality"] = graph_df["node"].map(nx.eigenvector_centrality(G, max_iter=1000))
    graph_df["Closeness Centrality"] = graph_df["node"].map(nx.closeness_centrality(G))
    graph_df["Betweenness Centrality"] = graph_df["node"].map(nx.betweenness_centrality(G))
    graph_df["Load Centrality"] = graph_df["node"].map(nx.load_centrality(G))
    graph_df["Harmonic Centrality"] = graph_df["node"].map(nx.harmonic_centrality(G))
    G = nx.Graph(G)
    graph_df["Information Centrality"] = graph_df["node"].map(nx.current_flow_closeness_centrality(G))
    graph_df["Currrent Flow Centrality"] = graph_df["node"].map(nx.current_flow_betweenness_centrality(G))
    graph_df["Subgraph Centrality"] = graph_df["node"].map(nx.subgraph_centrality(G))

    all_dfs.append(graph_df)

all_dfs = sorted(all_dfs, key=lambda d: d["MS_system"].iloc[0].casefold())
df = pd.concat(all_dfs)
df.to_csv("metrics/metrics_centrality.csv", index=False, header=True)