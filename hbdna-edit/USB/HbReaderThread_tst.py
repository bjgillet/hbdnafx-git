import threading
import time
import HbDevice
class DevReader (threading.Thread):
    
    def __init__(self, hb_device): #, ev_run):
        threading.Thread.__init__(self)
        self.ev_run = threading.Event()
        self.running = False
        self.halt = False
        self.ev_is_dead = threading.Event()
        self.hb_dna = hb_device

    def run(self):
        print("Starting Thread")
        while True:
            self.ev_run.wait()
            if not self.running :
                self.running = True
                print("DevReader flushing")
            if self.halt: 
                print("DevReader aborting")
                self.ev_is_dead.set()
                break
            print("DevReader running")
            time.sleep(10)

    def pause(self):
        print("DevReader pausing")
        self.running = 0
        self.ev_run.clear()

    def resume(self):
        print("DevReader resuming")
        self.ev_run.set()

    def stop(self):
        self.halt=True
        self.ev_run.set()
        


#ev_run=threading.Event()

cmd=""
hb_dna = HbDevice.HbDevice()
dev_reader = DevReader(hb_dna)
dev_reader.start()

while cmd != "q":
    cmd = input("Enter run/pause/q : ")
    if cmd == "run":
        dev_reader.resume()
    elif cmd == "pause":
        dev_reader.pause()
dev_reader.stop()
print("waiting for dev_reader termination")
dev_reader.ev_is_dead.wait()
print("ev_event is now down - quitting !")