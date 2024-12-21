# Replication package and Online Appendix

This is a replication package and online appendix for the ICSA2025 paper "Network Centrality as a New Perspective on Microservice Architecture"

## Contents
This repository contains the following:
- [INSTALL](INSTALL.md): Detailed installation instructions for each used tool
- [Appendix](Appendix):
  - [Table I](Appendix/TableI_used_projects.pdf): Data on the 24 studied projects
  - [Table II](Appendix/TableII_list_of_metrics.pdf): List of all gathered metrics
  - [Project information](Appendix/Project%20information.ods): Tables of all projects gathered from all dataset and their metadata
- [Projects](Projects): a folder containing source code of all studied projects
- [Figures](Figures): a folder containing all figures used in the paper
  - [Sankey diagram](Figures/DataCollectionSankey.pdf): Sankey diagram of project selection process
  - [BMP process](Figures/BPM-Flow.pdf): BMP process for the data collection
  - [Size Heat Map](Figures/SizeHeatMap.pdf): Heat of Spearman Rho for correlation of size metrics with centrality
  - [Size Heat Map (Stat. Sig.)](Figures/SizeHeatMapStatSig.pdf): Heat of Spearman Rho for correlation of size metrics with centrality (stat. sig. only)
  - [Complexity Heat Map](Figures/ComplexityHeatMap.pdf): Heat of Spearman Rho for correlation of complexity metrics with centrality
  - [Complexity Heat Map (Stat. Sig.)](Figures/ComplexityHeatMapStatSig.pdf): Heat of Spearman Rho for correlation of complexity metrics with centrality (stat. sig. only)
  - [Quality Heat Map](Figures/QualityHeatMap.pdf): Heat of Spearman Rho for correlation of quality metrics with centrality
  - [Quality Heat Map (Stat. Sig.)](Figures/QualityHeatMapStatSig.pdf): Heat of Spearman Rho for correlation of quality metrics with centrality (stat. sig. only)
  - [Centrality Heat Map (Stat. Sig.)](Figures/CentralityHeatMapStatSig.pdf): Heat of Spearman Rho for correlation of centrality metrics with each other (stat. sig. only)
- [Raw data](raw_data): a folder containing all raw data extracted from different tools
  - [code2dfd](raw_data/code2dfd): Raw output of Code2DFD
  - [graph](raw_data/graph): Graphs extracted from Code2DFD output
  - [understand](raw_data/understand): Raw data from Understand
  - [jasome](raw_data/jasome): Raw data from Jasome
  - [package_map.json](raw_data/package_map.json): Mapping of Java packages to microservices
- [Metrics](Metrics): metrics extracted from raw data
  - [metrics_centrality.csv](Metrics/metrics_centrality.csv): All the centrality metrics for all microservice
  - [metrics_understand.csv](Metrics/metrics_understand.csv): All the `Understand` metrics for all microservices
  - [metrics_jasome_package.csv](Metrics/metrics_jasome_package.csv): All the `Jasome` metrics for all microservices on package level
  - [metrics_jasome_class.csv](Metrics/metrics_jasome_class.csv): All the `Jasome` metrics for all microservices on class level
  - [metrics_jasome_method.csv](Metrics/metrics_jasome_method.csv): All the `Jasome` metrics for all microservices on method level
  - [metrics_sonarqube.csv](Metrics/metrics_sonarqube.csv): All the `SonarQube` metrics for all microservices
  - [metrics_merged.csv](Metrics/metrics_merged.csv): All the metrics for all microservices
  - [metrics_statsig.csv](Metrics/metrics_statsig.csv): List of all metrics that have a statistically significant correlation with centrality
