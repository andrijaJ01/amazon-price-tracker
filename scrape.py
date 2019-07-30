import bs4 as bs 
import sys 
import schedule
import time 
import urllib.request 
from PyQt5.QtWebEngineWidgets import QWebEnginePage 
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtCore import QUrl
import smtplib
from email.message import EmailMessage
import socket
socket.setdefaulttimeout(120)
  
import winsound 
frequency = 2500  
duration = 1000

  
class Page(QWebEnginePage): 
  
    def __init__(self, url): 
        self.app = QApplication(sys.argv) 
        QWebEnginePage.__init__(self) 
        self.html = '' 
        self.loadFinished.connect(self._on_load_finished) 
        self.load(QUrl(url)) 
        self.app.exec_() 
  
    def _on_load_finished(self): 
        self.html = self.toHtml(self.Callable) 
        print('Load finished') 
  
    def Callable(self, html_str): 
        self.html = html_str 
        self.app.quit() 
  
def exact_url(url): 
    index = url.find("B0") 
    index = index + 10
    current_url = "" 
    current_url = url[:index] 
    return current_url 

def send_mail():
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("andrijajovanovic001@gmail.com", "mojasoba001")
	server.sendmail(
	  "andrijajovanovic001@gmail.com", 
	  "andrijaaki001@gmail.com", 
	  "check the 'Mini Smartphone iLight X, World's Smallest XS Android Mobile Phone 4G LTE, Super Small Tiny Micro HD 3 Touch Screen. Global Unlocked Great for Kids. 2GB RAM / 16GB ROM. Tiny iPhone X Look Alike' on amazon ")
	server.quit()

	print ("mail has been sent")
    
  
def mainprogram(): 
    url = "https://www.amazon.com/dp/B07QL37B7D/ref=sspa_dk_detail_8?psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTERaQkM5QVFQVzZSJmVuY3J5cHRlZElkPUExMDM3OTIxMzZFTUpQOFFXU1BEViZlbmNyeXB0ZWRBZElkPUEwNjY0MjA0MU1CNFE5WVA1QkJUVCZ3aWRnZXROYW1lPXNwX2RldGFpbDImYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
    exacturl = exact_url(url) 
    page = Page(exacturl) 
    soup = bs.BeautifulSoup(page.html, 'html.parser') 
    js_test = soup.find('span', id ='priceblock_ourprice') 
    if js_test is None: 
        js_test = soup.find('span', id ='priceblock_dealprice')         
    str = "" 
    for line in js_test.stripped_strings : 
        str = line 
  
     
    str = str.replace(", ", "")
    newstr= str.replace("$", "")
    current_price = int(float(newstr)) 
    your_price = 600
    if current_price < your_price : 
        print("Price decreased book now")
        winsound.Beep(frequency, duration)
        send_mail()
    else: 
        print("Price is high please wait for the best deal")
        winsound.Beep(frequency, duration)
    
              
def job(): 
    print("Tracking....")     
    mainprogram()
   
    
  


  
while True: 
    job()
    time.sleep(60)



