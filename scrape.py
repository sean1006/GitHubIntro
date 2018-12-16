from __future__ import print_function
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
    website = "http://na.op.gg/summoner/champions/userName="
    user = raw_input()
    html_raw = simple_get(website+user)
    html = BeautifulSoup(html_raw, 'html.parser')
    #f = open("kevostat.txt","w+")
    winRate = html.findAll("div", {"class": "WinRatioGraph"})
    champName = html.findAll("td", {"class": "ChampionName Cell"})
    i = 0
    while i < len(winRate) and i < len(champName):
        j = str(winRate[i]).find("%") - 3
        l = str(winRate[i]).find("L<") - 4
        w = str(winRate[i]).find("W<") - 4
        Lose = 0
        Win = 0
        if l > 0:
            while str(winRate[i])[l] is not "L":
                if str(winRate[i])[l].isdigit():
                    Lose = Lose * 10 + int(str(winRate[i])[l])
                l+=1
        if w > 0:
            while str(winRate[i])[w] is not "W":
                if str(winRate[i])[w].isdigit():
                    Win = Win * 10 + int(str(winRate[i])[w])
                w+=1
        print(str(champName[i]).split("\"")[3] + " (" + str(Win + Lose) + "): ", end='')
        while str(winRate[i])[j] is not "%":
            if str(winRate[i])[j].isdigit():
                print(str(winRate[i])[j], end='')
            j+=1
        print("%")
        i += 1
    #f.close()

if __name__ == '__main__':
    main()
