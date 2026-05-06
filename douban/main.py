from fetch import fetch_movies
from parse import parse_movies  
import analyze
import save
import logging
def main():
    url="https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie"
    all_items=fetch_movies(url)
    df=parse_movies(all_items)
    save.save_movies(all_items)
    save.save_clean_movies(df)
    type_df,country_df=analyze.analyze_movies(df)
    save.save_analyze(type_df,country_df)
    hot_df = analyze.hot_movies(df)
    logging.info(f"高分电影数量: {len(hot_df)}")
if __name__=="__main__":
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
    main()
    