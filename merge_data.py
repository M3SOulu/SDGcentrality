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

# Group by microservice and sum all the Count columns
count_cols = [col for col in understand.columns if col not in ["MS_system", "Microservice"]]
ms_systems = understand.groupby("Microservice").first()[["MS_system"]]  # Retain the MS_system column
sum_metrics = understand.groupby('Microservice')[count_cols].sum().reset_index()
understand = sum_metrics.merge(ms_systems, on='Microservice')  # Insert back the MS_system column

# Reorder columns to start with system, service
cols = ["MS_system", "Microservice"] + [col for col in understand.columns
                                if col not in ["MS_system", "Microservice"]]
understand = understand[cols]
understand = understand.sort_values(by=["MS_system", "Microservice"])


# --- Centrality
centrality = pd.read_csv("metrics_centrality.csv")
centrality = centrality.rename(columns={"node": "Microservice"})


# --- Total merge

total = understand
total = total.merge(centrality, on=["MS_system", "Microservice"], how="left")
total = total.sort_values(by=["MS_system", "Microservice"])
total.to_csv("metrics_microservice.csv", index=False, header=True)

