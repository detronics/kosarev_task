
from PyQt5.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 150)
w.move(550, 300)
w.setWindowTitle('Simple')
w.show()

sys.exit(app.exec_())







