import os
import pandas as pd

if __name__ == "__main__":
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "movielist.csv"))
    df = pd.read_csv(csv_path)
    df["score"] = df["score"].astype(float)
    # df_head = df.head()
    # df_info = df.info()
    # df_desc = df.describe()
    # df_filtered = df[df["score"] > 9.0]
    sv = df.sort_values(by="score", ascending=False)
    df["star"] = 0.0
    df.loc[df["score"] >= 9.5, "star"] = 5.0
    df.loc[df["score"] >= 9, "star"] = 4.5
    df.loc[df["score"] >= 8, "star"] = 4.0
    df.loc[df["score"] >= 7, "star"] = 3.5

    df.to_csv(csv_path, index=False)
    print(df)