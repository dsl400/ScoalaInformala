
class Fractie():

    def __init__(self,numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'{self.numarator}/{self.numitor}'
    
    def __add__(self,fractie):
        return Fractie(
            self.numarator * fractie.numitor + fractie.numarator  * self.numitor,
            self.numitor * fractie.numitor
        )
    
    def __sub__(self,fractie):
        return Fractie(
            self.numarator * fractie.numitor - fractie.numarator  * self.numitor,
            self.numitor * fractie.numitor
        )

    def inverse(self):
        return Fractie(self.numitor,self.numarator)

