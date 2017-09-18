from appJar import gui
import time

#time
currentTime = time.ctime()

#app size
xlen = 200
ylen = 100

#increase app size
def upylen():
    global ylen
    ylen = ylen + 100
    return ylen

#timercounter
counter = 0

def counterup():
    global counter
    counter = counter + 1
    return counter

#gui setting
app = gui("Timer","%dx%d"%(xlen,ylen))
app.setSticky("news")

app.setFont(20)
app.setLocation(0,0)

#methods for button
def createApp(holder):
    #time = 0
    time = app.textBox("Duration of Timer","Set Time (Minutes) :")
    #check for int and not 0
    x = dispholder(time,counterup())
    return
def deleteApp(holder):
    
    return

#class for single timer instance
class dispholder:
    def __init__(self,timelength,tid):
        self.etime = float(timelength)*60
        self.id = tid
        app.addLabel(self.id,self.etime,1,1,1)
        #app.addButton("Start",self.countdown,1,2,1)
        app.setGeometry(xlen,upylen())
        app.registerEvent(self.downone())
        return
    def countdown(self,holder):
        return
    def downone(self):
        if self.etime != 0:
            print("test")
            self.etime = self.etime - 1
            app.setLabel(self.id,self.etime)
            app.update()
        return
    
#buttons
app.addButton("+",createApp,0,0)
app.addButton("-",deleteApp,0,1)

#assurance checks

#main function
def main():
    app.go()
    return
if __name__=="__main__":
    main()

