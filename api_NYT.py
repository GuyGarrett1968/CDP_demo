# Social Media API, provider C
import requests

class API_NYT(object):

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def retrieveArchive(self):

        url = "http://api.nytimes.com/svc/archive/v1/" + str(self.year) +"/" + str(self.month) + ".json?api-key=289a048eb3e545e496ff167572cca053"
        r = requests.get(url)
        if r.status_code == 200:
            return (r.json())

print('[NOTE]: File api_NYT.py was imported.')
