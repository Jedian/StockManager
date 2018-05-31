class StockManagerController():
    def __init__(self, view, controller):
        self.view = view
        # self.model = model
        # self.other_controllers = ...


    def start(self):
        self.view = self.view.StockManagerView()
        self.view.mainloop()
