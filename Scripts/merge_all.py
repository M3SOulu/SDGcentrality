import json

import pandas as pd

with open("raw_data/package_map.json", 'r') as f:
    PACKAGE_MAP = json.load(f)

PACKAGES = set(PACKAGE_MAP.keys())
SERVICES = set(PACKAGE_MAP.values())

# Mappping of packages to services
def map_packages(value: str):
    for package, service in PACKAGE_MAP.items():
        if value.startswith(package):
            return service
    return None


# --- Understand metrics
understand = pd.read_csv("Metrics/metrics_understand.csv")

# Remove NaN columns
understand = understand.dropna(axis=1, how='all')

# Map Package to Microservice
understand = understand.rename(columns={"Name": "Package"})
understand["Microservice"] = understand["Package"].map(map_packages)
# Remove rows that are not mapped to a service
understand = understand.dropna(subset=["Microservice"])
understand = understand.drop(columns=["Package"])

# Remove Average and Ratio columns
avg_cols = [col for col in understand.columns if "Avg" in col or "Ratio" in col or "Max" in col]
understand = understand.drop(columns=avg_cols)

# Group by microservice and sum all the metric columns
count_cols = [col for col in understand.columns if col not in ["MS_system", "Microservice"]]
ms_systems = understand.groupby("Microservice").first()[["MS_system"]]  # Retain the MS_system column
sum_metrics = understand.groupby('Microservice')[count_cols].sum().reset_index()
understand = sum_metrics.merge(ms_systems, on='Microservice')  # Insert back the MS_system column

# Calculate Private to Public method ratio
understand["RatioPrivateToPublicMethod"] = understand["CountDeclMethodPrivate"]/understand["CountDeclMethodPublic"]



# --- Jasome Package
jasome_package = pd.read_csv("Metrics/metrics_jasome_package.csv")
# Map Package to Microservice
jasome_package["Microservice"] = jasome_package["Package"].map(map_packages)
# Remove rows that are not mapped to a service
jasome_package = jasome_package.dropna(subset=["Microservice"])
jasome_package = jasome_package.drop(columns=["Package"])

# Drop unnecessary metrics
jasome_package = jasome_package.drop(columns=["A", "I", "DMS", "CCRC", "PkgRCI"], errors="ignore")

# Group by microservice and sum all the metric columns
count_cols = [col for col in jasome_package.columns if col not in ["MS_system", "Microservice"]]
ms_systems = jasome_package.groupby("Microservice").first()[["MS_system"]]  # Retain the MS_system column
sum_metrics = jasome_package.groupby('Microservice')[count_cols].sum()
sum_metrics.columns = sum_metrics.columns.map(lambda x: f"Sum({x})")
sum_metrics = sum_metrics.reset_index()
jasome_package = sum_metrics.merge(ms_systems, on='Microservice')  # Insert back the MS_system column


# --- Jasome Class
jasome_class = pd.read_csv("Metrics/metrics_jasome_class.csv")
# Map Package to Microservice
jasome_class["Microservice"] = jasome_class["Package"].map(map_packages)
# Remove rows that are not mapped to a service
jasome_class = jasome_class.dropna(subset=["Microservice"])
jasome_class = jasome_class.drop(columns=["Package"])

# Drop unnecessary metrics
jasome_class = jasome_class.drop(columns=["ClRCi", "ClTCi", "TLOC"], errors="ignore")

SUM_COLS = ["Aa", "Ad", "Ait", "Ao", "Av", "HMd", "HMi", "Ma", "Md", "Mi", "Mit", "Mo", "NF", "NM", "NMA",
            "NMI", "NOA", "NOCh", "NOD", "NOL", "NOPa", "NORM", "NPF", "NPM", "NSF", "NSM", "PMd",
            "PMi", "RTLOC", "SIX", "WMC", "LCOM*", "PF"]
AVG_COLS = ["Aa", "Ad", "Ait", "Ao", "Av", "DIT", "HMd", "HMi", "MHF", "MIF", "Ma", "Md", "Mi", "Mit", "Mo",
            "NF", "NM", "NMA", "NMI", "NOA", "NOCh", "NOD", "NOL", "NOPa", "NORM", "NPF", "NPM",
            "NSF", "NSM", "PMR", "PMd", "PMi", "SIX", "AHF", "AIF", "LCOM*", "NMIR", "PF"]
MAX_COLS = ["DIT", "WMC", "LCOM*", "PF"]
ms_systems = jasome_class.groupby("Microservice").first()[["MS_system"]]  # Retain the MS_system column
sum_metrics = jasome_class.groupby('Microservice')[SUM_COLS].sum()
sum_metrics.columns = sum_metrics.columns.map(lambda x: f"Sum({x})")
sum_metrics = sum_metrics.reset_index()
jasome_class_merged = sum_metrics.merge(ms_systems, on='Microservice')  # Insert back the MS_system column
avg_metrics = jasome_class.groupby('Microservice')[AVG_COLS].mean()
avg_metrics.columns = avg_metrics.columns.map(lambda x: f"Avg({x})")
avg_metrics = avg_metrics.reset_index()
jasome_class_merged = jasome_class_merged.merge(avg_metrics, on='Microservice')
max_metrics = jasome_class.groupby('Microservice')[MAX_COLS].max()
max_metrics.columns = max_metrics.columns.map(lambda x: f"Max({x})")
max_metrics = max_metrics.reset_index()
jasome_class_merged = jasome_class_merged.merge(max_metrics, on='Microservice')
jasome_class = jasome_class_merged


