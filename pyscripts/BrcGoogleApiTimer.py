#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from threading import Timer

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'timer'

app = AddTimer()
app.master.title("Timer")
app.mainloop()
	
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
		if self.checkBtnValue.get == 1:
			try:
				event = {'summary': str(name),'location': '263 W. End Ave, NewYork, NewYork','start': {'dateTime': str(datetime.datetime)},'end': {'dateTime': str(datetime.datetime)}, 'attendees': [{'email': ''},],}
			 	#event ={'summary': name,
				#	'location': '263 W. End Street',
				#	'start': {'dateTime': datetime.datetime},
				#	'end': {'dateTime': datetime.datetime}, 
				#	'attendees': [{'email': ''}]}
				created_event = service.events().insert(calendarId='primary',body=event).execute
				break
			except LoginError:
				print("Login Problems")
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
		#if self.checkBtnValue.get() == 1:
		#	self.id.grid(row=1,column=0)
		#	self.password.grid(row=3,column=0)
		#	self.idLabel.grid(row=0,column=0)
		#	self.passLabel.grid(row=2,column=0)
		#else:
		#	
		#	self.id.grid_remove()
		#	self.password.grid_remove()
		#	self.idLabel.grid_remove()
		#	self.passLabel.grid_remove()
		#return

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
		self.nameLabel = ttk.Label(self,text=self.name)
		self.timeLabel = ttk.Label(self, text=self.timeDisp())
		self.closeButton = ttk.Button(self,text="Close",command=self.clearTimer)		

		self.nameLabel.grid(row=0,column=0)
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
def main():
	try:
		credentials = get_credentials()
		http = credentials.authorize(httplib2.Http())
		service = discovery.build('calendar', 'v3', http=http)
		now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
		break
	except LoginError:
		print("LoginError")


def get_credentials():
    	"""Gets valid user credentials from storage.

    	If nothing has been stored, or if the stored credentials are invalid,
    	the OAuth2 flow is completed to obtain the new credentials.

   	 Returns:
		Credentials, the obtained credential.
	    """
	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
	os.makedirs(credential_dir)
	credential_path = os.path.join(credential_dir,'calendar-python-quickstart.json')

	store = Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		flow.user_agent = APPLICATION_NAME
		if flags:
		    credentials = tools.run_flow(flow, store, flags)
		else: # Needed only for compatibility with Python 2.6
		    credentials = tools.run(flow, store)
		print('Storing credentials to ' + credential_path)
	return credentials
	   


if __name__ = '__main__':
	main()
			
			
