import sys
from MainFrame import Ui_Form
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMouseEvent, QCursor , QMovie
from sheetstyle import *


class MyMainFrame(QtWidgets.QWidget, Ui_Form):

    max_flag = False
    mic_status_flag = True
    link_status_flag = False

    def __init__(self):
        super(MyMainFrame, self).__init__()
        self.setupUi(self)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
       if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


def init_ui():
    my_form.setWindowFlag(Qt.FramelessWindowHint)
    my_form.setStyleSheet(form_background_style)
    my_form.pushButton_min.setStyleSheet(min_btn_style)
    my_form.pushButton_mid.setStyleSheet(mid_btn_style)
    my_form.pushButton_close.setStyleSheet(close_btn_style)
    my_form.pushButton_main.setStyleSheet(main_btn_style)
    my_form.pushButton_light.setStyleSheet(light_btn_style)
    my_form.pushButton_tempature.setStyleSheet(tempature_btn_style)
    my_form.pushButton_main.setStyleSheet('QPushButton{'
                                          'border-image: url(icons/Main_on.png)'
                                          '}')
    my_form.pushButton_mic.setStyleSheet('QPushButton{'
                                          'border-image: url(icons/mic1.png)'
                                          '}')
    my_form.pushButton_link.setStyleSheet('QPushButton{'
                                         'border-image: url(icons/link_close1.png)'
                                         '}')

    my_form.groupBox_fjdw.setStyleSheet(radio_btn_style)
    my_form.groupBox_dbyd.setStyleSheet(radio_btn_style)
    my_form.groupBox_jdms.setStyleSheet(radio_btn_style)
    my_form.groupBox_left.setStyleSheet(radio_btn_style)
    my_form.groupBox_right.setStyleSheet(radio_btn_style)
    my_form.verticalSlider_sx_1.setStyleSheet(horizontal_slider_style)
    my_form.horizontalSlider_red.setStyleSheet(horizontal_slider_style)
    my_form.horizontalSlider_blue.setStyleSheet(horizontal_slider_style)
    my_form.horizontalSlider_green.setStyleSheet(horizontal_slider_style)
    my_form.horizontalSlider_cold_hot.setStyleSheet(horizontal_slider_style)
    my_form.horizontalSlider_left_bottom.setStyleSheet(horizontal_slider_style)
    my_form.horizontalSlider_right_bottom.setStyleSheet(horizontal_slider_style)
    my_form.verticalSlider_sx_1.setStyleSheet(vertical_slider_style)
    my_form.verticalSlider_sx_2.setStyleSheet(vertical_slider_style)
    show_gif()


def show_full_window():
    if my_form.max_flag:
        my_form.max_flag = False
        my_form.showNormal()
    else:
        my_form.max_flag = True
        my_form.showMaximized()


def clear_btn_checked_status():
    my_form.pushButton_main.setChecked(False)
    my_form.pushButton_light.setChecked(False)
    my_form.pushButton_tempature.setChecked(False)


def clicked_main_btn():
    clear_btn_checked_status()
    my_form.pushButton_main.setStyleSheet('QPushButton{'
                                          'border-image: url(icons/Main_on.png)'
                                          '}')
    my_form.pushButton_light.setStyleSheet(light_btn_style)
    my_form.pushButton_tempature.setStyleSheet(tempature_btn_style)
    my_form.tabWidget.setCurrentIndex(0)


def clicked_light_btn():
    clear_btn_checked_status()
    my_form.pushButton_main.setStyleSheet(main_btn_style)
    my_form.pushButton_light.setStyleSheet('QPushButton{'
                                           'border-image: url(icons/Light_hover.png)'
                                           '}')
    my_form.pushButton_tempature.setStyleSheet(tempature_btn_style)
    my_form.tabWidget.setCurrentIndex(1)


def clicked_tempature_btn():
    clear_btn_checked_status()
    my_form.pushButton_main.setStyleSheet(main_btn_style)
    my_form.pushButton_light.setStyleSheet(light_btn_style)
    my_form.pushButton_tempature.setStyleSheet('QPushButton{'
                                               'border-image: url(icons/Tempature_hover.png)'
                                               '}')
    my_form.tabWidget.setCurrentIndex(2)


def clicked_mic_btn():
    my_form.mic_status_flag = not my_form.mic_status_flag
    if my_form.mic_status_flag:
        my_form.pushButton_mic.setStyleSheet('QPushButton{'
                                             'border-image: url(icons/mic1.png)'
                                             '}')
    else:
        my_form.pushButton_mic.setStyleSheet('QPushButton{'
                                             'border-image: url(icons/mic2.png)'
                                             '}')


def clicked_link_btn():
    my_form.link_status_flag = not my_form.link_status_flag
    if my_form.link_status_flag:
        my_form.pushButton_link.setStyleSheet('QPushButton{'
                                             'border-image: url(icons/link_open1.png)'
                                             '}')
    else:
        my_form.pushButton_link.setStyleSheet('QPushButton{'
                                             'border-image: url(icons/link_close1.png)'
                                             '}')


def show_gif():
    gif = QMovie('test.gif')
    my_form.label_gif.setMovie(gif)
    gif.start()


def init_signal():
    my_form.pushButton_min.clicked.connect(lambda: my_form.showMinimized())
    my_form.pushButton_mid.clicked.connect(show_full_window)
    my_form.pushButton_close.clicked.connect(lambda: my_form.close())
    my_form.pushButton_main.clicked.connect(clicked_main_btn)
    my_form.pushButton_light.clicked.connect(clicked_light_btn)
    my_form.pushButton_tempature.clicked.connect(clicked_tempature_btn)
    my_form.pushButton_mic.clicked.connect(clicked_mic_btn)
    my_form.pushButton_link.clicked.connect(clicked_link_btn)


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        my_form = MyMainFrame()
        init_ui()
        init_signal()
        my_form.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)