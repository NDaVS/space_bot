import requests
import random

#There is my own API modules for this bot. Only what is necessary in this project

from config_data.config import Config, load_config
class NASA: #main class for data
    def __init__(self):
        self.config: Config = load_config()
        self.api_key = self.config.nasa.api_key

    def get_apod(self): #using for get APOD
        data = requests.get('https://api.nasa.gov/planetary/apod', params={'api_key': self.api_key}).json()
        return data

    def get_rmars(self): #using for get random mars photo
        sol = random.randint(1000, 3450)
        data = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos', params={'api_key': self.api_key, 'sol': sol}).json()
        return data

    def get_iss_data(self): #using for get astros data
        data = requests.get('http://api.open-notify.org/astros.json').json()
        return data
def load_nasa(): #return class instance
    return NASA()