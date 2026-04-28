#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 电影数据爬取主程序
# 功能：1. 从目标网站获取HTML页面 2. 解析HTML提取电影标题和评分 3. 将数据保存为CSV文件
# 用法：python main.py

#import myspider
#import myparser
#import mysave
from myparser import parser_movie  # 从解析模块导入解析函数
from myspider import getHtml        # 从爬虫模块导入获取HTML函数
from mysave import savetocsv        # 从保存模块导入保存函数


def main():
    # 主函数：协调各模块完成电影数据爬取
    url="https://ssr1.scrape.center/"  # 目标网站URL
    html=getHtml(url)  # 获取网页HTML
    if html:  # 判断是否成功获取
        movie_list=parser_movie(html)  # 解析HTML提取电影列表
        savetocsv(movie_list,"movies.csv")  # 保存到CSV文件
        print("succeed,保存",len(movie_list),"条数据")  # 打印成功信息


if __name__=="__main__":
    main()