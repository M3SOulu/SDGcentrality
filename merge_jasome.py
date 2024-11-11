import os
import xml.etree.ElementTree as ET

import pandas as pd

DATA = {}
for folder in os.listdir(os.getcwd()):
    if not folder.endswith("jasome"):
        continue
    for f in os.listdir(folder):
        if not f.endswith("xml"):
            continue
        tree = ET.parse(os.path.join(folder, f))
        root = tree.getroot()
        for child_r in root:
            if child_r.tag == "Packages":
                for package in child_r:
                    package_name = package.attrib["name"]
                    for child_p in package:
                        if child_p.tag == "Metrics":
                            DATA[f"{package_name}"] = {}
                            for metric in child_p:
                                DATA[f"{package_name}"][metric.attrib["name"]] = float(metric.attrib["value"].replace(",","."))
                        elif child_p.tag == "Classes":
                            for clas in child_p:
                                class_name = clas.attrib["name"]
                                for child_c in clas:
                                    if child_c.tag == "Metrics":
                                        DATA[f"{package_name}.{class_name}"] = {}
                                        for metric in child_c:
                                            DATA[f"{package_name}.{class_name}"][metric.attrib["name"]] = float(metric.attrib["value"].replace(",", "."))
                                    elif child_c.tag == "Methods":
                                        for method in child_c:
                                            method_name = method.attrib["name"]
                                            for child_m in method:
                                                if child_m.tag == "Metrics":
                                                    DATA[f"{package_name}.{class_name}.{method_name}"] = {}
                                                    for metric in child_m:
                                                        DATA[f"{package_name}.{class_name}.{method_name}"][metric.attrib["name"]] = float(metric.attrib["value"].replace(",","."))

df = pd.DataFrame.from_dict(DATA, orient="index")
df = df.reset_index().rename(columns={"index": "source"})
df.to_csv("jasome_metrics.csv", index=False, header=True)
