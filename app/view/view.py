# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.font as tkfont
from .startpage import StartPage
from .productionsubmitpage import ProductionSubmitPage
from .sellssubmitpage import SellsSubmitPage
from .stockpage import StockPage

class StockManagerView(tk.Tk):

    def __init__(self, controller, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Controlador de estoque')
        self.geometry('{}x{}'.format(800, 600))
        self.smcontroller = controller
        # tk.Tk.resizable(self, width=False, height=False)

        # self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, height=600, width=800)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in [StartPage, SellsSubmitPage, ProductionSubmitPage,
                StockPage]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.setController(self.smcontroller)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
