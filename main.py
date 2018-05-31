#! /usr/bin/python

import sys
sys.path.append('.\\app')
# sys.path.append('./app/model')
# sys.path.append('C:\\Users\\jedian\\StockManager\\app\\view')
# sys.path.append('.\\app/controller')
import app.model.model as model
import app.view.view as view
import app.controller.controller as controller

app = controller.StockManagerController(model, view, controller)
app.start()
