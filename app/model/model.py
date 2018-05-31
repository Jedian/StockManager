import pandas as pd

class Data():
    def __init__(self, filename):
        self.data = pd.read_csv(filename)

    def getContent(page=1):
        return self.data

