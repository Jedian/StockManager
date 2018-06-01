import Tkinter as tk

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Vendas",
                            command=lambda: controller.show_frame("SellsSubmitPage"))
        button2 = tk.Button(self, text="Corte",
                            command=lambda: controller.show_frame("ProductionSubmitPage"))
        button3 = tk.Button(self, text="Estoque",
                            command=lambda: controller.show_frame("StockPage"))
        button1.pack(side='left')
        button2.pack(side='left')
        button3.pack(side='left')

    def setController(self, controller):
        self.smcontroller = controller

