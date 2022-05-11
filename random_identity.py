import random
import requests
import urllib3
import sys
from random_address import real_random_address

sys.path.insert(0,"./imports")
sys.path.insert(0,'./imports/Random-Name-Generator')
sys.path.insert(0,'./imports/web_scraper')
sys.path.insert(0,'./imports/myTempEmail-API')
sys.path.insert(0,'./imports/pymailtm/pymailtm')

from random_name import random_first_name_updated, random_last_name_updated
from bs4 import BeautifulSoup
from web_scraper import get_soup_adv
from pymailtm import MailTm

urllib3.disable_warnings()

# Used for getting random phone numbers
states = [ 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


class Random_Identity:
    def __init__(self):
        self.state = "TODO"
        self.city = "TODO"
        self.get_name()
        self.get_address()
        self.get_phone_number()
        self.get_email()
        print(self.to_json())
        print(f"\nEmail: {self.emailaddress}\nPassword: {self.emailpassword}")
        print(f"\nGo to https://mail.tm/en/. Sign-out and then sign-in using credentials above.\n\n")
        return
    
    def to_string(self):
        stringy = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nState: {self.state}\nCity: {self.city}\nAddress: {self.address}\n"
        return stringy
    
    def to_json(self):
        return {
            "First Name" : self.first_name,
            "Last Name" : self.last_name,
            "Phone Number": self.phone_number,
            "Email" : self.emailaddress,
            "Email Password": self.emailpassword,
            "State": self.state,
            "City" : self.city,
            "Address" : self.address
            }

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
    def get_email(self):
        mail_obj = MailTm().get_account()
        self.emailaddress = mail_obj.address
        self.emailpassword  = mail_obj.password
        

    def get_address(self):
        
        dicty = real_random_address()
        self.address = str(dicty['address1']) + str(dicty['address2'])
        self.city = dicty['city']
        self.state = dicty['state']
        self.postalcode = dicty['postalCode']        
    
    def get_name(self):
        self.first_name = random_first_name_updated(path="./imports/Random-Name-Generator/")
        self.last_name = random_last_name_updated(path="./imports/Random-Name-Generator/")

person = Random_Identity()


