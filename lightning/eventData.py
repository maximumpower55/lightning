from typing import Callable
from dataclasses import dataclass

@dataclass
class EventData:
    target: Callable