#Importing files for GUI

from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter.ttk import Progressbar

#Importing files for encryption

import os
import getpass
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

#Importing for timer

import time

#Global variable declaration

passb='a'
lbl1='a'
lbl2='a'
passw='a'

#Functions

def browse_button1():
    global folder_path1
    inputDirectory = filedialog.askdirectory()
    folder_path1.set(inputDirectory)
	
def browse_button2():
    global folder_path2
    outputDirectory = filedialog.askdirectory()
    folder_path2.set(outputDirectory)

def callAbout():
	tkinter.messagebox.showinfo("USB Encryptor Tool","App Created by: Ashish Basantani")

"""def ii():
	print("inside")
	global passb
	global lbl1
	global lbl2
	lbl1=os.path.normcase(lbl1['text'])
	print(lbl1)
	passs=passb.get()
	print(passs)"""

"""def Progress1():
	global passw
	p=Tk()
	p.title("USB Encryptor Tool-Processing")
	w1=400
	w2=100
	x=int(p.winfo_screenwidth()/2 - w1/2)
	y=int(p.winfo_screenheight()/2 - w2/2)
	p.geometry("%dx%d+%d+%d" % (w1,w2,x,y))
	p.resizable(0,0)
	progress=Progressbar(p,orient=HORIZONTAL,length=100,mode='determinate')
	def pro():
		i=1
		while (i<=100):
			progress['value']=i
			p.update_idletasks()
			time.sleep(0.1)
			i=i+1
		p.quit()
	progress.pack()
	pro()
	passw.quit()
	mainloop()"""

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def encrypt(filename):
	global passb
	global lbl2
	key=getKey(passb.get())
	chunksize = 64 * 1024
	outputFile = lbl2 + "/" + filename
	filename = lbl1 + "/" + filename 
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)

			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += b' ' * (16 - (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))
				
def decrypt(filename):
	global passb
	global lbl2
	key=getKey(passb.get())
	chunksize = 64 * 1024
	#outputFile = lbl2 + "/" + filename[11:]
	outputFile = lbl2 + "/" + filename
	filename = lbl1 + "/" + filename 

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)

def fileAccess1():
	global lbl1
	global lbl2
	global passw
	lbl1=os.path.normcase(lbl1['text'])
	lbl2=os.path.normcase(lbl2['text'])
	for root, dirs, files in os.walk(lbl1):  
		for filename in files:
			encrypt(filename)
	passw.quit()
def fileAccess2():
	global lbl1
	global lbl2
	global passw
	lbl1=os.path.normcase(lbl1['text'])
	lbl2=os.path.normcase(lbl2['text'])
	for root, dirs, files in os.walk(lbl1):  
		for filename in files:
			decrypt(filename)
	passw.quit()

def inputPass1():
	global passw
	passw=Tk()
	passw.title("USB Encryptor Tool-Enter Password")
	w1=400
	w2=100
	x=int(passw.winfo_screenwidth()/2 - w1/2)
	y=int(passw.winfo_screenheight()/2 - w2/2)
	passw.geometry("%dx%d+%d+%d" % (w1,w2,x,y))
	passw.resizable(0,0)
	label1=Label(passw, text="Enter Password: ", font=("Arial",13))
	label1.place(x=10,y=12)
	global passb
	passb=Entry(passw,show="*")
	passb.place(x=150,y=12)
	ok=Button(passw,text="Ok", command=fileAccess1)
	ok.place(x=190,y=55)
	passw.mainloop()
	
def inputPass2():
	global passw
	passw=Tk()
	passw.title("USB Encryptor Tool-Enter Password")
	w1=400
	w2=100
	x=int(passw.winfo_screenwidth()/2 - w1/2)
	y=int(passw.winfo_screenheight()/2 - w2/2)
	passw.geometry("%dx%d+%d+%d" % (w1,w2,x,y))
	passw.resizable(0,0)
	label1=Label(passw, text="Enter Password: ", font=("Arial",13))
	label1.place(x=10,y=12)
	global passb
	passb=Entry(passw,show="*")
	passb.place(x=150,y=12)
	ok=Button(passw,text="Ok", command=fileAccess2)
	ok.place(x=190,y=55)
	passw.mainloop()
	



#Design of Main Window

MainWindow=Tk()
MainWindow.title("USB Encryptor Tool")
w1=900
w2=400
x=int(MainWindow.winfo_screenwidth()/2 - w1/2)
y=int(MainWindow.winfo_screenheight()/2 - w2/2)
MainWindow.geometry("%dx%d+%d+%d" % (w1,w2,x,y))
MainWindow.resizable(0,0)
MainWindow.iconbitmap('as.ico')

#Main Menu

menu=Menu(MainWindow)
MainWindow.config(menu=menu)
menu.add_command(label="About", command=callAbout)

#Main Window widgets

tempFrame=Frame(MainWindow,height=50, width=300)
tempFrame.pack()
frame=Frame(MainWindow,bg="lightgray",bd='5', height=250, width=700)
frame.pack()
label1=Label(MainWindow, text="Input Directory: ", bg="lightgray", font=("Arial",13))
label2=Label(MainWindow, text="Output Directory: ",bg="lightgray", font=("Arial",13))
label1.place(x=110,y=70)
label2.place(x=110,y=150)	

folder_path1 = StringVar()
lbl1 = Label(MainWindow,bg="lightgray",textvariable=folder_path1)
lbl1.place(x=350,y=70)
Browse1 = Button(MainWindow, text="Browse", command=browse_button1)
Browse1.place(x=250,y=70)

folder_path2 = StringVar()
lbl2 = Label(MainWindow,bg="lightgray",textvariable=folder_path2)
lbl2.place(x=350,y=150)
Browse2 = Button(MainWindow, text="Browse", command=browse_button2)
Browse2.place(x=250,y=150) 


encryptButton=Button(MainWindow, text="Encrypt", command=inputPass1)
decryptButton=Button(MainWindow, text="Decrypt", command=inputPass2)
encryptButton.place(x=300,y=250)
decryptButton.place(x=450,y=250)

#Running Application

MainWindow.mainloop()