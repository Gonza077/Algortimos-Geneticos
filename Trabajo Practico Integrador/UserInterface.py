# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\Users\User\Desktop\uiTPParquesEolicos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from Generacion import *
from Poblacion import *
from Cromosoma import *
from OperadoresGeneticos import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 209)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 10, 251, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 127))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.selectCrossover = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectCrossover.sizePolicy().hasHeightForWidth())
        self.selectCrossover.setSizePolicy(sizePolicy)
        self.selectCrossover.setObjectName("selectCrossover")
        self.selectCrossover.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.selectCrossover)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.selectMutacion = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectMutacion.sizePolicy().hasHeightForWidth())
        self.selectMutacion.setSizePolicy(sizePolicy)
        self.selectMutacion.setObjectName("selectMutacion")
        self.selectMutacion.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.selectMutacion)
        self.tamPoblacion = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.tamPoblacion.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tamPoblacion.sizePolicy().hasHeightForWidth())
        self.tamPoblacion.setSizePolicy(sizePolicy)
        self.tamPoblacion.setObjectName("tamPoblacion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tamPoblacion)
        self.selectSeleccion = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectSeleccion.sizePolicy().hasHeightForWidth())
        self.selectSeleccion.setSizePolicy(sizePolicy)
        self.selectSeleccion.setObjectName("selectSeleccion")
        self.selectSeleccion.addItem("")
        self.selectSeleccion.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.selectSeleccion)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 10, 221, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 201, 121))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.cantAerogeneradores = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.cantAerogeneradores.setObjectName("cantAerogeneradores")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cantAerogeneradores)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.velocidadViento = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.velocidadViento.setObjectName("velocidadViento")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.velocidadViento)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.coefRugosidad = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.coefRugosidad.setObjectName("coefRugosidad")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.coefRugosidad)
        self.tamCromosoma = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.tamCromosoma.setObjectName("tamCromosoma")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tamCromosoma)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(490, 10, 231, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 211, 121))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(5, 5, 5, 5)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.cantPoblaciones = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.cantPoblaciones.setObjectName("cantPoblaciones")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cantPoblaciones)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.probCrossover = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.probCrossover.setObjectName("probCrossover")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.probCrossover)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.probMutacion = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.probMutacion.setObjectName("probMutacion")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.probMutacion)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.checkBoxElitismo = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.checkBoxElitismo.setText("")
        self.checkBoxElitismo.setObjectName("checkBoxElitismo")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBoxElitismo)
        self.btnEjecutar = QtWidgets.QPushButton(Dialog)
        self.btnEjecutar.setGeometry(QtCore.QRect(450, 170, 151, 31))
        self.btnEjecutar.setObjectName("btnEjecutar")
        self.btnResetear = QtWidgets.QPushButton(Dialog)
        self.btnResetear.setGeometry(QtCore.QRect(620, 170, 101, 31))
        self.btnResetear.setObjectName("btnResetear")

        self.retranslateUi(Dialog)
        self.selectCrossover.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TPI - Parques Eolico"))
        self.groupBox_2.setTitle(_translate("Dialog", "Parametros de la Población"))
        self.label.setText(_translate("Dialog", "Tamaño de población"))
        self.label_3.setText(_translate("Dialog", "Tipo de selección"))
        self.label_4.setText(_translate("Dialog", "Tipo de crossover"))
        self.selectCrossover.setItemText(0, _translate("Dialog", "Por fila y columna"))
        self.label_12.setText(_translate("Dialog", "Tipo de mutación"))
        self.selectMutacion.setItemText(0, _translate("Dialog", "Al Azar"))
        self.tamPoblacion.setText(_translate("Dialog", "50"))
        self.selectSeleccion.setItemText(0, _translate("Dialog", "Ruleta"))
        self.selectSeleccion.setItemText(1, _translate("Dialog", "Torneo"))
        self.groupBox_3.setTitle(_translate("Dialog", "Parámetros del Cromosoma"))
        self.label_5.setText(_translate("Dialog", "Tamaño del cromosoma"))
        self.label_6.setText(_translate("Dialog", "Cantidad Generadores"))
        self.cantAerogeneradores.setText(_translate("Dialog", "25"))
        self.label_8.setText(_translate("Dialog", "Velocidad del viento"))
        self.velocidadViento.setText(_translate("Dialog", "25"))
        self.label_14.setText(_translate("Dialog", "Coeficiente de rugosidad"))
        self.coefRugosidad.setText(_translate("Dialog", "0.05"))
        self.tamCromosoma.setText(_translate("Dialog", "10"))
        self.groupBox_4.setTitle(_translate("Dialog", "Parametros del Algoritmo"))
        self.label_9.setText(_translate("Dialog", "Cantidad de Poblaciones"))
        self.cantPoblaciones.setText(_translate("Dialog", "200"))
        self.label_10.setText(_translate("Dialog", "Probabilidad de crossover"))
        self.probCrossover.setText(_translate("Dialog", "0.9"))
        self.label_11.setText(_translate("Dialog", "Probabilidad de mutación"))
        self.probMutacion.setText(_translate("Dialog", "0.05"))
        self.label_13.setText(_translate("Dialog", "Elitismo"))
        self.btnEjecutar.setText(_translate("Dialog", "Correr Algoritmo Genético"))
        self.btnResetear.setText(_translate("Dialog", "Resetear"))

        #Conexion del metodo con el boton
        self.btnEjecutar.clicked.connect(self.ejecutarAlgoritmo)

    def ejecutarAlgoritmo(self):

        generaciones=[]
        CantPoblaciones = [int(self.cantPoblaciones.text())]
        #Parametros del Parque 
        Cromosoma.tCromo = int(self.tamCromosoma.text())
        Cromosoma.CantAerogeneradores=int(self.cantAerogeneradores.text())
        Cromosoma.VelocidadViento= int(self.velocidadViento.text()) #Velocidad del viento
        Cromosoma.TamañoCelda = 180
        Cromosoma.CoeficienteRugosidad = float(self.coefRugosidad.text())
        #Parametros de la Poblacion
        Poblacion.tPobla = int(self.tamPoblacion.text()) #Cantidad de cromosomas x Poblacion
        probCrossover = float(self.probCrossover.text())
        probMutacion = float(self.probMutacion.text())       

        if self.selectSeleccion.currentIndex() == 0:
            Poblacion.tipoSeleccion=Ruleta()
        elif self.selectSeleccion.currentIndex() == 1:
            Poblacion.tipoSeleccion=Torneo()

        print(self.selectCrossover.currentIndex())
        if self.selectCrossover.currentIndex() == 0:
            Poblacion.tipoCrossover=CrossOverUnPunto(probCrossover)

        if self.selectMutacion.currentIndex() == 0:
            Poblacion.tipoMutacion=MutacionInvertida(probMutacion)

        #CheckBox Elitismo
        Poblacion.elitismo=self.checkBoxElitismo.isChecked()

        for x in CantPoblaciones:
            generacion=Generacion()
            for _ in range(x):        
                generacion.creoPoblacion()
            Poblacion.reseteoIDPoblacion() #Metodo de clase que vuelve el ID a 1
            generaciones.append(generacion)

        #Se crea una archivo XLSX y se elimina la primer pagina
        wb = opyxl.Workbook() 
        wb.remove(wb.active) 
        print("\n")
        for generacion in generaciones:
            generacion.datosGeneracion(wb)
            print("\n")