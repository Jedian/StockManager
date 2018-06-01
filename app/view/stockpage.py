import Tkinter as tk
from tkintertable import *

class StockPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
	self.currentPage = 1
	self.totalPages = 25
        self.smcontroller = None
	# tabela

	# voltar + pesquisa
        self.label = tk.Label(self, text="This is page 3")
        self.dataEntry = tk.Entry(self)
        self.backbutton = tk.Button(self, text="Voltar",
                           command=lambda: controller.show_frame("StartPage"))

        self.label.pack(side="top", fill="x", pady=10)
        self.dataEntry.pack()
        self.backbutton.pack(side='bottom')

    def setController(self, controller):
        self.smcontroller = controller
	self.setTable()

    def setTableModel(self):
	model = TableModel(rows=550, columns=8)
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

        self.table = TableCanvas(tframe, model=self.setTableModel())
        self.table.createTableFrame()
        self.setTableContent(self.currentPage)
	#model.importDict(test)

    def setTableContent(self, page):
        stockcontent = self.smcontroller.getStockPageContent(self.currentPage)
        lineno = 1
        ri = 0
        while ri < len(stockcontent):
            self.table.model.data[ri*5]['1'] = str(stockcontent[ri]['ref'])
            self.table.model.data[ri*5 + 1]['1'] = 'Corte'
            self.table.model.data[ri*5 + 2]['1'] = 'Venda'
            self.table.model.data[ri*5 + 3]['1'] = 'Saldo'

            for i, j in zip(xrange(2, 8), ['pp', 'p', 'm', 'g', 'gg', 'xgg']):
                self.table.model.data[ri*5][str(i)] = '----------------'
                self.table.model.data[ri*5 + 1][str(i)] = str(stockcontent[ri]['val'][j]['p'])
                self.table.model.data[ri*5 + 2][str(i)] = str(stockcontent[ri]['val'][j]['s'])
                self.table.model.data[ri*5 + 3][str(i)] = str(stockcontent[ri]['val'][j]['st'])

            ri = ri+1

        self.table.redrawTable()
        print(stockcontent[0])
	#todo
	return 1

    def nextPage(self):
	#if self.currentPage != self.totalPages:
	#    self.currentPage = self.currentPage + 1
        #    self.setTableContent(self.currentPage)
	#todo
	return 1

    def prevPage(self):
	#if self.currentPage != 1:
	#    self.currentPage = self.currentPage - 1
        #    self.setTableContent(self.currentPage)
	#todo
	return 1	
