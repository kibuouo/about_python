import requests
def getUrl(url):
    header={
        "User-Agent":"Mozilla/5.0"
    }
    responser = requests.get(url,headers=header)
    return responser.text