from abc import ABC, abstractmethod


# TODO: Add event types to notify observers only when relevant events happen.
class Observer(ABC):
    """Abstract class for an observer object in observer pattern."""

    def __init__(self):
        pass
    
    
    @abstractmethod
    def on_event(self, source):
        """Called when an event regarding an observed object happens.
        
        :param source: The source object of the event
        :type source: Observable
        """
        pass