- [Results](Results): Data files containing the analyzed results to answer the Research Question
  - [NormalityAndersonDarling](Results/NormalityAndersonDarling.ods): Results of testing normality of each metric distribution with Anderson-Darling
  - [RQ1](Results/RQ1): Does centrality correlate with size metrics?
    - [metrics_size.csv](Results/RQ1/metrics_size.csv): All the size metrics that have a statistically significant correlation with centrality
    - [SizeSpearmanRho](Results/RQ1/SizeSpearmanRho.ods): Spearman Rho correlation between centrality and size metrics
  - [RQ2](Results/RQ2): Does centrality correlate with complexity metrics?
    - [metrics_complexity.csv](Results/RQ2/metrics_complexity.csv): All the complexity metrics that have a statistically significant correlation with centrality
    - [ComplexitySpearmanRho](Results/RQ2/ComplexitySpearmanRho.ods): Spearman Rho correlation between centrality and complexity metrics
  - [RQ3](Results/RQ3): Does centrality correlate with quality metrics?
    - [metrics_quality.csv](Results/RQ3/metrics_quality.csv): All the quality metrics that have a statistically significant correlation with centrality
    - [QualitySpearmanRho](Results/RQ3/QualitySpearmanRho.ods): Spearman Rho correlation between centrality and complexity metrics
- [Scripts](Scripts): a folder containing all the scripts
  - [extract_graphs.py](Scripts/extract_graphs.py): processes the `Code2DFD` output into standard graph `json`
  - [metrics_centrality.py](Scripts/metrics_centrality.py): computes centrality scores with `NetworkX`
  - [metrics_jasome.py](Scripts/metrics_jasome.py): executes `Jasome` tool and saves raw data
  - [merge_jasome.py](Scripts/merge_jasome.py): merge the raw `Jasome` data into `csv` files
  - [metrics_understand.py](Scripts/metrics_understand.py): executes `Understand` tool and saves raw data
  - [merge_understand.py](Scripts/merge_understand.py): merge the raw `Understand` data into a `csv` file
  - [metrics_sonarqube.py](Scripts/metrics_sonarqube.py): executes `SonarQube` analysis
  - [merge_sonarqube.py](Scripts/merge_sonarqube.py): put the `SonarQube` data into a `csv` file
  - [merge_all.py](Scripts/merge_all.py): merge all metrics into a single `csv` file
  - [metrics_results.py](Scripts/metrics_results.py): keep only the statistically significantly correlated metrics

## License

All generated data is provided under [Creative Commons 4.0 Attribution License](DATA_LICENSE).

All scripts are provided under the [MIT License](SCRIPT_LICENSE).

All the analysed projects must be used in accordance with their respective licenses (shared in each project when applicable).

## Preparation and installation

Follow the instructions in [INSTALL](INSTALL.md) to install and configure all used tools.

