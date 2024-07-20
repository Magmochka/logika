# Підключення модуля та бібліотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


app = QApplication([]) #створюємо додаток

main_wind = QWidget() #Створюємо обєкт вікно
main_wind.resize(400, 200)
main_wind.move(200, 200)

btn1 = QPushButton("Згенерувати") # Створюємо кнопку
text = QLabel("Переможець")

line = QVBoxLayout() # Вертикальна лінія
line.addWidget(btn1, alignment= Qt.AlignCenter)
line.addWidget(text, alignment= Qt.AlignCenter)

main_wind.setLayout(line)
main_wind.show() 
app.exec_()














