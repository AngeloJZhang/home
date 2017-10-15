#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from threading import Timer



class AddTimer(ttk.Frame): 
	def __init__(self,master=None):
	#create the window
		ttk.Frame.__init__(self,master=None)
		self.timers = {}
		self.nameHolder = tk.StringVar()
		self.timeHolder, self.checkBtnValue = tk.IntVar(),tk.IntVar()
		self.grid()
		self.createWidgets()
		return
	def createWidgets(self):
	#create starting widgets ( button)
		self.addbutton = ttk.Button(self,text="+", command=self.timerInfoInput)
		self.calendarBox = ttk.Checkbutton(self,variable=self.checkBtnValue,command=self.greyOut,text="Add to G Calendar")
		self.addbutton.grid(row=5,column=0, padx="15px",pady="25px")
		self.calendarBox.grid(row=4,column=0, padx="15px",pady="5px")
		self.id = ttk.Entry(self,textvariable=self.nameHolder)
		self.password = ttk.Entry(self,textvariable=self.nameHolder)
		self.idLabel = ttk.Label(self,text="Enter gmail account :")
		self.passLabel = ttk.Label(self,text="Enter password :")
		
		return
	def timerInfoInput(self):
	#create a pop up box to take information
		self.inputBox = tk.Toplevel(self)
		self.inputBox.title("infoBox")
		self.nameLabel = tk.Label(self.inputBox,text="Enter the name of alarm :")
		self.nameTextBox = tk.Entry(self.inputBox,textvariable=self.nameHolder)
		self.timeLabel = tk.Label(self.inputBox,text="Set alarm time(minutes) :")
		self.timeTextBox = tk.Entry(self.inputBox,textvariable=self.timeHolder)
		self.submitButton = tk.Button(self.inputBox,text="Submit",command=self.destroyInput)
		
		self.inputBox.grid()
		self.nameLabel.grid(row=0,column=0)
		self.nameTextBox.grid(row=1,column=0)
		self.timeLabel.grid(row=2,column=0)
		self.timeTextBox.grid(row=3,column=0)
		self.submitButton.grid(row=4,column=0)
		return
	def destroyInput(self):
		#pass everything through to next window and or make the calendar event
		#print(self.nameHolder.get())
		name = self.nameHolder.get()
		#print(self.timeHolder.get())
		time = self.timeHolder.get()
		self.nameHolder.set("")
		self.timeHolder.set(0)
		self.inputBox.destroy()
		self.timers[name] = Timer(name,time)
	def removeTimer(self,name):
		#remove the timer
		del dict(self.timers)[name]
		self.popUp = tk.Toplevel()
		self.exitLabel = tk.Label(self.popUp,text=("Task " + name + " has concluded"))
		self.exitButton = tk.Button(self.popUp,text="Okay",command=self.popUp.destroy)
			
		self.popUp.grid()
		self.exitLabel.grid()
		self.exitButton.grid()
		return
	def greyOut(self):
		#Last resort if google api don't work
		if self.checkBtnValue.get() == 1:
			self.id.grid(row=1,column=0)
			self.password.grid(row=3,column=0)
			self.idLabel.grid(row=0,column=0)
			self.passLabel.grid(row=2,column=0)
		else:
			
			self.id.grid_remove()
			self.password.grid_remove()
			self.idLabel.grid_remove()
			self.passLabel.grid_remove()
		return

class Timer(tk.Toplevel):
	def __init__(self,name,time,master=None):
		#making timer box
		tk.Toplevel.__init__(self,master=None)
		self.name = name
		self.time = time*60
		self.grid()
		self.createWidgets()
		self.tickDown()
		return
	def createWidgets(self):
		#making timer widgets
		self.nameLabel = ttk.Label(self,text=self.name,font=('Helvetica', 12))
		self.timeLabel = ttk.Label(self, text=self.timeDisp(),font=('Helvetica', 16))
		self.closeButton = ttk.Button(self,text="Close",command=self.clearTimer)		

		self.nameLabel.grid(row=0,column=0,rowspan=1,columnspan=2)
		self.timeLabel.grid(row=1,column=0)
		self.closeButton.grid(row=1,column=1)
		return
	def tickDown(self):
		#count down the timer
		if self.time != 0: 
			self.time = self.time - 1
			self.timeLabel.configure(text=self.timeDisp())
			self.after(1000,self.tickDown)
		else:
			self.clearTimer()
		return
	def timeDisp(self):
		#makes displayable timer
		days = self.time// 86400
		hours = (self.time % 86400) // 3600 
		minutes = (self.time % 3600) // 60
		seconds = (self.time % 60)
		
		if days < 10 :
			days = "0" + str(days)
		else: days = str(days)
		if hours < 10:
			hours = "0" + str(hours)
		else: hours = str(hours)
		if minutes < 10:
			minutes = "0" + str(minutes)
		else: minutes = str(minutes)
		if seconds < 10: 
			seconds = "0" + str(seconds)
		else: seconds = str(seconds)
		holder = days + ":" + hours + ":" + minutes + ":" + seconds   
		return holder
	def clearTimer(self):
		self.time = 0
		AddTimer.removeTimer(app,self.name)
		self.destroy()
		return
app = AddTimer()
app.master.title("Timer")
app.mainloop()



			
