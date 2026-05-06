def analyze_movies(df):
    print("正在分析电影数据...")
    type_df=df.copy()
    type_df["类型"]=type_df["类型"].str.split()
    type_df=type_df.explode("类型")
    
    country_df=df.copy()
    country_df["地区"]=country_df["地区"].str.split(r"\s+")
    country_df=country_df.explode("地区")
    
    return type_df,country_df
def hot_movies(df, threshold=8.0):
    return df[df["rating"] > threshold] 