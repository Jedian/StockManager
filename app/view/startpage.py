# -*- coding: utf-8 -*-
import Tkinter as tk
from PIL import ImageTk, Image

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Página Inicial")
        label.pack(side="top", fill="x", pady=10)

        bframe = tk.Frame(self)
        bframe.pack(side='top')

        b1frame = tk.Frame(bframe)
        b1frame.pack(side='left')

        b2frame = tk.Frame(bframe)
        b2frame.pack(side='left')

        b3frame = tk.Frame(bframe)
        b3frame.pack(side='left')

        button1 = tk.Button(b1frame, text="Vendas",
                            command=lambda: controller.show_frame("SellsSubmitPage"))
        button2 = tk.Button(b2frame, text="Corte",
                            command=lambda: controller.show_frame("ProductionSubmitPage"))
        button3 = tk.Button(b3frame, text="Estoque",
                            command=lambda: controller.show_frame("StockPage"))

        self.money_icon = ImageTk.PhotoImage(Image.open("./icons/money_icon2.png"))
        # self.money_icon = tk.PhotoImage(file='../icons/money_icon2.png')
        # self.industry_icon = tk.PhotoImage(file='../icons/industry_icon2.png')
        self.industry_icon = ImageTk.PhotoImage(Image.open("./icons/industry_icon2.png"))
        # self.box_icon = tk.PhotoImage(file='../icons/box_icon2.png')
        self.box_icon = ImageTk.PhotoImage(Image.open("./icons/box_icon2.png"))

        button1.config(image=self.money_icon,width="230",height="230")
        button2.config(image=self.industry_icon,width="230",height="230")
        button3.config(image=self.box_icon,width="230",height="230")

        lab1 = tk.Label(b1frame, text="Vendas", font=("Arial", 20))
        lab2 = tk.Label(b2frame, text="Corte", font=("Arial", 20))
        lab3 = tk.Label(b3frame, text="Estoque", font=("Arial", 20))

        lab1.pack(side='bottom')
        lab2.pack(side='bottom')
        lab3.pack(side='bottom')

        button1.pack(side='left')
        button2.pack(side='left')
        button3.pack(side='left')

    def setController(self, controller):
        self.smcontroller = controller
