class Macaulay:
    def __init__(self,a, b, power):
        # Macaulay function in form: b*<x-a>**power.
        self.a = a
        self.b = b
        self.power = power

    def result(self, x):
        if x < self.a:
            return 0
        else:
            return self.b*((x-self.a)**self.power)

    def integrate(self):
        self.power += 1
        self.b  = self.b / self.power


