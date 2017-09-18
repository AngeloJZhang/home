#!/usr/bin/env python
import time
#put in single instance code
class dispholder:
    def __init__(self,addtime):
        self.stime = time.time()
        self.etime = self.stime + 60*addtime
        return
    def countdown(self):
        print("Running until %s"%(time.ctime(self.etime)))
        while self.stime < self.etime:
            print(time.ctime(self.stime))
            time.sleep(5)
            self.stime= self.stime + 5.0
        print("Timer End")
        return
def main():
    timelength = float(input("Set timer(mins) : "))
    a = dispholder(timelength)
    a.countdown()
    return
#def vinput(valtype):
    
    return holder
if __name__=="__main__":
    main()
