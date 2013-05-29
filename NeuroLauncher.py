#!/usr/bin/python
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
aBestellen=str("https://10.253.53.200/einstieg.php")#experimentel

SIZE=int(150)
#Fenster
Main=tk.Tk()
Main.title("NeuroLauncher von Florian Becker")

frame0=tk.Frame(Main, bg="#BEBEBE")
frame0.pack(side="top")

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

#def pdf():
 #  subprocess.Popen('finder "/USERS"')

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
                           ("Informationen zum NeuroLauncher", "Dieses Programm wurde von Florian Becker geschrieben. Bei Fragen und Anregungen bitte per E-Mail melden an: S1l3nzCodes@googlemail.com Sourcecode: https://github.com/S1l3nzCodes")

#Farben
schrift="#FFA54F"
hintergrund="#27408B"
groesse=1

l1=tk.Label(frame0, text="Neuroradiologie UKSH - Campus Kiel", font="courier 16 italic", height=1)
l1.pack()

Intranet=tk.Button(frame1,text=" Intranet ", command=intranet, fg=schrift, bg=hintergrund, bd=2, width=groesse)
Intranet.pack(ipadx=SIZE, ipady=SIZE)

Website=tk.Button(frame1, text="Homepage", command=website, fg=schrift, bg=hintergrund, bd=2, width=groesse)
Website.pack(ipadx=SIZE, ipady=SIZE)

Logbuch=tk.Button(frame2, text="Logbuch", command=transport, fg=schrift, bg=hintergrund, bd=2, width=groesse)
Logbuch.pack(ipadx=SIZE, ipady=SIZE)

OPPlan=tk.Button(frame2, text="OP-Plan", command=op, fg=schrift, bg=hintergrund, bd=2, width=groesse)
OPPlan.pack(ipadx=SIZE, ipady=SIZE)

Webmail=tk.Button(frame1, text="Email @uksh", command=mail, fg=schrift, bg=hintergrund, bd=2, width=groesse)
Webmail.pack(ipadx=SIZE, ipady=SIZE)

Bestellen=tk.Button(frame2, text="Bestellen", command=bestellen, fg=schrift, bg=hintergrund, bd=2, width=groesse)
Bestellen.pack(ipadx=SIZE, ipady=SIZE)

Essen=tk.Button(frame3, text="Speiseplan", command=essen, fg=schrift, bg=hintergrund, bd=2, width=groesse)
Essen.pack(ipadx=SIZE, ipady=SIZE)

News=tk.Button(frame3, text="News", command=news, fg=schrift, bg=hintergrund, bd=2, width=groesse)
News.pack(ipadx=SIZE, ipady=SIZE)

PDF=tk.Button(frame3, text="PDF's", command=write, fg=schrift, bg=hintergrund, bd=2, width=groesse)
PDF.pack(ipadx=SIZE, ipady=SIZE)

menue=tk.Menu(Main)
mProg=tk.Menu(menue)
mProg.add_command(label="Beenden",command=ende)
mAbout=tk.Menu(menue)
mAbout.add_command(label="Über dieses Programm",command=ueber)
menue.add_cascade(label="Programm", menu=mProg)
menue.add_cascade(label="Über", menu=mAbout)
Main["menu"]=menue

Main.mainloop()