# --- Jasome Method
jasome_method = pd.read_csv("Metrics/metrics_jasome_method.csv")
# Map Package to Microservice
jasome_method["Microservice"] = jasome_method["Package"].map(map_packages)
# Remove rows that are not mapped to a service
jasome_method = jasome_method.dropna(subset=["Microservice"])
jasome_method = jasome_method.drop(columns=["Package"])

# Drop unnecessary metrics
jasome_method = jasome_method.drop(columns=["Ci", "NCOMP", "NOP", "NVAR", "TLOC"], errors="ignore")

SUM_COLS = ["Di", "Fin", "Fout", "IOVars", "MCLC", "NBD", "Si", "VG"]
AVG_COLS = ["Di", "Fin", "Fout", "IOVars", "MCLC", "NBD", "Si", "VG"]
MAX_COLS = ["Di", "Fin", "Fout", "IOVars", "MCLC", "NBD", "Si", "VG"]
ms_systems = jasome_method.groupby("Microservice").first()[["MS_system"]]  # Retain the MS_system column
sum_metrics = jasome_method.groupby('Microservice')[SUM_COLS].sum()
sum_metrics.columns = sum_metrics.columns.map(lambda x: f"Sum({x})")
sum_metrics = sum_metrics.reset_index()
jasome_method_merged = sum_metrics.merge(ms_systems, on='Microservice')  # Insert back the MS_system column
avg_metrics = jasome_method.groupby('Microservice')[AVG_COLS].mean()
avg_metrics.columns = avg_metrics.columns.map(lambda x: f"Avg({x})")
avg_metrics = avg_metrics.reset_index()
jasome_method_merged = jasome_method_merged.merge(avg_metrics, on='Microservice')
max_metrics = jasome_method.groupby('Microservice')[MAX_COLS].max()
max_metrics.columns = max_metrics.columns.map(lambda x: f"Max({x})")
max_metrics = max_metrics.reset_index()
jasome_method_merged = jasome_method_merged.merge(max_metrics, on='Microservice')
jasome_method = jasome_method_merged


# --- SonarQube
sonarqube = pd.read_csv("Metrics/metrics_sonarqube.csv")
sonarqube["Microservice"] = sonarqube["Package"].map(map_packages)

# Remove rows that are not mapped to a service
sonarqube = sonarqube.dropna(subset=["Microservice"])
sonarqube = sonarqube.drop(columns=["Package"])

rating_cols = ["Sqale rating", "Reliability rating", "Security rating"]
count_cols = [col for col in sonarqube.columns if col not in ["MS_system", "Microservice"] + rating_cols]
ms_systems = sonarqube.groupby("Microservice").first()[["MS_system"]]  # Retain the MS_system column
sum_metrics = sonarqube.groupby('Microservice')[count_cols].sum().reset_index()
avg_metrics = sonarqube.groupby('Microservice')[rating_cols].mean()
avg_metrics.columns = avg_metrics.columns.map(lambda x: f"Avg({x})")
avg_metrics = avg_metrics.reset_index()
max_metrics = sonarqube.groupby('Microservice')[rating_cols].max()
max_metrics.columns = max_metrics.columns.map(lambda x: f"Max({x})")
max_metrics = max_metrics.reset_index()
sonarqube_merged = sum_metrics.merge(ms_systems, on='Microservice')  # Insert back the MS_system column
sonarqube_merged = sonarqube_merged.merge(avg_metrics, on="Microservice")
sonarqube = sonarqube_merged.merge(max_metrics, on="Microservice")


# --- Centrality
centrality = pd.read_csv("Metrics/metrics_centrality.csv")
centrality = centrality.rename(columns={"node": "Microservice"})


# --- Total merge

total = understand
total = total.merge(jasome_package, on=["MS_system", "Microservice"], how="left")
total = total.merge(jasome_class, on=["MS_system", "Microservice"], how="left")
total = total.merge(jasome_method, on=["MS_system", "Microservice"], how="left")
total = total.merge(sonarqube, on=["MS_system", "Microservice"], how="left")
total = total.merge(centrality, on=["MS_system", "Microservice"], how="left")
total = total.drop(columns=["Avg(NMIR)", "Avg(PF)", "Max(PF)"])
total = total.dropna()

# Reorder columns to start with system, service
cols = ["MS_system", "Microservice"] + [col for col in total.columns
                                        if col not in ["MS_system", "Microservice"]]
total = total[cols]
total = total.sort_values(by=["MS_system", "Microservice"])
total.to_csv("Metrics/metrics_merged.csv", index=False, header=True)
