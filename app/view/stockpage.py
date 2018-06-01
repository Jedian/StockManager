# -*- coding: utf-8 -*-,
import Tkinter as tk
from tkintertable import *

class StockPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
	self.currentPage = 1
	self.prodPerPage = 6
	self.totalPages = (60 + (self.prodPerPage-1))/self.prodPerPage
        self.totalPadding = 6
        self.totalRows = self.prodPerPage*self.totalPadding
        self.totalCols = 7
        self.smcontroller = None

	# voltar + pesquisa
        self.label = tk.Label(self, text="Tabela de saldo")
        self.backbutton = tk.Button(self, text="Voltar",
                           command=lambda: controller.show_frame("StartPage"))

        self.label.pack(side="top", fill="x", pady=10)
        self.backbutton.pack(side='bottom')

    def setController(self, controller):
        self.smcontroller = controller
	self.setTable()

    def setTableModel(self):
	model = TableModel(rows=self.totalRows, columns=self.totalCols)
	colidx = 1
	for col in ['Ref.', 'PP', 'P', 'M', 'G', 'GG', 'XGG']:
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

        self.table = TableCanvas(tframe, model=self.setTableModel(),
                thefont=("Arial", 16), editable=False, rowheight=25)
        self.table.createTableFrame()
        self.setTableContent(self.currentPage)
	#model.importDict(test)

    def clearTableContent(self):
        for row in xrange(0, self.totalRows):
            for col in xrange(0, self.totalCols+1):
                self.table.model.data[row][str(col)] = ""

    def setTableStyle(self, content):
        ri = 0
        while ri < len(content):
            #colors
            self.table.model.setColorAt(ri*self.totalPadding, 0, '#5e5e5e', key='bg')
            self.table.model.setColorAt(ri*self.totalPadding, 0, 'white', key='fg')
            self.table.model.setColorAt(ri*self.totalPadding, 1, 'white', key='fg')
            self.table.model.setColorAt(ri*self.totalPadding + 1, 0, 'green', key='fg')
            self.table.model.setColorAt(ri*self.totalPadding + 2, 0, 'red', key='fg')
            self.table.model.setColorAt(ri*self.totalPadding + 3, 0, 'blue', key='fg')

            for i, j in zip(xrange(2, 8), ['pp', 'p', 'm', 'g', 'gg', 'xgg']):
                self.table.model.setColorAt(ri*self.totalPadding, i-1, '#5e5e5e', key='bg')
                self.table.model.setColorAt(ri*self.totalPadding, i-1, 'white', key='fg')
                self.table.model.setColorAt(ri*self.totalPadding + 1, i-1, 'green', key='fg')
                self.table.model.setColorAt(ri*self.totalPadding + 2, i-1, 'red', key='fg')
                self.table.model.setColorAt(ri*self.totalPadding + 3, i-1, 'blue', key='fg')

            ri = ri+1

    def setTableContent(self, page):
        stockcontent, productscontent = self.smcontroller.getStockPageContent(self.currentPage)
        self.clearTableContent()
        self.setTableStyle(stockcontent)

        ri = 0
        while ri < len(stockcontent):
            productname = productscontent[stockcontent[ri]['ref']].split(' ')
            self.table.model.data[ri*self.totalPadding]['1'] = str(stockcontent[ri]['ref'])
            self.table.model.data[ri*self.totalPadding + 1]['1'] = 'Corte'
            self.table.model.data[ri*self.totalPadding + 2]['1'] = 'Venda'
            self.table.model.data[ri*self.totalPadding + 3]['1'] = 'Saldo'
            
            for i, j in zip(xrange(2, 8), ['pp', 'p', 'm', 'g', 'gg', 'xgg']):
                if i-2 < len(productname):  
                    self.table.model.data[ri*self.totalPadding][str(i)] = productname[i-2]
                self.table.model.data[ri*self.totalPadding + 1][str(i)] = str(stockcontent[ri]['val'][j]['p'])
                self.table.model.data[ri*self.totalPadding + 2][str(i)] = str(stockcontent[ri]['val'][j]['s'])
                self.table.model.data[ri*self.totalPadding + 3][str(i)] = str(stockcontent[ri]['val'][j]['st'])

            ri = ri+1

        self.table.redrawTable()
	return 1

    def nextPage(self):
	if self.currentPage != self.totalPages:
	    self.currentPage = self.currentPage + 1
            self.setTableContent(self.currentPage)
	#todo
	return 1

    def prevPage(self):
	if self.currentPage != 1:
	    self.currentPage = self.currentPage - 1
            self.setTableContent(self.currentPage)
	#todo
	return 1	
