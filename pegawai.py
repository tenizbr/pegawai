import sys
from PyQt4 import Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import QDate, SIGNAL
from PyQt4 import QtGui

class FormUtama(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.initUI()
		self.setWindowTitle('Pegawai')
		self.resize(550,550)
		self.labelNama=QLabel(self)
		self.labelAlamat=QLabel(self)
		self.labelTglLahir=QLabel("tgl_lahir",self)
		self.labelJenis=QLabel(self)
		self.labelNama=QLabel(self)
		self.editNama=QLineEdit(self)
		self.editAlamat=QTextEdit(self)
		self.editTglLahir=QDateEdit(self)
		self.editJenis=QComboBox(self)
		self.buttonSimpan=QPushButton(self)
		self.listPegawai=QTableWidget(self)
		self.labelNama.setText('Nama')
		self.labelAlamat.setText('Alamat')
		self.labelJenis.setText('Jenis_Kelamin')
		#self.editTglLahir.setDisplayFormat('dd-MM-yyyy')
		self.editTglLahir.setDisplayFormat('dd-MM-yyyy')
		self.editTglLahir.setDate(QDate(2010,10,23))
		self.editJenis.addItems(['Pria','Wanita'])
		self.buttonSimpan.setText('Simpan')
		self.listPegawai.setColumnCount(5)
		self.listPegawai.setHorizontalHeaderLabels(['ID','Nama','Alamat','Tgl_Lahir','Kelamin'])
		self.listPegawai.setColumnWidth(0,20)
		self.listPegawai.setColumnWidth(1,150)
		self.editAlamat.resize(200,100)
		self.listPegawai.resize(500,200)
		self.labelNama.move(10,10)
		self.labelAlamat.move(10,40)
		self.labelTglLahir.move(10,140)
		self.labelJenis.move(10,170)
		self.editNama.setGeometry(100,10,200,30)
		self.editAlamat.move(100,40)
		self.editTglLahir.move(100,140)
		self.editJenis.move(199,170)
		self.buttonSimpan.move(100,200)
		self.listPegawai.move(10,300)
		self.connect(self.buttonSimpan,SIGNAL('clicked()'),self.simpan)
		
	def closeEvent(self,event):
		s='' 
		for row in range(self.listPegawai.rowCount()):
			r=''
			for col in range(self.listPegawai.columnCount()):
				v=str(self.listPegawai.item(row,col).text())
				r +=v+','
			s+=r.strip(',')+'\n'
		f=open('pegawai.csv','w')
		f.write(s)
		f.close()
		QMainWindow.closeEvent(self,event)
	
	def simpan(self):
		row=self.listPegawai.rowCount()
		pid=row+1
		self.listPegawai.setRowCount(pid)
		self.listPegawai.setItem(row,0,QTableWidgetItem(str(pid)))
		self.listPegawai.setItem(row,1,QTableWidgetItem(self.editNama.text()))
		self.listPegawai.setItem(row,2,QTableWidgetItem(self.editAlamat.toPlainText()))
		self.listPegawai.setItem(row,3,QTableWidgetItem(self.editTglLahir.text()))
		self.listPegawai.setItem(row,4,QTableWidgetItem(self.editJenis.currentText()))
		self.editNama.clear()
		self.editAlamat.clear()
		self.editJenis.setCurrentIndex(0)
		self.editNama.setFocus()
	
app=Qt.QApplication(sys.argv)
fm= FormUtama()
fm.show()
app.exec_()
