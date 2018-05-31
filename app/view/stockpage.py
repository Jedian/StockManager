import Tkinter as tk
from tkintertable import *

class StockPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
	self.currentPage = 1
	self.totalPages = 25

	# tabela
	self.setTable()

	# voltar + pesquisa
        self.label = tk.Label(self, text="This is page 3")
        self.dataEntry = tk.Entry(self)
        self.backbutton = tk.Button(self, text="Voltar",
                           command=lambda: controller.show_frame("StartPage"))

        self.label.pack(side="top", fill="x", pady=10)
        self.dataEntry.pack()
        self.backbutton.pack(side='bottom')

    def setTableModel(self):
	model = TableModel(rows=10, columns=8)
	colidx = 1
	for col in ['Ref.', 'PP', 'P', 'M', 'G', 'GG', 'XGG', 'XXGG']:
	    model.columnlabels[str(colidx)] = col
	    colidx = colidx+1
	return model

    def setTable(self):
	# tabela + botoes tabela
	aframe = tk.Frame(self)
	aframe.pack(side='left', fill='both', expand=True)

	# botoes tabela
	bframe = tk.Frame(aframe)
	bframe.pack(side='bottom')
        self.nextbutton = tk.Button(bframe, text="Proxima pagina", command=lambda: self.nextPage())
        self.prevbutton = tk.Button(bframe, text="Pagina anterior", command=lambda: self.prevPage())
        self.nextbutton.pack(side='right')
        self.prevbutton.pack(side='right')

	# tabela
	tframe = tk.Frame(aframe, height=1500, width=1500)
	tframe.pack(side='left', fill='both', expand=True)

	
        table = TableCanvas(tframe, model=self.setTableModel())
        table.createTableFrame()
	table.addRow()
	#model.importDict(test)

    def setTableContent(self, data):
	#todo
	return 1

    def nextPage(self):
	#if self.currentPage != self.totalPages:
	#    self.currentPage = self.currentPage + 1
	#    self.setTableContent(self.controller.getPageContent(self.currentPage))
	#todo
	return 1

    def prevPage(self):
	#if self.currentPage != 1:
	#    self.currentPage = self.currentPage - 1
	#    self.setTableContent(self.controller.getPageContent(self.currentPage))
	#todo
	return 1	
