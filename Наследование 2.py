Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Seat:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f"{self.__class__.__name__}({', '.join([str(x) for x in self.args])})"


class Chair(Seat):
    pass


class ArmChair(Seat):
    pass


class Stool(Seat):
    pass


class BagChair(Seat):
    pass

##################################
class NestingDoll:
    def __init__(self, s):
        self.s = s

    def get_size(self):
        return self.s

    def __str__(self):
        return f'Russian Folk doll, size {self.s}.'


class OrdinaryNestingDoll(NestingDoll):
    def __init__(self, s, st):
        self.s = s
        self.st = st

    def get_size(self):
        return self.s

    def previous_doll(self):
        return OrdinaryNestingDoll(self.s + self.st, self.st)

    def next_doll(self):
        if self.s - self.st <= 0:
            return SmallestNestingDoll(self.s, self.st)
        else:
            return OrdinaryNestingDoll(self.s - self.st, self.st)

    def __str__(self):
        return f'Russian Folk doll, size {self.s}.'


class SmallestNestingDoll(OrdinaryNestingDoll):
    def __init__(self, s, st):
        self.s = s
        self.st = st

    def get_size(self):
        return self.s

    def next_doll(self):
        return None

    def previous_doll(self):
        return OrdinaryNestingDoll(self.s + self.st, self.st)

    def __str__(self):
        return f'Russian Folk doll, size {self.s}.'

##############################
class Cucumber:
    def crunch(self):
        return f'crunch'

    def refresh(self):
        return f'Cucumber refresh.'


class Tomato:
    def melt(self):
        return f'melt'

    def refresh(self):
        return f'Tomato refresh.'


class Salad(Tomato):
    def __init__(self):
        Tomato.__init__(self)


class Smoothie(Cucumber):
    def __init__(self):
        Cucumber.__init__(self)