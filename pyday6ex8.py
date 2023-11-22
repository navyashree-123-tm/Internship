class Monitor:
    def __init__ (self,resolution,refresh_rate):
        self.resolution=resolution
        self.refresh_rate=refresh_rate

    def display_info():
        print("Monitor Resolution:{self.resolution}, RefreshRate:{self.refresh_rate}")
              
class Computer(Monitor):
    def __init__ (self, monitor):
        self.monitor=Monitor
