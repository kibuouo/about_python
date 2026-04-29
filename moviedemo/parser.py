from bs4 import BeautifulSoup
def parser_html(html):
    soup=BeautifulSoup(html,"html.parser")
    str=soup.find_all("a",class_="DyCardBottom-cardTitle")
    return str