import os
import xml.etree.ElementTree as ET

import pandas as pd

DATA_PACKAGE = []
DATA_CLASS = []
DATA_METHOD = []
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
                            data_point = {"Package": package_name}
                            for metric in child_p:
                                data_point[metric.attrib["name"]] = float(metric.attrib["value"].replace(",", "."))
                            DATA_PACKAGE.append(data_point)
                        elif child_p.tag == "Classes":
                            for clas in child_p:
                                class_name = clas.attrib["name"]
                                for child_c in clas:
                                    if child_c.tag == "Metrics":
                                        data_point = {"Package": package_name,
                                                      "Class": class_name}
                                        for metric in child_c:
                                            data_point[metric.attrib["name"]] = float(metric.attrib["value"].replace(",", "."))
                                        DATA_CLASS.append(data_point)
                                    elif child_c.tag == "Methods":
                                        for method in child_c:
                                            method_name = method.attrib["name"]
                                            for child_m in method:
                                                if child_m.tag == "Metrics":
                                                    data_point = {"Package": package_name,
                                                                  "Class": class_name,
                                                                  "Method": method_name}
                                                    for metric in child_m:
                                                        data_point[metric.attrib["name"]] = float(metric.attrib["value"].replace(",", "."))
                                                    DATA_METHOD.append(data_point)

df = pd.DataFrame(DATA_PACKAGE)
df.to_csv("jasome_metrics_package.csv", index=False, header=True)
df = pd.DataFrame(DATA_CLASS)
df.to_csv("jasome_metrics_class.csv", index=False, header=True)
df = pd.DataFrame(DATA_METHOD)
df.to_csv("jasome_metrics_method.csv", index=False, header=True)
