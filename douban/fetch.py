import requests
import time
import logging
def fetch_movies(url):
    logging.info("正在获取豆瓣热门电影数据...")
    headers={
    "User-Agent":"Mozilla/5.0",
    "Referer":"https://m.douban.com/movie/"
}
    all_items = []
    for start in range(0, 400, 20):
        params={
            "category":"热门",
            "type":"全部",
            "limit":20,
            "start":start
        }
        try:
            response=requests.get(url,params=params,headers=headers)
            response.raise_for_status()
        except Exception as e:
            logging.error(f"请求失败：{e}")
            continue
        data=response.json()
        items = data.get("items", []) 
        if not items:
            break
        all_items.extend(items)
        logging.info(f"已获取 {len(all_items)} 条")
        time.sleep(1)
    return all_items