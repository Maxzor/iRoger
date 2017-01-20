# -*- coding: utf-8 -*-
import os, sys, os.path
import time, datetime
from scheduler import scheduler
import UART
from datetime import datetime
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from groupbox import Ui_GroupBox
import picamera

#classe principale, fenêtre iRoger
class iRogerApplication(QGroupBox):
	def __init__(self, parent=None):
		super (iRogerApplication, self).__init__(parent)
                self.get_thread = scheduler()
                self.get_thread.start()
		self.createWidgets()
		

        #Mise en place des éléments de la fenêtre
	def createWidgets(self):
		self.ui = Ui_GroupBox()
		self.ui.setupUi(self)
                w = self.ui.tabWidget
                w.setAutoFillBackground(True)
                p = QPalette()
                gradient = QLinearGradient(0, 0, 0, 400)
                gradient.setColorAt(0.0, QColor(251, 254, 230))
                gradient.setColorAt(1.0, QColor(187, 240, 178))
                p.setBrush(QPalette.Window, QBrush(gradient))
                w.setPalette(p)
		#zone 'historique'
                with open("fichier.txt") as f:
                        text = f.read()
                self.ui.textBrowser.setPlainText(text)		
		#mise en place base SQlite
		self.db = QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName('differe.db')
		self.db.open()
        	#définition du modèle de la table
		self.model = QSqlTableModel(self)
		self.model.setTable("differe")
		#stratégie d'édition : instantanée
                self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
                self.model.setHeaderData(0, Qt.Horizontal, "Heure")
                self.model.setHeaderData(1, Qt.Horizontal, "Ration")
                self.model.select()
                self.ui.tableView_2.setModel(self.model)
                #définir la photo
                photo = QPixmap(os.getcwd() + "/photo_iRoger.jpg")
                photo = photo.scaledToHeight(171)
                self.ui.label.setPixmap(photo)                

        #fonctions BDD
        def addrow(self):
                ret = self.model.insertRows(self.model.rowCount(),1)

        def delrow(self):
                self.model.removeRow(self.ui.tableView_2.currentIndex().row())

        def findrow(i):
                delrow = i.row()

        #fonction rotation du servo (module UART)
        def bouffailledesuite(self):
                #déclencher la distribution
                duration = self.ui.spinBox.value()
                action=UART.deal(duration)
                self.alim_histo(duration)

        #alimenter l'historique
        def alim_histo(self, duration):
                duration = duration
                maintenant=datetime.now()
                datastr = str(duration)
                fichier = open("fichier.txt","r")
                total = str(maintenant.day) + "/" + \
                        str(maintenant.month) + " " + str(maintenant.hour) \
                        + ":" + str(maintenant.minute) + \
                        "  " + datastr + "s" + "\n" + fichier.read()
                fichier.close()
                fichier =open("fichier.txt","w")
                fichier.write(total)
                fichier.close
                #rafraîchir l'historique
                self.ui.textBrowser.setText(total)
                QtCore.QCoreApplication.processEvents()

        #prise d'une photo
        def actu_photo(self):
                camera = picamera.PiCamera()
                photo = camera.capture("photo_iRoger.jpg")
                photo_saved = os.path.join("/home/pi/Desktop","photo_iRoger.jpg")
                camera.close()
                pxmap = QPixmap(os.getcwd() + "/photo_iRoger.jpg")
                pxmap = pxmap.scaledToHeight(171)
                self.ui.label.setPixmap(pxmap)
                QtCore.QCoreApplication.processEvents()

#foction principale
if __name__== "__main__":
	app=QApplication(sys.argv)
	myapp=iRogerApplication()

        delrow = -1

        #prog événementielle classique
        QObject.connect(myapp.ui.tableView_2, SIGNAL("clicked()"), myapp.findrow)
        QObject.connect(myapp.ui.pushButton, SIGNAL("clicked()"), myapp.bouffailledesuite)
        QObject.connect(myapp.ui.pushButton_2, SIGNAL("clicked()"), myapp.addrow)
        QObject.connect(myapp.ui.pushButton_3, SIGNAL("clicked()"), myapp.delrow)
        QObject.connect(myapp.ui.pushButton_4, SIGNAL("clicked()"), myapp.actu_photo)
        #signal/slot pour historique
        myapp.connect(myapp.get_thread, SIGNAL('alim_histo(QString)'), myapp.alim_histo)
	
	myapp.show()
	sys.exit(app.exec_())