##  `Code2DFD` and centrality metrics
All DFDs are reconstructed with [c65b4a](https://github.com/tuhh-softsec/code2DFD/tree/c65b4a081ed2ca1618319e5dabf9ecf590988059) version of `Code2DFD` tool.

The raw output for each `PROJECT` is copied here to a folder `PROJECT-code2dfd`.

### Converting `Code2DFD` to `NetworkX` graph
The script [process_graphs.py](Scripts/extract_graphs.py) converts the `json` files of the `Code2DFD` output into
network files suitable for `NetworkX`.

For each `PROJECT`, it creates 2 files in a `PROJECT-graph` folder:
- `PROJECT-gwcc.json`: The Greatest Weakly Connected Component (GWCC) of the reconstructed architecture graph
- `PROJECT-gwcc_noDB.json`: The GWCC with all databases that are only connected to one service removed

### Computing centrality metrics

The script [metrics_centrality.py](Scripts/metrics_centrality.py) loads the `PROJECT-gwcc_noDB.json` files and computes the following centrality metrics with `NetworkX`:
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

The centrality metrics for each system and service are saved into [metrics_centrality.csv](Metrics/metrics_centrality.csv) `csv` file.

## `Jasome` metrics

`Jasome` tool can be downloaded from its GitHub [page](https://github.com/rodhilton/jasome).

### Raw `Jasome` data
The script [metrics_jasome.py](Scripts/metrics_jasome.py) executes the `Jasome` tool for each `PROJECT`.

Change the variable `JASOME_PATH` in the script to point to the `Jasome` binary on your system.

For each `PROJECT`, the scripts saves to the folder `PROJECT-jasome` the raw `xml` output from `Jasome` for each `src` folder in the project. 

### Merging `Jasome` metrics

The script [merge_jasome.py](Scripts/merge_jasome.py) takes the data from all the raw `xml`s into the following `csv` files:
- [metrics_jasome_package.csv](Metrics/metrics_jasome_package.csv): metrics calculated for each package
- [metrics_jasome_class.csv](Metrics/metrics_jasome_class.csv): metrics calculated for each class
- [metrics_jasome_method.csv](Metrics/metrics_jasome_method.csv): metrics calculated for each method

## `Understand` metrics

Download the `Understand` tool and acquire its license on the official [website](https://scitools.com/)

### Raw `Understand` data

The script [metrics_understand.py](Scripts/metrics_understand.py) executes the `Understand` tool for each `PROJECT`.

Change the variable `UND_PATH` in the script to point to the `und` [cli tool](https://support.scitools.com/support/solutions/articles/70000582798-using-understand-from-the-command-line-with-und) on your system.

For each `PROJECT`, the scripts saves to the folder `PROJECT-und` the raw `csv` output from `Understand`.

### Merging `Understand` metrics

The script [merge_understand.py](Scripts/merge_understand.py) takes only the metrics calculated on `Package` level for all
`PROJECTS` and saves them to [metrics_understand.csv](Metrics/metrics_understand.csv) `csv` file.


## `SonarQube` metrics

Deploy a `SonarQube` instance using the instructions from the [official website](https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/install-the-server/introduction/).

Generate a `Global Analysis Token` and a `User token`.

Download the `SonarScanner` application from the [official website](https://docs.sonarsource.com/sonarqube/9.9/analyzing-source-code/scanners/sonarscanner/).

### Raw `SonarQube` data

The script [metrics_sonarqube.py](Scripts/metrics_sonarqube.py) sets up a `SonarQube` project for each of the `PROJECT`s
in the repository and executes the analysis with `SonarScanner`.

Change the `SONAR_PATH` variable to the location of the `sonar-scanner` binary.

Change the `TOKEN` variable to the `Global Analysis Token` generated in `SonarQube`.

Additionally, if `SonarQube` is not deployed on `localhost:9000`, change the `-Dsonar.host.url` parameter in the run command.

After executing the script, you should see all projects analyzed in the `SonarQube` dashboard.

### Merging `SonarQube` data

The script [merge_sonarqube.py](Scripts/merge_sonarqube.py) queries data for each `PROJECT`.

Change the variable `USER_TOKEN` to the `User token` generated in `SonarQube`.

The script will query the `SonarQube` metrics on directory level, infer the package name from the directory path,
and save the metrics for each `PROJECT` and each package in the [metrics_sonarqube.csv](Metrics/metrics_sonarqube.csv).

## Merging all data

The file [package_map.json](raw_data/package_map.json) contains the mapping of Java packages to the microservices.

The script [merge_data.py](Scripts/merge_all.py) takes the [metrics_centrality.csv](Metrics/metrics_centrality.csv), [metrics_understand.csv](Metrics/metrics_understand.csv),
 [metrics_jasome_package.csv](Metrics/metrics_jasome_package.csv), [metrics_jasome_class.csv](Metrics/metrics_jasome_class.csv), [metrics_jasome_method.csv](Metrics/metrics_jasome_method.csv) ,
[metrics_sonarqube.csv](Metrics/metrics_sonarqube.csv) files, maps the packages to microservices and creates a unified `csv` file [metrics_merged.csv](Metrics/metrics_merged.csv) with microservices that have all possible metrics.

Metrics are aggregated from packages using `sum`, `mean` and `max` wherever suitable.

## Filtering metrics with statistically significant correlation

The file [metrics_statsig.csv](Metrics/metrics_statsig.csv) contains a list of metrics that have a statistically significant (`p<0.01`)
correlation with at least one centrality score, and their category of either `size`, `complexity` or `quality`.

The script [metrics_filter_statsig.py](Scripts/metrics_results.py) takes only such metrics from [metrics_merged.csv](Metrics/metrics_merged.csv)
and saves them to three respective `csv` files: [metrics_size.csv](Results/RQ1/metrics_size.csv), [metrics_complexity.csv](Results/RQ2/metrics_complexity.csv) and [metrics_quality.csv](Results/RQ3/metrics_quality.csv) together with the centrality metrics.