import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

class character_sheet(QMainWindow):

    def calcModAttributes(self, value):
        mod = {"1": "-5", "2": "-4", "3": "-4", "4": "-3", "5": "-3", "6": "-2", "7": "-2", "8": "-1", "9": "-1", "10": "0", "11": "0", "12": "1", "13": "1", "14": "2", "15": "2",
            "16": "3", "17": "3", "18": "4", "19": "4", "20": "5", "21": "5", "22": "6", "23": "6", "24": "7", "25": "7", "26": "8", "27": "8", "28": "9", "29": "9", "30": "10"}
        if value is not None:
            return mod.get(value, "")
        return ""


    def calcAttributes(self):
        strValue = self.strVal.toPlainText()
        self.strMod.setText(self.calcModAttributes(strValue))

        dexValue = self.dexVal.toPlainText()
        self.dexMod.setText(self.calcModAttributes(dexValue))

        conValue = self.conVal.toPlainText()
        self.conMod.setText(self.calcModAttributes(conValue))

        intValue = self.intVal.toPlainText()
        self.intMod.setText(self.calcModAttributes(intValue))

        wisValue = self.wisVal.toPlainText()
        self.wisMod.setText(self.calcModAttributes(wisValue))

        chaValue = self.chaVal.toPlainText()
        self.chaMod.setText(self.calcModAttributes(chaValue))


    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)
        self.butCalcAtr.clicked.connect(self.calcAttributes)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = character_sheet()
    GUI.show()
    sys.exit(app.exec_())