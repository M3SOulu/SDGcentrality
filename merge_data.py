import json

import pandas as pd

with open("package_map.json", 'r') as f:
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
understand = pd.read_csv("metrics_understand.csv")

# Remove NaN columns
understand = understand.dropna(axis=1, how='all')
# Remove Kind column (always Package)
understand = understand.drop(columns=["Kind"])

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


# --- Jasome Package
jasome_package = pd.read_csv("metrics_jasome_package.csv")
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
sum_metrics.columns = sum_metrics.columns.map(lambda x: f"PackageSum{x}")
sum_metrics = sum_metrics.reset_index()
jasome_package = sum_metrics.merge(ms_systems, on='Microservice')  # Insert back the MS_system column


# --- Jasome Class
jasome_class = pd.read_csv("metrics_jasome_class.csv")
# Map Package to Microservice
jasome_class["Microservice"] = jasome_class["Package"].map(map_packages)
# Remove rows that are not mapped to a service
jasome_class = jasome_class.dropna(subset=["Microservice"])
jasome_class = jasome_class.drop(columns=["Package"])


# --- Jasome Method
jasome_method = pd.read_csv("metrics_jasome_method.csv")
# Map Package to Microservice
jasome_method["Microservice"] = jasome_method["Package"].map(map_packages)
# Remove rows that are not mapped to a service
jasome_method = jasome_method.dropna(subset=["Microservice"])
jasome_method = jasome_method.drop(columns=["Package"])


# --- Centrality
centrality = pd.read_csv("metrics_centrality.csv")
centrality = centrality.rename(columns={"node": "Microservice"})


# --- Total merge

total = understand
total = total.merge(jasome_package, on=["MS_system", "Microservice"], how="left")
total = total.merge(centrality, on=["MS_system", "Microservice"], how="left")

# Reorder columns to start with system, service
cols = ["MS_system", "Microservice"] + [col for col in total.columns
                                        if col not in ["MS_system", "Microservice"]]
total = total[cols]
total = total.sort_values(by=["MS_system", "Microservice"])
total.to_csv("metrics_microservice.csv", index=False, header=True)

