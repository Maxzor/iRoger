from PyQt4 import QtSql, QtGui

def createDB():
   db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('differe.db')
	
   if not db.open():
      QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
         QtGui.qApp.tr("Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read "
            "the Qt SQL driver documentation for information "
            "how to build it.\n\n" "Click Cancel to exit."),
         QtGui.QMessageBox.Cancel)
			
      return False
		
   query = QtSql.QSqlQuery()
	
   query.exec_("create table differe(Heure text primary key, "
      "Ration int)")
		
   query.exec_("insert into differe values('11:01', 3)")
   query.exec_("insert into differe values('19:00', 5)")
   return True
	
if __name__ == '__main__':
   import sys
	
   app = QtGui.QApplication(sys.argv)
   createDB()
