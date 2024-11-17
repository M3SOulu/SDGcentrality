# Replication package and Online Appendix

This is a replication package and online appendix for the ICSA2025 paper "Network Centrality as a New Perspective on Microservice Architecture"

## Contents
This repository contains the source code of 24 OSS Microservice projects that we identified for our study.
This repository contains the following:
- For 24 `PROJECT`s:
  - A folder called `PROJECT` with the projects source code at the commit we performed the analysis on
  - A folder `PROJECT-code2dfd` with the raw `Code2DFD` output
  - A folder `PROJECT-graph` with graphs in `json` format for processing with `NetworkX`
  - A folder `PROJECT-jasome` with the raw `Jasome` output
  - A folder `PROJECT-und` with the raw `Understand` output
- Scripts:
  - [process_graph.py](process_graphs.py): processes the `Code2DFD` output into standard graph `json`
  - [metrics_centrality.py](metrics_centrality.py): computes centrality scores with `NetworkX`
  - [metrics_jasome.py](merge_jasome.py): executes `Jasome` tool and saves raw data
  - [merge_jasome.py](merge_jasome.py): merge the raw `Jasome` data into `csv` files
  - [metrics_understand.py](merge_understand.py): executes `Understand` tool and saves raw data
  - [merge_understand.py](merge_understand.py): merge the raw `Understand` data into a `csv` file

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

## `Jasome` metrics

`Jasome` tool can be downloaded from its GitHub [page](https://github.com/rodhilton/jasome).

### Raw `Jasome` data
The script [metrics_jasome.py](metrics_jasome.py) executes the `Jasome` tool for each `PROJECT`.

Change the variable `JASOME_PATH` in the script to point to the `Jasome` binary on your system.

For each `PROJECT`, the scripts saves to the folder `PROJECT-jasome` the raw `xml` output from `Jasome` for each `src` folder in the project. 

### Merging `Jasome` metrics

The script [merge_jasome.py](merge_jasome.py) takes the data from all the raw `xml`s into the following `csv` files:
- [metrics_jasome_package.csv](metrics_jasome_package.csv): metrics calculated for each package
- [metrics_jasome_class.csv](metrics_jasome_class.csv): metrics calculated for each class
- [metrics_jasome_method.csv](metrics_jasome_method.csv): metrics calculated for each method

## `Understand` metrics

Download the `Understand` tool and acquire its license on the official [website](https://scitools.com/)

### Raw `Understand` data

The script [metrics_understand.py](metrics_understand.py) executes the `Understand` tool for each `PROJECT`.

Change the variable `UND_PATH` in the script to point to the `und` [cli tool](https://support.scitools.com/support/solutions/articles/70000582798-using-understand-from-the-command-line-with-und) on your system.

For each `PROJECT`, the scripts saves to the folder `PROJECT-und` the raw `csv` output from `Understand`.

### Merging `Understand` metrics

The script [merge_understand.py](merge_understand.py) takes only the metrics calculated on `Package` level for all
`PROJECTS` and saves them to [metrics_understand.csv](metrics_understand.csv) `csv` file.
