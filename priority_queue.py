class PriorityQueueBase:
    
    class _Item:
        __slots__ = '_key','_value'  #key sets priority to element
    
        def __init__(self,k,v):
            self._key = k
            self._value = v
            
        def __lt__(self,other):
            return self._key < other._key #compare items based on key

        def __repr__(self):
                return '({0},{1})'.format(self._key, self._value) 
             
    def is_empty(self):
        return len(self) == 0        

    def __len__(self):
            """Return the number of items in the priority queue."""
            raise NotImplementedError('must be implemented by subclass')

    def add(self, key, value):
        """Add a key-value pair."""
        raise NotImplementedError('must be implemented by subclass')

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        raise NotImplementedError('must be implemented by subclass')

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        raise NotImplementedError('must be implemented by subclass')



##UNSORDED LIST IMPLEMENTATION
## ADD HAS O(1) COMPLEXITY
## REMOVE AND MIN HAS O(N) 

class UnsortedPriorityQueue(PriorityQueueBase):
    
    def __init__(self):
        self._data = PositionalList()
         
    
    
    
    
    
    