import requests
from PyQt5.uic.properties import QtGui
from PyQt5.QtGui import QIntValidator
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import mysql.connector
from flask import Flask
from flask import render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics


source = requests.get('https://kur.doviz.com/serbest-piyasa/amerikan-dolari')
soup = BeautifulSoup(source.text, 'html.parser')
basliklar = soup.findAll('div', attrs={'class':'data'})
for i in basliklar:
    print(i.text)

class ExchangeRate (QDialog):
    def __init__(self, parent=None):
        super(ExchangeRate,self).__init__(parent)
        self.horizontalGroupBox = QGroupBox("General Information")
        grid=QGridLayout()
        grid.setColumnStretch(1,10)
        grid.addWidget(QLabel("Ürün Kodu:"),0,0)
        grid.addWidget(QLabel("Maliyet:"),1,0)
        grid.addWidget(QLabel("Satış:"),2,0)
        grid.addWidget(QLabel("Dolar Kuru:"),3,0)
        grid.addWidget(QLabel("Sonuc:"), 4,0)
        grid.addWidget(QLabel("Sabit Kar:"), 5,0)
        grid.addWidget(QLabel("Ürün Kodu:"),6,0)
        grid.addWidget(QLabel("Dolar Kuru:"), 7,0)
        grid.addWidget(QLabel("Sonuc 2:"), 8,0)
        grid.addWidget(QLabel("Net Kar"), 9,0)
        grid.addWidget(QLabel(""), 10,0)
        self.urun = QtWidgets.QLineEdit(self)
        self.m = QtWidgets.QLineEdit(self)
        self.s = QtWidgets.QLineEdit(self)
        self.d = QtWidgets.QLineEdit(self)
        self.sonuc = QtWidgets.QLabel(self)
        self.kar = QtWidgets.QLabel(self)
        self.kod = QtWidgets.QLineEdit(self)
        self.dolarkuru = QtWidgets.QLineEdit(self)
        self.sonuc2 = QtWidgets.QLabel(self)
        self.netkar = QtWidgets.QLabel(self)
        grid.addWidget(self.urun, 0, 1)
        grid.addWidget(self.m, 1, 1)
        grid.addWidget(self.s, 2, 1)
        grid.addWidget(self.d, 3, 1)
        grid.addWidget(self.sonuc, 4, 1)
        grid.addWidget(self.kar, 5, 1)
        grid.addWidget(self.kod, 6, 1)
        grid.addWidget(self.dolarkuru, 7, 1)
        grid.addWidget(self.sonuc2, 8, 1)
        grid.addWidget(self.netkar, 9, 1)
        hesapla = QPushButton("Hesapla")
        hesapla.clicked.connect(self.kaydet)
        grid.addWidget(hesapla)
        self.setLayout(grid)
        self.setWindowTitle("Exchange Rate")

    def kaydet(self):
        urunkodu = int(self.urun.text())
        maliyet = int(self.m.text())
        satis = int(self.s.text())
        kur = float(self.d.text())
        kar = float(satis-maliyet)
        self.kar.setText(('%d'%kar))
        sonuc = float((satis - maliyet)*kur)
        self.sonuc.setText('%d'%sonuc)
        kod = int(self.kod.text())
        dolarkuru = float(self.dolarkuru.text())
        sonuc2 = float(kar * dolarkuru)
        self.sonuc2.setText('%d'%sonuc2)
        netkar = float(sonuc2-sonuc)
        self.netkar.setText('%d'%netkar)
        baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="exchange")
        isaretci=baglanti.cursor()
        isaretci.execute('''INSERT INTO rate (urunkodu, maliyet, satis, kur, sonuc, kar, kod, dolarkuru, sonuc2, netkar)  VALUES("%s","%s","%s", "%s", "%d", "%d","%s", "%s", "%d","%d")'''%(urunkodu, maliyet, satis, kur, sonuc, kar, kod, dolarkuru, sonuc2, netkar))
        baglanti.commit()
        baglanti.close()

numpy_array = np.array([6.05, 7.56, 7.00, 6.50, 6.70, 7.12, 7.40, 7.65, 8.00, 8.10, 8.12, 8.56])
print("1 yıllık Dolar Kuru Değerleri:")
print(numpy_array)
print("Dolar Kurunun Maximum Değeri:")
print(numpy_array.max())
print("Dolar Kurunun Minimum Değeri:")
print(numpy_array.min())
print("Yıllık Dolar Kuru Ortalaması:")
print(numpy_array.mean())
print("******************")

kur_listesi= {"aylar":["ocak","subat","mart","nisan","mayis","haziran","temmuz","agustos","eylul","ekim","kasim","aralik"],
                  "kur":[6.05, 7.56, 7.00, 6.50, 6.70, 7.12, 7.40, 7.65, 8.00, 8.10, 8.12, 8.56]}
dataframe = pd.DataFrame(kur_listesi)
print(dataframe)

plt.scatter(dataframe.aylar, dataframe.kur)
plt.title("Aylara Göre Kur Dağılımı")
plt.xlabel("Aylar")
plt.ylabel("Kurlar")
plt.show()


uyg=QApplication([])
pencere=ExchangeRate()
pencere.show()
uyg.exec_()

app = Flask(__name__)
#x_ekseni = ["ocak","subat","mart","nisan","mayis","haziran","temmuz","agustos","eylul","ekim","kasim","aralik"]
#y_ekseni = [6.05, 7.56, 7.00, 6.50, 6.70, 7.12, 7.40, 7.65, 8.00, 8.10, 8.12, 8.56]

@app.route("/")
def anaSayfa():
    source = requests.get('https://kur.doviz.com/serbest-piyasa/amerikan-dolari')
    soup = BeautifulSoup(source.text, 'html.parser')
    basliklar = soup.findAll('div', attrs={'class': 'data'})
    for i in basliklar:
        return(i.text)

#@app.route("/barchart")
#def barchart():
    #return render_template('bar_chart.html', title='Aylara göre kur oranı', max=10,labels=x_ekseni,values=y_ekseni)

@app.route("/hakkimizda")
def hakkimizda():
    return "Hakkımızda Sayfası"

if __name__=="__main__":
    app.run()

