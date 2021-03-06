from PyQt5.QtWidgets import *
from MainPage import Ui_Ana




class Launch(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Ana()
        self.ui.setupUi(self)


        #ButtonWorks
        self.ui.btnExt.clicked.connect(self.btnExtClicked)
        self.ui.btnStart.clicked.connect(self.EngineStart)

        self.ui.lblPow1.setVisible(False)
        self.ui.lblPow2.setVisible(False)
        self.ui.lblPow3.setVisible(False)
        self.ui.lblPow4.setVisible(False)

        self.ui.sliderPower.valueChanged.connect(self.ValueChanged)

    def ValueChanged(self):
        a = self.ui.sliderPower.value()

        if (a > 100):
            self.ui.lblError.setText("ENGINE  \nOVERLIMIT !! ")
            print("%100 limit + !! OVERLIMIT !! ")
        elif (a >= 100):
            self.ui.lblPow1.setVisible(True)
            self.ui.lblPow2.setVisible(True)
            self.ui.lblPow3.setVisible(True)
            self.ui.lblPow4.setVisible(True)
            self.ui.lblError.setText("ON POWER LIMIT ")
            if (a<99):
                self.ui.lblPow4.setVisible(False)

        elif (a >= 75):
            self.ui.lblPow1.setVisible(True)
            self.ui.lblPow2.setVisible(True)
            self.ui.lblPow3.setVisible(True)
            print("ENGINE POWER: ", a)
            if(a<74):
                self.ui.lblPow3.setVisible(False)


        elif (a >= 45):

            self.ui.lblPow1.setVisible(True)
            self.ui.lblPow2.setVisible(True)
            print("ENGINE POWER: ", a)
            if (a < 44):
                self.ui.lblPow2.setVisible(False)


        elif (a >= 15):
            self.ui.lblPow1.setVisible(True)
            print("ENGINE POWER: ", a)
            if (a < 14):
                self.ui.lblPow1.setVisible(False)


        elif (a <= 5):
            self.ui.lblPow.setText("UP SLIDE")
            print("ENGINE POWER: ", a)


    def EngineStart(self):
        E="ERROR: "

        chckElectrical= self.ui.chckElectric.isChecked()
        chckEnginePow = self.ui.chckEngine.isChecked()
        chckFuel =self.ui.chckFuel.isChecked()
        chckTires = self.ui.chckTires.isChecked()
        chckRadio= self.ui.chckRadio.isChecked()

        print("Electrical Systems=  ",chckElectrical)
        print("Engine Systems=  ",chckEnginePow)
        print("Fuel Systems=  ",chckFuel)
        print("Radio Systems=  ",chckRadio)
        print("Tire Systems=  ",chckTires)





        if(chckTires==True and chckFuel==True and chckRadio==True and chckFuel==True and chckElectrical==True and chckEnginePow==True):
            print("Succes")

            self.ui.lblError.setText("Engine Running")


        elif(chckTires==False):
            print(E,"Tires Systems")
            self.ui.lblError.setText(E+"Tires Systems")

        elif(chckRadio==False):
            print(E,"Radio Systems")
            self.ui.lblError.setText(E+"Radio Systems")
        elif(chckFuel==False):
            print(E,"Fuel Systems")
            self.ui.lblError.setText(E+"Fuel Systems")
        elif(chckEnginePow==False):
            print(E,"Engine Systems")
            self.ui.lblError.setText(E+"Engine Systems")
        elif(chckElectrical==False):
            print(E,"Electrical Systems")
            self.ui.lblError.setText(E+"Electrical Systems")




    def btnExtClicked(self):
        print("????k??l??yor....")
        self.ui.lblPow.setText("ENG OFF")
        quit()




app = QApplication([])
window = Launch()
window.show()
app.exec()