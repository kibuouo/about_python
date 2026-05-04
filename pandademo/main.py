import pandas as pd
if __name__=="__main__":
    df=pd.read_csv("movielist.csv")
    df["score"]=df["score"].astype(float)
    #str=df.head()
    #str=df.info()
    #str=df.describe()
    #str=df[df["score"]>9.0]
    sv=df.sort_values(by="score",ascending=False)
    df["star"]=0.0
    df.loc[df["score">=9.5],"star"]=5.0
    df.loc[df["score">=9],"star"]=4.5
    df.loc[df["score">=8],"star"]=4.0
    df.loc[df["score"]>=7,"star"]=3.5
    
    df.to_csv("movielist.csv", index=False)
    print(df)