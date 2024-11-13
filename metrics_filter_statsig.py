import pandas as pd

df_metrics = pd.read_csv("metrics_statsig.csv")

df = pd.read_csv("metrics_microservice.csv")
centrality_cols = [col for col in df.columns if "Centrality" in col]
complexity_metrics = (["MS_system", "Microservice"] + centrality_cols
                      + list(df_metrics[df_metrics["type"] == "complexity"]["metric"]))
df_complexity = df[complexity_metrics]
df_complexity.to_csv("metrics_complexity.csv", index=False, header=True)
size_metrics = (["MS_system", "Microservice"] + centrality_cols
                + list(df_metrics[df_metrics["type"] == "size"]["metric"]))
df_size = df[size_metrics]
df_size.to_csv("metrics_size.csv", index=False, header=True)
techdebt_metrics = (["MS_system", "Microservice"] + centrality_cols
                    + list(df_metrics[df_metrics["type"] == "techdebt"]["metric"]))
df_techdebt = df[techdebt_metrics]
df_techdebt.to_csv("metrics_techdebt.csv", index=False, header=True)
