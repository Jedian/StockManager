# -*- coding: utf-8 -*-
import pandas as pd

class Data():
    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(self.filename)
        self.data.to_csv(filename+'.bkp', index=False)

    def getContent(self, page=1):
        if page != 'all':
            return self.data[(page-1)*6:page*6]
        else:
            return self.data

    def saveData(self, data):
        data.to_csv(self.filename, index=False)
        self.data = pd.read_csv(self.filename)
