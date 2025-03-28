class RichWord:
    def __init__(self, parola):
        self._parola = parola # this is a string
        self._corretta = None #this is a bool

    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        return self._parola