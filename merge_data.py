import json

import pandas as pd

with open("package_map.json", 'r') as f:
    package_map = json.load(f)

packages = set(package_map.keys())
services = set(package_map.values())

understand = pd.read_csv("metrics_understand.csv")

# Remove NaN columns
understand = understand.dropna(axis=1, how='all')


# Map packages to services
def map_packages(value: str):
    for package, service in package_map.items():
        if value.startswith(package):
            return service
    return None


understand = understand.rename(columns={"Name": "package"})
understand["microservice"] = understand["package"].map(map_packages)

# Remove rows that are not mapped to a service
understand = understand.dropna(subset=["microservice"])

# Remove Kind column (always Package)
understand = understand.drop(columns=["Kind"])

centrality = pd.read_csv("metrics_centrality.csv")
centrality = centrality.rename(columns={"node": "microservice"})

# Merged Understand metrics and Centrality scores on correct System and Microservice pair
merged = pd.merge(understand, centrality, on=["MS_system", "microservice"], how='left')

# Reorder columns to start with system, service, package
cols = ["MS_system", "microservice", "package"] + [col for col in merged.columns
                                                   if col not in ["MS_system", "microservice", "package"]]
merged = merged[cols]

# Save
merged = merged.sort_values(by=["MS_system", "microservice", "package"])
merged.to_csv("metrics_microservice.csv", index=False, header=True)

# Remove Average and Ratio columns
avg_cols = [col for col in understand.columns if "Avg" in col or "Ratio" in col]
collapsed = understand.drop(columns=avg_cols)

# Group by microservice and sum all the Count columns
count_cols = [col for col in collapsed.columns if 'Count' in col]
ms_systems = collapsed.groupby("microservice").first()[["MS_system"]]  # Retain the MS_system column
collapsed = collapsed.groupby('microservice')[count_cols].sum().reset_index()
collapsed = collapsed.merge(ms_systems, on='microservice')  # Insert back the MS_system column


# Merged collapsed Understand metrics and Centrality scores on correct System and Microservice pair
collapsed_merged = pd.merge(collapsed, centrality, on=["MS_system", "microservice"], how='left')

# Reorder columns to start with system, service
cols = ["MS_system", "microservice"] + [col for col in collapsed_merged.columns
                                if col not in ["MS_system", "microservice"]]
collapsed_merged = collapsed_merged[cols]


# Save
collapsed_merged = collapsed_merged.sort_values(by=["MS_system", "microservice"])
collapsed_merged.to_csv("metrics_microservice_collapsed.csv", index=False, header=True)
