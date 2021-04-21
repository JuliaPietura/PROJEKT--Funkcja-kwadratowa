import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout, QLineEdit

print(sys.path)
#widgets init to be used in our app

widgets = {
    "logo": [],
    "btn": [],
    "btn2": [],
    "btn3": [],
    "text": [],
    "title": [],
    "a": [],
    "b": [],
    "c": [],
    "r": [],
    "d": [],
    "x_start": [],
    "x_stop": [],
    "msg": []
           }

#this function is clearing widgets to use one main window instead of opening next


def clear_widgets():
    for widget in widgets:
        if widgets[widget]:
            widgets[widget][-1].hide()
            for i in range(0, len(widgets[widget])):
                widgets[widget].pop()

#starting function


def start():
    clear_widgets()
    frame2()
#restarting function


def restart():
    os.execv(sys.executable, ['python'] + sys.argv)

#result function


def result():
    clear_widgets()

    #handling exceptions in our case if input is string or int
    try:
        a = float(input_a.text())
        b = float(input_b.text())
        c = float(input_c.text())
        x_sta = float(x_start.text())
        x_sto = float(x_stop.text())
        delta = b*b-4*a*c
        r = QLabel("Your delta is: "+str(delta) + "\n\n Thanks for using our app")
        r.setAlignment(QtCore.Qt.AlignCenter)
        r.setStyleSheet("color: white;" +
                           "font-size: 35px;" +
                           "padding: 25px 20px;" +
                           "margin-top: 100px"
                           )

        widgets['r'].append(r)
        grid.addWidget(widgets["r"][-1], 0, 0)
        #plotting chart

        x = np.linspace(x_sta, x_sto)
        y = a * x * x + b * x + c
        plt.plot(x, y)
        plt.xlabel('x_values')
        plt.ylabel('y_values')
        plt.title('Calc_Delta_Graph')
        plt.grid(True)
        plt.show()
    except ValueError:
        frame3()


#frame 1 structure
def frame():
    logo = QLabel()
    image = QPixmap("logo2.png")
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)
    grid.addWidget(widgets["logo"][-1], 0, 0)

    btn = QPushButton("START")
    btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    btn.setStyleSheet("*{border: 4px solid '#BC006C';" +
                      "border-radius: 45px;" +
                      "font-size: 35px;" +
                      "color: 'white';" +
                      "padding: 25px 0;" +
                      "margin: 100px 200px;}" +
                      "*:hover{background: '#BC006C';}"
                      )
    btn.clicked.connect(start)
    widgets["btn"].append(btn)

    grid.addWidget(widgets["btn"][-1], 1, 0)

#frame2 structure


def frame2():
    text = QLabel("Time to do some math")
    text.setAlignment(QtCore.Qt.AlignCenter)
    text.setStyleSheet("color: white;" +
                       "font-size: 35px;" +
                       "padding: 25px 20px;" +
                       "margin-top: 100px"
                       )
    widgets["text"].append(text)
    grid.addWidget(widgets["text"][-1], 0, 0)

    input_a.setStyleSheet("margin: 0 300px;" +
                          "color: white;")
    widgets["a"].append(input_a)
    grid.addWidget(widgets["a"][-1], 1, 0)

    input_b.setStyleSheet("margin: 0 300px;" +
                          "color: white;")
    widgets["b"].append(input_b)
    grid.addWidget(widgets["b"][-1], 2, 0)

    input_c.setStyleSheet("margin: 0 300px;" +
                          "color: white;")
    widgets["c"].append(input_c)
    grid.addWidget(widgets["c"][-1], 3, 0)

    x_start.setStyleSheet("margin: 0 300px;" +
                          "color: white;")

    widgets["x_start"].append(x_start)
    grid.addWidget(widgets["x_start"][-1], 4, 0)

    x_stop.setStyleSheet("margin: 0 300px;" +
                         "color: white;")

    widgets["x_stop"].append(x_stop)
    grid.addWidget(widgets["x_stop"][-1], 5, 0)

    btn2 = QPushButton("RESULT")
    btn2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    btn2.setStyleSheet("*{border: 4px solid '#BC006C';" +
                       "border-radius: 45px;" +
                       "font-size: 35px;" +
                       "color: 'white';" +
                       "padding: 25px 0;" +
                       "margin: 100px 200px;}" +
                       "*:hover{background: '#BC006C';}"
                      )
    btn2.clicked.connect(result)
    widgets["btn2"].append(btn2)

    grid.addWidget(widgets["btn2"][-1], 6, 0)
#frame 3 structure


def frame3():
    msg = QLabel("Invalid type")
    msg.setAlignment(QtCore.Qt.AlignCenter)
    msg.setStyleSheet("color: white;" +
                       "font-size: 35px;" +
                       "padding: 25px 20px;" +
                       "margin-top: 100px"
                       )
    widgets["msg"].append(msg)
    grid.addWidget(widgets["msg"][-1], 0, 0)

    btn3 = QPushButton("TRY AGAIN")
    btn3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    btn3.setStyleSheet("*{border: 4px solid '#BC006C';" +
                       "border-radius: 45px;" +
                       "font-size: 35px;" +
                       "color: 'white';" +
                       "padding: 25px 0;" +
                       "margin: 100px 200px;}" +
                       "*:hover{background: '#BC006C';}"
                       )
    btn3.clicked.connect(restart)
    widgets["btn3"].append(btn3)

    grid.addWidget(widgets["btn3"][-1], 1, 0)

#app initiaition with global variables and our grid


app = QApplication(sys.argv)
x_start = QLineEdit("Enter start value of X")
x_stop = QLineEdit("Enter stop value of X")
input_a = QLineEdit("ENTER A")
input_b = QLineEdit("ENTER B")
input_c = QLineEdit("ENTER C")
window = QWidget()
window.setWindowTitle("Calc Delta")
window.setWindowIcon(QIcon("logo.png"))
window.setFixedWidth(1000)
window.setStyleSheet("background:#161219;")

grid = QGridLayout()
frame()
window.setLayout(grid)
window.show()
sys.exit(app.exec_())










