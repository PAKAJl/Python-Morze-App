import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLabel, QGridLayout


def click_event():
    lable.setText("123")


# initialize GIU on pyQT5
app = QApplication(sys.argv)

main_window = QMainWindow()
main_window.setWindowTitle("Morze")

grid_layout = QGridLayout()

button = QPushButton("Click here")
lable = QLabel("Morze Text")

grid_layout.addWidget(lable)
grid_layout.addWidget(button)

button.clicked.connect(lambda: click_event())

widget = QWidget()

widget.setLayout(grid_layout)
main_window.setCentralWidget(widget)
main_window.show()

sys.exit(app.exec_())
