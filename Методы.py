Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ChairLeg:
    def __init__(self, length):
        self.length = length

    def __mul__(self, other):
        self.length = self.length * other
        return self

    def __floordiv__(self, other):
        self.length = self.length // other
        return self

    def __mod__(self, other):
        return self.length % other

    def __rmul__(self, other):
        self.length = other * self.length
        return self

    def length(self):
        return f'{self.length}'

####################################
class Butterfly:
    def __init__(self, v):
        self.v = v
        self.v2 = 0
        self.c = 0

    def __iadd__(self, other):
        self.c += other
        if self.c > self.v:
            self.c = self.v
        elif self.c < 0:
            self.c = 0
        return self

    def __add__(self, other):
        self.v2 = self.v + other.v
        return Butterfly(self.v2)

    def __floordiv__(self, other):
        r = list()
        if self.v % other == 0:
            for i in range(other):
                r.append(Butterfly(self.v // other))
        else:
            for i in range(other):
                r.append(Butterfly(self.v // other))
            r.append(Butterfly(self.v % other))
        return r

    def __repr__(self):
        return f'Butterfly({self.v})'

    def __str__(self):
        return f'Volume: {self.v}, content: {self.c}'

################################
class PearsBasket:
    def __init__(self, k):
        self.k = k

    def __floordiv__(self, other):
        if self.k % other:
            return [PearsBasket(self.k // other) for _ in range(other)] + [PearsBasket(self.k % other)]
        else:
            return [PearsBasket(self.k // other) for _ in range(other)]

    def __mod__(self, other):
        return self.k % other

    def __add__(self, other):
        return PearsBasket(self.k + other.k)

    def __sub__(self, other):
        if self.k < other:
            self.k = 0
        else:
            self.k = self.k - other
        return self

    def __str__(self):
        return str(self.k)

    def __repr__(self):
        return f'PearsBasket({self.k})'

##################################
class Queue:
    def __init__(self):
        self.q = []

    def add(self, other):
        self.q.append(other)
        return 'done'

    def remove(self):
        if len(self.q) != 0:
            a = self.q[0]
            del self.q[0]
            return a
        else:
            return None

    def len(self):
        return len(self.q)

    def last(self):
        if len(self.q) != 0:
            return self.q[-1]
        else:
            return None

    def first(self):
        if len(self.q) != 0:
            return self.q[0]
        else:
            return None

    def clear(self):
        self.q.clear()
        return 'done'