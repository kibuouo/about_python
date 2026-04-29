from spider import getUrl
from parser import parser_html
def main():
    url="https://www.douyu.com/directory/all"
    #url="https://www.bilibili.com/v/popular/all"
    html=getUrl(url)
    str=parser_html(html)
    print(str)
if __name__=="__main__":
    main()