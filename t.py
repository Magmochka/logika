#підключення модулів
from PyQt5.QtCore import Qt      
from PyQt5.QtWidgets import *  
from random import randint

app = QApplication([]) #об'єкт програм

#створюємо вікно
main_wind = QWidget()
main_wind.resize(400, 400)
main_wind.move(100, 100)
main_wind.setWindowTitle("Лотерея")

#створюємо віджети(кнопки та надписи)
num1 = QLabel("?")
num2 = QLabel("?")
text = QLabel("Натисни, щоб взяти участь")
button = QPushButton("Випробувати Удачу")

#розміщення віджетів
line = QVBoxLayout()
line.addWidget(text, alignment= Qt.AlignCenter)
line.addWidget(num1, alignment= Qt.AlignCenter)
line.addWidget(num2, alignment= Qt.AlignCentrer)
line.addWidget(button, alignment= Qt.AlignCenter)

main_wind.setLayout(line) #встановлюємо макет на вікно

#функція яка генерує та кохує числа
def rand():
    n1 = randint(0, 9)
    n2 = randint(0, 9)
    num1.setText(str(n1))
    num2.setText(str(n2))
    if n1 == n2:
        text.setText("ви виграли! Зіграйте знов")
    else:
        text.setText("ви програли! Зіграйте знов")

button.clicked.connect(rand)

main_wind.show()# показати вікно
app.exec_()#щоб автоматично не завершувалось



