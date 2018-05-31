import sys
sys.path.append('.\\app')
# sys.path.append('./app/model')
# sys.path.append('C:\\Users\\jedian\\StockManager\\app\\view')
# sys.path.append('.\\app/controller')
import app.view.view as view
import app.controller.controller as controller
# import view, controller

app = controller.StockManagerController(view, controller)
app.start()
