"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start = 0):
        """Makes new number generator starting from 'start' 
        Attributes
        --------------
        start: int
                starting number
        """
        self.start = start
        self.next = start
    
    def __repr__(self):
        """Representation"""

        return f"<SerialGenerator start = {self.start} next = {self.start+1}>"
    
    
    def generate(self):
        """Returns number next to previously returned"""
        self.next +=1 
        return self.next-1
    
    def reset(self):
        """Resets starting number to start"""
        self.next = self.start
        return self.start
