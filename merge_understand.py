import os

import pandas as pd


all_dfs = []
for folder in os.listdir(os.getcwd()):
    if not os.path.isdir(folder):
        continue
    if not folder.endswith("-und"):
        continue
    for file in os.listdir(folder):
        if not file.endswith("csv"):
            continue
        metrics_path = os.path.join(folder, file)
        df = pd.read_csv(metrics_path)
        df = df[df["Kind"] == "Package"]
        df["MS_system"] = file[:-4]
        cols = ["MS_system"] + [col for col in df.columns if col != "MS_system"]
        df = df[cols]
        all_dfs.append(df)

all_dfs = sorted(all_dfs, key=lambda d: d["MS_system"].iloc[0].casefold())
df = pd.concat(all_dfs)
df.to_csv("metrics_understand.csv", index=False, header=True)