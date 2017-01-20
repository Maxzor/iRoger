import sys, time
import sqlite3 as db
from PyQt4.QtCore import QThread, SIGNAL
import schedule
import UART

class scheduler(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.startScheduler()

    def __del__(self):
        self.wait()

    def startScheduler(self):
        conn=db.connect('differe.db')
        conn.row_factory = lambda cursor, row: row[0]
        c=conn.cursor()
        h=c.execute('SELECT Heure from differe').fetchall()
        r=c.execute('SELECT Ration from differe').fetchall()

        for line in range(len(h)):
            #programmation distribution
            schedule.every().day.at(h[line]).do(UART.deal,r[line])
            #remonter info distributions pour historique
            schedule.every().day.at(h[line]).do(self.signal_histo, r[line])

    def signal_histo(self, duration):
        duration = str(duration)
        self.emit(SIGNAL('alim_histo(QString)'), duration)

    def run(self):
        while True:
            schedule.run_pending()
            #actualisation du plannificateur toutes les minutes
            self.sleep(60)
