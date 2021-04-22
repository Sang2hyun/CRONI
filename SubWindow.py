import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.diglab = QLabel(' 증상 만족 유무 ')
        self.ranklab = QLabel(' rank up ')
        self.diglab.setAlignment(Qt.AlignCenter)
        self.ranklab.setAlignment(Qt.AlignCenter)
        grid = QGridLayout()
        grid.addWidget(self.diglab, 0, 0)
        grid.addWidget(self.dignosisgroup(), 1, 0)
        grid.addWidget(self.ranklab, 2, 0)
        grid.addWidget(self.rankupgroup(), 3, 0)


        self.setLayout(grid)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def dignosisgroup(self):
        groupbox = QGroupBox('')


        symptom1 = QCheckBox('1번')
        symptom2 = QCheckBox('2번')
        symptom3 = QCheckBox('3번')
        symptom4 = QCheckBox('4번')
        symptom5 = QCheckBox('5번')
        symptom6 = QCheckBox('6번')


        vbox = QVBoxLayout()
        vbox.addWidget(symptom1)
        vbox.addWidget(symptom2)
        vbox.addWidget(symptom3)
        vbox.addWidget(symptom4)
        vbox.addWidget(symptom5)
        vbox.addWidget(symptom6)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def rankupgroup(self):
        groupbox = QGroupBox('')

        rank1 = QPushButton('1')
        rank2 = QPushButton('2')
        rank3 = QPushButton('3')
        rank4 = QPushButton('4')
        rank5 = QPushButton('5')
        rank6 = QPushButton('6')
        rank7 = QPushButton('7')
        rank8 = QPushButton('8')


        vbox = QGridLayout()
        vbox.addWidget(rank1, 0, 0)
        vbox.addWidget(rank2, 0, 1)
        vbox.addWidget(rank3, 1, 0)
        vbox.addWidget(rank4, 1, 1)
        vbox.addWidget(rank5, 2, 0)
        vbox.addWidget(rank6, 2, 1)
        vbox.addWidget(rank7, 3, 0)
        vbox.addWidget(rank8, 3, 1)
        groupbox.setLayout(vbox)

        return groupbox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())