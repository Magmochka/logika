from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

def show_win():
    victory_win = QMessageBox()
    victory_win.setText("Правильно😎")
    victory_win.exec_()

def show_lose():
    victory_lose = QMessageBox()
    victory_lose.setText(" Не правильно😝")
    victory_lose.exec_()

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("конкус від CRazy People")
main_win.resize(400,200)

quetion = QLabel("В якому році канал отримав <золоту кнопку> від YouTube?")

button1 = QRadioButton("2005")
button2 = QRadioButton("2010")
button3 = QRadioButton("2015")
button4 = QRadioButton("2020")

layuotH1 = QHBoxLayout()
layuotH2 = QHBoxLayout()
layuotH3 = QHBoxLayout()



layuotH1.addWidget(quetion, alignment = Qt.AlignCenter)
layuotH2.addWidget(button1, alignment = Qt.AlignCenter)
layuotH2.addWidget(button2, alignment = Qt.AlignCenter)
layuotH3.addWidget(button3, alignment = Qt.AlignCenter)
layuotH3.addWidget(button4, alignment = Qt.AlignCenter)

line = QVBoxLayout()
line.addLayout(layuotH1)
line.addLayout(layuotH2)
line.addLayout(layuotH3)

button1.clicked.connect(show_win)
button2.clicked.connect(show_lose)
button3.clicked.connect(show_lose)
button4.clicked.connect(show_lose)



main_win.setLayout(line) 
main_win.show()
app.exec_()












