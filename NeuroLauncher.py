#!C:/Python/python.exe
# -*- coding: utf-8 -*-
import Tkinter as tk
import tkMessageBox
import webbrowser
import os
import subprocess

#Adressen:
aLogbuch=str("http://10.140.223.201/logbuch/login.php?host=radpc810")
aImpax=str("")
aIntranet=str("http://10.253.53.23/intranet.html")
aOP=str("http://172.24.181.10/OP-Plan/2013/Kalender/PerpetualCalendar21.htm")
aWebmail=str("https://webmail.uksh.de/CookieAuth.dll?GetLogon?curl=Z2Fowa&reason=0&formdir=1")
aSPX=str("http://10.253.53.224/webaspx/")
aBestellen=str("https://10.253.53.200/einstieg.php")
aEssen=str("http://10.253.53.23/Kiel_Übersicht_Speisepläne/etc.html")#Expreri

#Bestelliste erzeugen:
try:
    Bestelliste=open("Bestellwunsch.txt", "r")
except:
    Bestelliste=open("Bestellwunsch.txt", "w")




SIZE=int(165)
#Fenster
Main=tk.Tk()
Main.title("NeuroStarter von Florian Becker")

frame0=tk.Frame(Main, bg="#BEBEBE")
frame0.pack(side="top")
frame4=tk.Frame(Main, bg="#FFA54F", bd=5)
frame4.pack(side="bottom")


frame1=tk.Frame(Main, bg="#FFA54F", bd=5)
frame1.pack(side="left")

frame2=tk.Frame(Main, bg="#FFA54F", bd=5)
frame2.pack(side="left")

frame3=tk.Frame(Main, bg="#FFA54F", bd=5)
frame3.pack(side="left")


def transport():
    webbrowser.open_new(aLogbuch)

def mail():
    webbrowser.open_new(aWebmail)

def op():
    webbrowser.open_new(aOP)

def bestellen():
    webbrowser.open_new(aBestellen)

def intranet():
    webbrowser.open_new(aIntranet)

def website():
    webbrowser.open_new(aWebsite)

def essen():
    webbrowser.open_new(aEssen)

def news():
    webbrowser.open_new(aNews)

def pdf():
   subprocess.Popen('explorer')

def error():
    print ("Error")


def write():
    Daten=open("Wunschliste.txt","w")
    Daten.write("Testzeuch")
    Daten.close

def ende():
    Main.destroy()

def ueber():
    tkMessageBox.showinfo \
                           ("Informationen zum NeuroStarter", "Dieses kleine Programm wurde von Florian Becker geschrieben. Bei Fragen und Anregungen bitte per E-Mail melden an: \n S1l3nzCodes@googlemail.com \n Sourcecode: https://github.com/S1l3nzCodes")

def send():
    Wunsch=Bestellwunsch.get()
    Daten=open("Bestellwunsch.txt", "r")
    Inhalt=Daten.read()
    Daten.close
    Daten=open("Bestellwunsch.txt", "w")
    Neu=str(Inhalt + "\n" + Wunsch)
    Daten.write(Neu)
    Daten.close
    Bestellwunsch.delete(0, 99)
    tkMessageBox.showinfo \
                          ("Info", "Dein Bestellwunsch wurde eingetragen")
def show():
    Daten=open("Bestellwunsch.txt", "r")
    Wunsch=Daten.read()
    tkMessageBox.showinfo \
                          ("Bestellwunsch.txt", "Folgende Materialien wurde gewünscht:  \n" + Wunsch)
#Farben
schrift="#FFA54F"
schriftart="helvetiva 18"
hintergrund="#27408B"
groesse=1

#l1=tk.Label(frame0, text="Neuroradiologie UKSH - Campus Kiel", font="courier 20", height=1)
#l1.pack()

Intranet=tk.Button(frame1,text=" Intranet ", command=intranet, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
Intranet.pack(ipadx=SIZE, ipady=SIZE)

Website=tk.Button(frame1, text="Homepage", command=website, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
Website.pack(ipadx=SIZE, ipady=SIZE)

Logbuch=tk.Button(frame2, text="Logbuch", command=transport, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
Logbuch.pack(ipadx=SIZE, ipady=SIZE)

OPPlan=tk.Button(frame2, text="OP-Plan", command=op, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
OPPlan.pack(ipadx=SIZE, ipady=SIZE)

Webmail=tk.Button(frame1, text="Email @uksh", command=mail, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
Webmail.pack(ipadx=SIZE, ipady=SIZE)

Bestellen=tk.Button(frame2, text="Bestellen", command=bestellen, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
Bestellen.pack(ipadx=SIZE, ipady=SIZE)

Essen=tk.Button(frame3, text="Speiseplan", command=essen, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
Essen.pack(ipadx=SIZE, ipady=SIZE)

News=tk.Button(frame3, text="News", command=news, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
News.pack(ipadx=SIZE, ipady=SIZE)

PDF=tk.Button(frame3, text="PDF's", command=pdf, fg=schrift, bg=hintergrund, bd=2, width=groesse, font=schriftart)
PDF.pack(ipadx=SIZE, ipady=SIZE)

Bestellwunsch=tk.Entry(frame4, width=45, font="helvetica 16")
Bestellwunsch.pack(side="left", ipady=10)

Send=tk.Button(frame4, text="Bestellwunsch abschicken", command=send, fg=schrift, font=schriftart, bg=hintergrund)
Send.pack(side="left")

Read=tk.Button(frame4, text="Wünsche Anzeigen", command=show,fg=schrift, font=schriftart, bg=hintergrund)
Read.pack(side="left")


menue=tk.Menu(Main)
mProg=tk.Menu(menue)
mProg.add_command(label="Beenden",command=ende)
mAbout=tk.Menu(menue)
mAbout.add_command(label="Über dieses Programm",command=ueber)
menue.add_cascade(label="Programm", menu=mProg)
menue.add_cascade(label="Über", menu=mAbout)
Main["menu"]=menue

Main.mainloop()
