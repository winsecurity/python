import sys
from PyQt5 import QtWidgets

def window():
    app=QtWidgets.QApplication(sys.argv)   
    w=QtWidgets.QWidget()        #creating a window
    w.setWindowTitle("Basic Reconnaisance Tool")   #setting the title for the window
    w.show()            #displaying the window
    sys.exit(app.exec_())
    

window()
