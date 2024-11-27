import pandas as pd

df_metrics = pd.read_csv("Metrics/metrics_statsig.csv")

df = pd.read_csv("Metrics/metrics_merged.csv")
centrality_cols = [col for col in df.columns if "Centrality" in col]
complexity_metrics = (["MS_system", "Microservice"] + centrality_cols
                      + list(df_metrics[df_metrics["type"] == "complexity"]["metric"]))
df_complexity = df[complexity_metrics]
df_complexity.to_csv("Results/RQ2/metrics_complexity.csv", index=False, header=True)
size_metrics = (["MS_system", "Microservice"] + centrality_cols
                + list(df_metrics[df_metrics["type"] == "size"]["metric"]))
df_size = df[size_metrics]
df_size.to_csv("Results/RQ1/metrics_size.csv", index=False, header=True)
techdebt_metrics = (["MS_system", "Microservice"] + centrality_cols
                    + list(df_metrics[df_metrics["type"] == "quality"]["metric"]))
df_techdebt = df[techdebt_metrics]
df_techdebt.to_csv("Results/RQ3/metrics_quality.csv", index=False, header=True)
