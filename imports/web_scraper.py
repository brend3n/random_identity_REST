import requests
from bs4 import BeautifulSoup
import random

# Returns the soup of the HTML content
def get_soup_basic(url):
    # print(f"get_soup({url})")
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

ua_link = "http://www.webapps-online.com/online-tools/user-agent-strings/dv/plugin55210/chromium"

def get_user_agents(ua_link):
    ua_list = []
    soup = get_soup_basic(ua_link)
    td = soup.find_all("td", {"class": "uas_useragent"})
    for t in td:
        # print(f'{t.text}\n')
        ua_list.append(t.text)

    return ua_list
    
ua_list = get_user_agents(ua_link)

# Returns a random user agent from the list of user agents
def get_random_ua(ua_list):
    return random.choice(ua_list)

# Returns the soup of the HTML content
def get_soup_adv(url, ua_list=ua_list):
    headers = {'User-Agent': get_random_ua(ua_list)}
    page = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# if __name__== "__main__":
    ua_link = "http://www.webapps-online.com/online-tools/user-agent-strings/dv/plugin55210/chromium"
    ua_list = get_user_agents(ua_link)
