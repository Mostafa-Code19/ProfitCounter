from PyQt5 import QtCore, QtGui, QtWidgets

# UI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 471)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(392, 471))
        MainWindow.setMaximumSize(QtCore.QSize(392, 471))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)

        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")

        self.app__body = QtWidgets.QWidget(MainWindow)
        self.app__body.setStyleSheet("")
        self.app__body.setObjectName("app__body")

        # LABELS

        self.label_howMuchWillYouSelling = QtWidgets.QLabel(self.app__body)
        self.label_howMuchWillYouSelling.setGeometry(QtCore.QRect(40, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Changa")
        font.setPointSize(12)
        self.label_howMuchWillYouSelling.setFont(font)
        self.label_howMuchWillYouSelling.setObjectName("label_howMuchWillYouSelling")

        self.label_priceWhenBought = QtWidgets.QLabel(self.app__body)
        self.label_priceWhenBought.setGeometry(QtCore.QRect(40, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Changa")
        font.setPointSize(12)
        self.label_priceWhenBought.setFont(font)
        self.label_priceWhenBought.setObjectName("label_priceWhenBought")

        self.label_priceWhenSold = QtWidgets.QLabel(self.app__body)
        self.label_priceWhenSold.setGeometry(QtCore.QRect(40, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Changa")
        font.setPointSize(12)
        self.label_priceWhenSold.setFont(font)
        self.label_priceWhenSold.setObjectName("label_priceWhenSold")

        self.label_profitDollar = QtWidgets.QLabel(self.app__body)
        self.label_profitDollar.setGeometry(QtCore.QRect(200, 360, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        self.label_profitDollar.setFont(font)
        self.label_profitDollar.setStyleSheet("")
        self.label_profitDollar.setText("")
        self.label_profitDollar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_profitDollar.setObjectName("label_profitDollar")

        self.label_profitPercent = QtWidgets.QLabel(self.app__body)
        self.label_profitPercent.setGeometry(QtCore.QRect(90, 360, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        self.label_profitPercent.setFont(font)
        self.label_profitPercent.setStyleSheet("")
        self.label_profitPercent.setText("")
        self.label_profitPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.label_profitPercent.setObjectName("label_profitPercent")

        # INPUTS

        self.input_howMuchWillYouSelling = QtWidgets.QLineEdit(self.app__body)
        self.input_howMuchWillYouSelling.setGeometry(QtCore.QRect(240, 40, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_howMuchWillYouSelling.setFont(font)
        self.input_howMuchWillYouSelling.setAutoFillBackground(False)
        self.input_howMuchWillYouSelling.setStyleSheet("border: 2px solid black; color: white; \n"
"background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.523, y2:0, stop:0 rgba(227, 169, 255, 255), stop:1 rgba(33, 10, 127, 255));")
        self.input_howMuchWillYouSelling.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_howMuchWillYouSelling.setText("")
        self.input_howMuchWillYouSelling.setAlignment(QtCore.Qt.AlignCenter)
        self.input_howMuchWillYouSelling.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_howMuchWillYouSelling.setObjectName("input_howMuchWillYouSelling")

        self.input_priceWhenBought = QtWidgets.QLineEdit(self.app__body)
        self.input_priceWhenBought.setGeometry(QtCore.QRect(240, 120, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_priceWhenBought.setFont(font)
        self.input_priceWhenBought.setAutoFillBackground(False)
        self.input_priceWhenBought.setStyleSheet("border: 2px solid black; color: white; \n"
"background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.523, y2:0, stop:0 rgba(227, 169, 255, 255), stop:1 rgba(33, 10, 127, 255));")
        self.input_priceWhenBought.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_priceWhenBought.setText("")
        self.input_priceWhenBought.setAlignment(QtCore.Qt.AlignCenter)
        self.input_priceWhenBought.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_priceWhenBought.setObjectName("input_priceWhenBought")

        self.input_priceWhenSold = QtWidgets.QLineEdit(self.app__body)
        self.input_priceWhenSold.setGeometry(QtCore.QRect(240, 200, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_priceWhenSold.setFont(font)
        self.input_priceWhenSold.setAutoFillBackground(False)
        self.input_priceWhenSold.setStyleSheet("border: 2px solid black; color: white; \n"
"background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.523, y2:0, stop:0 rgba(227, 169, 255, 255), stop:1 rgba(33, 10, 127, 255));")
        self.input_priceWhenSold.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_priceWhenSold.setText("")
        self.input_priceWhenSold.setAlignment(QtCore.Qt.AlignCenter)
        self.input_priceWhenSold.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_priceWhenSold.setObjectName("input_priceWhenSold")

        # BUTTONS

        self.btn_count = QtWidgets.QPushButton(self.app__body)
        self.btn_count.setGeometry(QtCore.QRect(150, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Changa")
        font.setPointSize(10)
        self.btn_count.setFont(font)
        self.btn_count.setMouseTracking(False)
        self.btn_count.setStyleSheet("border: 2px solid purple;")
        self.btn_count.setObjectName("btn_count")
        self.btn_count.clicked.connect(self.profitCounter)
        
        MainWindow.setCentralWidget(self.app__body)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Profit Counter"))
        self.label_howMuchWillYouSelling.setText(_translate("MainWindow", "How much will you sell"))
        self.label_priceWhenBought.setText(_translate("MainWindow", "Price when you bough"))
        self.label_priceWhenSold.setText(_translate("MainWindow", "Price When you sold"))
        self.btn_count.setText(_translate("MainWindow", "Count 💲"))
        self.input_howMuchWillYouSelling.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.input_priceWhenBought.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.input_priceWhenSold.setPlaceholderText(_translate("MainWindow", "0.00"))

    # Code

    def profitCounter(self):

        howMuchWillYouSelling = float(self.input_howMuchWillYouSelling.text())
        priceWhenBought = float(self.input_priceWhenBought.text())
        priceWhenSold = float(self.input_priceWhenSold.text())

        # if howMuchWillYouSelling == None or priceWhenBought == None or priceWhenSold == None:
        profitPercent = f'{round((priceWhenSold / priceWhenBought * 100 - 100), 2)}%'
        profitDollar = f'{round((howMuchWillYouSelling * priceWhenSold - howMuchWillYouSelling * priceWhenBought), 2)}$'

        print(profitPercent, profitDollar)

        self.label_profitPercent.setText(profitPercent)
        self.label_profitDollar.setText(profitDollar)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())