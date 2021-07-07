# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import re
from tkintertable import *

class SellsSubmitPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.rowIter=0
        self.totalRows=100
        self.totalCols=7

        self.label = tk.Label(self, text="Digite no campo abaixo a referência e a quantidade vendida para cada tamanho.")
        self.dataEntry = tk.Entry(self, font=("Arial", 16), width=30)
        self.bbutton = tk.Button(self, text="Voltar", command=lambda: controller.show_frame("StartPage"))
        self.scbutton = tk.Button(self, text="Salvar e limpar", command=lambda: self.saveAndClean())

        self.label.pack(side="top", fill="x", pady=10)
        self.dataEntry.bind("<Return>", self.teste)
        self.dataEntry.pack()
        self.bbutton.pack(side='bottom')
        self.scbutton.pack(side='bottom')
        self.setHistoryTable()

    def setController(self, controller):
        self.smcontroller = controller

    def teste(self, event):
        inp = self.dataEntry.get().split(' ')
        if inp == []:
            return

        try:
            self.dataEntry.delete(0, len(self.dataEntry.get()))
            tr = {'PP': '2', 'P': '3', 'M': '4', 'G': '5', 'GG': '6', 'XGG': '7'}
            self.table.model.data[self.rowIter]['1'] = inp[0]
            for entry in inp[1:]:
                qt = re.search("[0-9]+", str(entry)).group()
                tam = re.search("[a-z]+", str(entry)).group()
                self.table.model.data[self.rowIter][tr[tam.upper()]] = qt
        except Exception as e:
            messagebox.showerror('Erro!', "Você provavelmente digitou algo errado, tente novamente. Caso o erro persista, talvez você devesse informar ao Jedian: " + str(e.message))

        self.table.redrawTable()
        self.rowIter = self.rowIter + 1 


    def setHistoryTable(self):
        tframe = tk.Frame(self)
        tframe.pack(side='bottom', fill='y', expand=True)

        self.table = TableCanvas(tframe, model=self.setTableModel(), thefont=("Arial", 16),
                editable=True, rowheight=25, cellwidth=70)

        self.table.createTableFrame()
    
    def setTableModel(self):
        model = TableModel(rows=self.totalRows, columns=self.totalCols)
        colidx = 1
        for col in ['Ref.', 'PP', 'P', 'M', 'G', 'GG', 'XGG']:
            model.columnlabels[str(colidx)] = col
            colidx = colidx + 1
        return model

    def clearTableContent(self):
        for row in range(0, self.totalRows):
            for col in range(0, self.totalCols+1):
                self.table.model.data[row][str(col)] = ""

    def saveAndClean(self):
        data = {}
        tr = {'2':'pp', '3': 'p', '4':'m', '5':'g', '6':'gg', '7':'xgg'}
        for row in range(0, self.rowIter):
            if self.table.model.data[row]['1'] != "":
                data[str(self.table.model.data[row]['1'])] = {'pp':0, 'p':0, 'm':0, 'g':0, 'gg':0, 'xgg':0}

        for row in range(0, self.rowIter):
            for col in range(2, self.totalCols+1):
                if str(col) in self.table.model.data[row] and self.table.model.data[row][str(col)] != "":
                    data[str(self.table.model.data[row]['1'])][tr[str(col)]] = data[str(self.table.model.data[row]['1'])][tr[str(col)]]  + int(self.table.model.data[row][str(col)])
        try:
            self.smcontroller.saveData(data, 'venda')
            self.clearTableContent()
            self.table.redrawTable()
        except Exception as e:
            messagebox.showerror('Erro!', e.message)
