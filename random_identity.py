import random
import requests
import urllib3

from random_name import random_first_name_updated, random_last_name_updated
from bs4 import BeautifulSoup

urllib3.disable_warnings()



# Used for getting random phone numbers
states = [ 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

class Random_Identity:
    def __init__(self):
        return
    
    # TODO: Change this so it is 10 minute temporary phone number or longer
    def get_phone_number(self):
        state = self.state
        url = f"https://www.randomphonenumbers.com/Generator/us_phone_number?state={state}&city="
	soup = get_soup_adv(url)
	soup = soup.find_all("p", "text-center code")
	soup = [ele.text for ele in soup]
        phone_number = random.choice(soup).replace("-","")

        self.phone_number = phone_number

    # TODO: Change this to use the other API
    def get_email():
        return

    def get_random_state():
        self.state = random.choice(states)

    def get_random_city():
        url = f"https://locations.chipotle.com/{str(state).lower()}"
        soup = get_soup_adv(url)
        cities = soup.find_all("a", "Directory-listLink")
        self.city = random.choice(cities)['href']

    def get_name():
        self.first_name = random_first_name_updated(path="./Random-Name-Generator")
        self.last_name = random_last_name_updated(path="./Random-Name-Generator")


