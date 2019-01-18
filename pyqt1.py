from PyQt5.QtWidgets import *

app=QApplication([])

root=QWidget()
root.setWindowTitle("Super Market Management System")
root.setGeometry(500,300,500,500)
root.show()

b1=QPushButton(root)
b1.move(50,20)
