import math
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('form.ui', self)

        self.setWindowTitle('Сложные табличные вычисления в Python')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.img_Lbl.setPixmap(QPixmap('images/task.png'))
        self.img_Lbl.setScaledContents(True)

        self.rand_Btn.clicked.connect(self.fill_random_numbers)
        self.solve_Btn.clicked.connect(self.solve)
        self.clear_Btn.clicked.connect(self.clear)
        self.exit_Btn.clicked.connect(self.exit)

    def fill_random_numbers(self):
        i = 0
        while i < self.tableWidget.rowCount():
            random_num = randint(0, 20)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random_num)))
            i += 1

    def clear(self):
        self.tableWidget.clearContents()

    def exit(self):
        self.close()

    def solve(self):
        if validation_of_data(self.tableWidget):
            i = 0
            j = 1
            proiz = 1
            summa = 0


            while i < self.tableWidget.rowCount():
                item = int(self.tableWidget.item(i, 0).text())
                summa += item
                numerator = ((math.cos(item ** 2)) / (math.factorial(i) + math.sin(item) ** 2)) ** (
                            1.0 / 2) * proiz
                denominator = summa
                value = numerator / denominator

                try:
                    answer = format(value,".6f")



                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(answer)))
                except Exception:
                    self.tableWidget.setItem(i, j, QTableWidgetItem('none'))

                i += 1

            #self.label_error.setText('')
        else:
            self.label_error.setText('Введены некорректные данные!')

def validation_of_data(table_widget):
    i = 0
    while i < table_widget.rowCount():
        try:
            float(table_widget.item(i, 0).text())
            i += 1
        except Exception:
            return False
    return True


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()