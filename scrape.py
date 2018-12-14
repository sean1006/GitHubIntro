from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def main():
    website = "http://na.op.gg/summoner/userName=mafi4rmy"
    html_raw = simple_get(website)
    html = BeautifulSoup(html_raw, 'html.parser')
    f = open("kevostat.txt","w+")
    f.write(html_raw)
    winRate = html.findAll("div", {"title": "Win Ratio"})
    champName = html.findAll("div", {"class": "ChampionName"})
    i = 0
    while i < len(winRate) and i < len(champName):
        print(str(champName[i]).split()[2:4])
        print(str(winRate[i]).split()[6])
        i += 1
#    for i in divs:
#        print(i)
        #f.write(i)
    f.close()

if __name__ == '__main__':
    main()
