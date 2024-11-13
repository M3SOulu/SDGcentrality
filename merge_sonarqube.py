import os

import requests
import pandas as pd

USER_TOKEN = "squ_716bdb66681839207f45848b2884859ab60540d5"

METRICS = ["sqale_rating",
           "reliability_remediation_effort",
           "security_remediation_effort",
           "software_quality_maintainability_remediation_effort",
           "software_quality_reliability_remediation_effort",
           "software_quality_security_remediation_effort",
           "bugs",
           "code_smells",
           "cognitive_complexity",
           "violations",
           "effort_to_reach_software_quality_maintainability_rating_a",
           "duplicated_blocks",
           "reliability_rating",
           "security_hotspots",
           "security_rating",
           "critical_violations",
           "info_violations",
           "major_violations",
           "minor_violations"]

COMPONENTS = {}
for folder in os.listdir(os.getcwd()):
    if not folder.endswith("-graph"):
        continue
    folder = folder.replace("-graph", "")
    response = requests.get("http://localhost:9000/api/measures/component_tree", params={
        "component": folder,
        "metricKeys": ",".join(METRICS),
        "ps": 500,
        "qualifiers": "DIR"
    }, auth=(USER_TOKEN, ''))
    r = response.json()
    COMPONENTS[r["baseComponent"]["name"]] = r["components"]

DATA = []
for ms_system, components in COMPONENTS.items():
    for component in components:
        if "src/main/java" not in component["path"]:
            continue
        package = component["path"].split("src/main/java/")[1].replace("/", ".")
        datapoint = {"MS_system": ms_system, "Package": package}
        for metric in component["measures"]:
            datapoint[metric["metric"]] = metric["value"]
        DATA.append(datapoint)
df = pd.DataFrame(DATA)
df.to_csv("metrics_sonarqube.csv", header=True, index=False)

