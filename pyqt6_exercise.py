# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# import sys
#
# app = QApplication(sys.argv)  # 创建一个应用
#
# # print(sys.argv)
# # print(app.arguments())
#
# window = QWidget()
# window.setWindowTitle("Learn Python")
# window.resize(400, 300)
# window.move(20, 20)
# window.show()
#
# label = QLabel()
# label.setText("Hello World!")
# label.move(80, 80)
# label.resize(150, 50)
# label.setStyleSheet("background-color:yellow;padding:12px")
# label.setParent(window)
# label.show()
#
# sys.exit(app.exec())  # 开始执行程序, 并且进入消息循环等待

# # 调用保存的ui文件
# import sys
#
# from PyQt6.QtWidgets import QApplication, QLabel
# from PyQt6 import uic
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = uic.loadUi("./materials/test_02.ui")
#
#     myLabel: QLabel = ui.label  # 获取label对象
#     print(myLabel.text())
#     ui.show()
#
#     sys.exit(app.exec())
#
# 写一个__main__函数调用pyuic转换成的py文件
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from materials.test_01 import Ui_Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()

    Ui_Form().setupUi(w)
    w.show()

    sys.exit(app.exec())
