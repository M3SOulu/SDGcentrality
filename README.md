# Replication package and Online Appendix

This is a replication package and online appendix for the ICSA2025 paper "Network Centrality as a New Perspective on Microservice Architecture"

## Contents
This repository contains the source code of 24 OSS Microservice projects that we identified for our study.
This repository contains the following:
- For 24 `PROJECT`s:
  - A folder called `PROJECT` with the projects source code at the commit we performed the analysis on
  - A folder `PROJECT-code2dfd` with the raw `Code2DFD` output
  - A folder `PROJECT-graph` with graphs in `json` format for processing with `NetworkX`
- Script [process_graph.py](process_graphs.py): processes the `Code2DFD` output into standard graph `json`
- Script [metrics_centrality.py](metrics_centrality.py): computes centrality scores with `NetworkX`

## Setup
Install the following Python packages: `networkx`, `pandas`, `requests`.
If you want to replicate a specific tool, follow its instructions on how to properly set it up.

##  `Code2DFD` and centrality metrics
All DFDs are reconstructed with [c65b4a](https://github.com/tuhh-softsec/code2DFD/tree/c65b4a081ed2ca1618319e5dabf9ecf590988059) version of `Code2DFD` tool.

The raw output for each `PROJECT` is copied here to a folder `PROJECT-code2dfd`.

### Converting `Code2DFD` to `NetworkX` graph
The script [process_graphs.py](process_graphs.py) converts the `json` files of the `Code2DFD` output into
network files suitable for `NetworkX`.

For each `PROJECT`, it creates 2 files in a `PROJECT-graph` folder:
- `PROJECT-gwcc.json`: The Greatest Weakly Connected Component (GWCC) of the reconstructed architecture graph
- `PROJECT-gwcc_noDB.json`: The GWCC with all databases that are only connected to one service removed

### Computing centrality metrics

The script [metrics_centrality.py](metrics_centrality.py) loads the `PROJECT-gwcc_noDB.json` files and computes the following centrality metrics with `NetworkX`:
- Degree centrality
- In-degree centrality
- Out-degree centrality
- Eigenvector centrality
- Closeness centrality
- Betweenness centrality
- Load centrality
- Harmonic centrality
- Information Centrality
- Current flow centrality
- Subgraph centrality

The centrality metrics for each system and service are saved into [metrics_centrality.csv](metrics_centrality.csv) `csv` file.