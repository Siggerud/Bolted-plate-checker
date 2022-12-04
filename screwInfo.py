import requests, bs4

class ScrewInfo:
    def __init__(self, screwSize):
        self.screwSize = screwSize
        res = requests.get("https://eurocodeapplied.com/design/en1993/bolt-design-properties")
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")

