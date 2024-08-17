from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

menu_win = QWidget()
menu_win.resize(400, 30)                           
menu_win.move(300, 300)                                
menu_win.setWindowTitle("Меню")                     

#Поля для запитань
#--------------------------------------------------------------
txt_Question = QLineEdit("")
txt_Answer = QLineEdit("")
txt_Wrong1 = QLineEdit("")
txt_Wrong2 = QLineEdit("")
txt_Wrong3 = QLineEdit("")


#Групування полей для запитань
#---------------------------------------------------------------
Loyout_form = QFormLayout()
Loyout_form.addRow("Введіть запитання:",txt_Question)
Loyout_form.addRow("Введіть вірну відповідь:",txt_Answer)
Loyout_form.addRow("Введіть першу хибну відповідь:",txt_Wrong1)
Loyout_form.addRow("Введіть другу хибну відповідь:",txt_Wrong2)
Loyout_form.addRow("Введіть третю хибну відповідь:",txt_Wrong3)


#Кнопки вікна меню
#---------------------------------------------------------------
btn_add_q = QPushButton("Додати запитання")
btn_back = QPushButton("Назад")
btn_clear = QPushButton("Очистити")

#Add statistics Label
lbl_statistics = QLabel("")

#Статистика
lbl_statistics = QLabel("Статистика:\nПравильних відповідей: 0\nЗагальна кількість спроб: 0")

#Макети для віджетів
hbtn = QHBoxLayout()
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)


#Макет для основного вікна
vline = QVBoxLayout()
vline.addLayout(Loyout_form)
vline.addLayout(hbtn)
vline.addWidget(lbl_statistics)#додаємо його на макет

menu_win.setLayout(vline)



menu_win.show()
app.exec_()


