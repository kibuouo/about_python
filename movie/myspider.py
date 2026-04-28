#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 网页爬虫模块
# 功能：使用requests库发送HTTP请求，获取网页HTML内容
# 依赖：requests

import requests  # 导入requests库，用于发送HTTP请求
#from bs4 import BeautifulSoup  # 导入BeautifulSoup库（已注释，用于解析HTML）
#url="https://ssr1.scrape.center/"  # 定义目标URL（已注释）


def getHtml(url):
    # 获取指定URL的HTML内容
    # 参数：url - 目标网页URL
    # 返回：HTML文本内容，失败返回None
    headers = {  # 定义请求头字典
        "User-Agent":"Mozilla/5.0"  # 设置User-Agent，模拟浏览器访问
    }
    responser = requests.get(url,headers=headers)  # 发送GET请求，获取响应
    if responser.status_code == 200:  # 判断响应状态码是否为200（成功）
        return responser.text  # 返回响应文本内容
    else:  # 状态码不是200的情况
        print("请求失败，状态码：",responser.status_code)  # 打印错误状态码
        return None  # 返回None表示请求失败