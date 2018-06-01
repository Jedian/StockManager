import Tkinter as tk

class ProductionSubmitPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="This is page 2")
        self.dataEntry = tk.Entry(self)
        self.button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))

        self.label.pack(side="top", fill="x", pady=10)
        self.dataEntry.pack()
        self.button.pack()

    def setController(self, controller):
        self.smcontroller = controller

