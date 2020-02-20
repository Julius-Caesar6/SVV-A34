


class Macaulay:
    def __init__(self,a, b, power):
        # Macaulay function in form: b*<x-a>**power.
        self.a = a
        self.b = b
        self.power = power

    def result(self, x): #FIXME if power=0, does it always return 1 or 0 in case x<a
        if x < self.a:
            return 0
        else:
            return self.b*((x-self.a)**self.power)

    def integrate(self):
        self.power += 1
        self.b  = self.b / self.power

    def differentiate(self):
        if self.power == 0:
            self.b = 0
        else:
            self.b = self.b * self.power
            self.power -= 1


