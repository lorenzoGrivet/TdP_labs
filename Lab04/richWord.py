class RichWord:
    def __init__(self, parola):
        self._parola = parola
        self._corretta = None

    # def isCorretta(self):
    #     if self._corretta is not None:
    #         return self._corretta

    @property
    def corretta(self):
        print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        return self._parola