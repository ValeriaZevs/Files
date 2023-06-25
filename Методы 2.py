Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Knight:
    def __init__(self, name, weight, weapon):
        self.n = name
        self.w = weight
        self.wep = weapon

    def overturn(self):
        self.n = ''.join(reversed(self.n.lower())).capitalize()
        if len(self.wep) != 0:
            self.wep.append(self.wep[0])
            self.wep = self.wep[1:]
        return self

    def add_weapon(self, unit):
        self.wep.append(unit)
        return self

    def add_weight(self, value):
        self.w = self.w + value
        if self.w < 0:
            self.w = 0

    def __eq__(self, other):
        return (self.w, len(self.wep), self.n) == (other.w, len(other.wep), other.n)

    def __ne__(self, other):
        return (self.w, len(self.wep), self.n) != (other.w, len(other.wep), other.n)

    def __lt__(self, other):
        return (self.w, len(self.wep), self.n) < (other.w, len(other.wep), other.n)

    def __gt__(self, other):
        return (self.w, len(self.wep), self.n) > (other.w, len(other.wep), other.n)

    def __le__(self, other):
        return (self.w, len(self.wep), self.n) <= (other.w, len(other.wep), other.n)

    def __ge__(self, other):
        return (self.w, len(self.wep), self.n) >= (other.w, len(other.wep), other.n)

    def __str__(self):
        if len(self.wep) != 0:
            return f'Knight {self.n}, weapon {self.wep[0]}, {self.w}'
        else:
            return f'Knight {self.n}, weapon , {self.w}'

#######################################
class VoltaicPile:
    def __init__(self, x):
        self.my_list = x[:]
        self.i = 0

    def __iter__(self):
        return iter(self.my_list)

    def __next__(self):
        k = self.my_list[self.i]
        self.i += 1
        return k

    def __getitem__(self, key):
        return self.my_list[key]

    def __setitem__(self, key, v):
        self.my_list[key] = v
        return self

    def __len__(self):
        return len(self.my_list)

    def append(self, x):
        if len(self.my_list) == 0:
            self.my_list.append(x)
        elif len(self.my_list) > 1:
            if x in 'Cu' and self.my_list[-1] == 'cloth' and self.my_list[-2] == 'Zn':
                self.my_list.append(x)
            elif x in 'Zn' and self.my_list[-1] == 'cloth' and self.my_list[-2] == 'Cu':
                self.my_list.append(x)
            elif x == 'cloth' and self.my_list[-1] in 'Cu Zn':
                self.my_list.append(x)
        elif len(self.my_list) == 1:
            a = (self.my_list[0] == 'Zn' and x == 'Cu')
            if self.my_list[0] != x and not (self.my_list[0] == 'Cu' and x == 'Zn') and not a:
                self.my_list.append(x)

    def __str__(self):
        cu = self.my_list.count('Cu')
        zn = self.my_list.count('Zn')
        return f'{min(cu, zn) * 1.1} V.'

##########################################
class Wagon:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f'№{self.n}'

    def get_number(self):
        return self.n


class Train:
    def __init__(self, n, wagon=None):
        self.n = n
        self.w = []
        if wagon is not None:
            self.w = wagon[:]

    def get_number(self):
        return self.n

    def get_wagons(self):
        return self.w

    def append(self, j):
        self.w.append(j)

    def __len__(self):
        return len(self.w)

    def __str__(self):
        return f'Train {self.n} has {len(self.w)} wagons'

    def __iter__(self):
        return iter(self.w)

    def __getitem__(self, key):
        return self.w[key]

    def __setitem__(self, key, other):
        self.w[key] = other
        return self

    def __delitem__(self, key):
        if key == len(self.w) - 1:
            del self.w[-1]
        return self