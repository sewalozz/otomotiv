# from tkinter import *
 
# def set():
#     print("Hello World")

# labelyazi = "adsfdsa"

# windows = Tk()
# windows.geometry("480x240")
 
# frame = Frame(windows)
# frame.pack()
# label = Label(frame,fg="black", textvariable = labelyazi )
# label.pack()
# button = Button(frame, text = "Merhaba De", command = set)
# button.pack()
# image = PhotoImage(file="intro_ball.gif") 
 
# label2 = Label(frame, image = image)
# label2.pack(padx=0,pady=300)""

 
# windows.mainloop()

from PyQt5.QtWidgets import QMessageBox,QApplication, QWidget, QPushButton, QVBoxLayout
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
buton = QPushButton('Top')
buton.clicked.connect(on_button_clicked)
layout.addWidget(buton)
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()