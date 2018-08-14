from abc import ABC


# TODO: Add event types to notify observers only when relevant events happen.
class Observable(ABC):
    """Abstract class for an observable object in observer pattern."""

    def __init__(self):
        self._observers = []


    def add_observer(self, o):
        """Adds an observer of this object.
        
        :param o: The observer to add
        :type o: Observer
        """
        self._observers.append(o)
    
    def remove_observer(self, o):
        """Removes an observer of this object.
        
        :param o: The observer to remove
        :type o: Observer
        """
        if o in self._observers:
            self._observers.remove(o)
    
    def remove_all_observers(self):
        """Removes all observers of this object."""
        self._observers = []
    
    def notify(self):
        """Notifies all observers that an event has occurred."""
        for o in self._observers:
            o.on_event(self)
