import json
import logging
def save_movies(all_items):
    logging.info("正在保存电影数据...")
    with open("douban/data/douban_movies_row.json","w",encoding="utf-8") as f:
        json.dump(all_items,f,ensure_ascii=False,indent=4)#原始数据
def save_clean_movies(df):
    df.to_csv("douban/data/douban_clean_movies.csv", index=False, encoding="utf-8-sig") 
def save_analyze(type_df,country_df):
    type_df.to_csv("douban/data/douban_type_movie.csv",index=False,encoding="utf-8-sig")
    country_df.to_csv("douban/data/douban_country_movie.csv",index=False,encoding="utf-8-sig")