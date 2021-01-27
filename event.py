from eventmanager import LightningEventManager
from eventData import EventData
from dataclasses import dataclass

class Event:
    def invoke(self):
        datalist: EventData = LightningEventManager.getEventData(self.__class__)
        
        if datalist != None:
            try:
                for data in datalist:
                    data.target.execute()
            except Exception as e:
                raise e