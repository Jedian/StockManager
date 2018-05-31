class StockManagerController():
    def __init__(self, model, view, controller):
        self.view = view
        self.model = model
        # self.other_controllers = ...
        
        self.loadDatabase()

    def start(self):
        self.view = self.view.StockManagerView()
        self.view.mainloop()

    def loadDatabase(self):
        self.productionData = self.model.Data('../../database/corte.csv')
        self.sellData = self.model.Data('../../database/venda.csv')

    def getStockPageContent(page):
        self.
        #fazer as conta e mostrar a planilha bonitinha
