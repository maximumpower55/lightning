from .event import Event
from .eventData import EventData
from decorator import decorator
from collections import Sequence

class EventManager:
    def __init__(self) -> None:
        self.event_map: dict[Event, list[EventData]] 

    @classmethod
    def register(cls, event: Event):
        cls.event_map.setdefault(event, None)

    @classmethod
    @decorator
    def on(cls, f, event: Event):
        cls.event_map.setdefault(event, EventData(f))

        return f

    @classmethod
    def getEventData(cls, event: Event) -> list[EventData]:
        try:
            return cls.event_map.get(event)
        except Exception:
            return None

class TestEvent(Event): pass

eventManager = EventManager()

EventManager.register(TestEvent)

@EventManager.on(TestEvent)
def on_test():
    print("IT'S WORKING")

for event in eventManager.event_map.keys():
    event.invoke()