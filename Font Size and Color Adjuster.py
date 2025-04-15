import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
from desainUI_F1D022096 import Ui_MainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Font Size and Color Adjuster")

        # Styling slider
        slider_style = """
        QSlider::groove:horizontal {
            border: 1px solid #999;
            height: 6px;
            background: #ccc;
            margin: 0px;
            border-radius: 3px;
        }

        QSlider::handle:horizontal {
            background: #888;
            border: 1px solid #666;
            width: 14px;
            height: 14px;
            margin: -5px 0;
            border-radius: 7px;
        }

        QSlider::sub-page:horizontal {
            background: #aaa;
            border-radius: 3px;
        }

        QSlider::add-page:horizontal {
            background: #eee;
            border-radius: 3px;
        }
        """

        self.ui.horizontalSlider.setStyleSheet(slider_style)
        self.ui.horizontalSlider_2.setStyleSheet(slider_style)
        self.ui.horizontalSlider_3.setStyleSheet(slider_style)

        self.ui.horizontalSlider.setMinimum(20)
        self.ui.horizontalSlider.setMaximum(60)
        self.ui.horizontalSlider.setValue(30)

        self.ui.horizontalSlider_2.setMinimum(0)
        self.ui.horizontalSlider_2.setMaximum(255)
        self.ui.horizontalSlider_2.setValue(255)

        self.ui.horizontalSlider_3.setMinimum(0)
        self.ui.horizontalSlider_3.setMaximum(255)
        self.ui.horizontalSlider_3.setValue(0)

        self.ui.horizontalSlider.valueChanged.connect(self.updateFontSize)
        self.ui.horizontalSlider_2.valueChanged.connect(self.updateBackgroundColor)
        self.ui.horizontalSlider_3.valueChanged.connect(self.updateFontColor)

        self.updateFontSize()
        self.updateFontColor()
        self.updateBackgroundColor()

    def updateFontSize(self):
        size = self.ui.horizontalSlider.value()
        font = QFont()
        font.setPointSize(size)
        self.ui.label_2.setFont(font)

    def updateFontColor(self):
        gray = self.ui.horizontalSlider_3.value()
        style = f"color: rgb({gray}, {gray}, {gray});"
        self.ui.label_2.setStyleSheet(style)

    def updateBackgroundColor(self):
        gray = self.ui.horizontalSlider_2.value()
        self.ui.groupBox_3.setStyleSheet(f"background-color: rgb({gray}, {gray}, {gray});")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
