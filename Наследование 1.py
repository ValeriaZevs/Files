Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Rewrite:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def done(self):
        with open(self.a, 'r') as r:
            w = open(self.b, 'w')
            k = r.read()
            w.write(k)


class Calculus(Rewrite):
    def __init__(self, a, b):
        Rewrite.__init__(self, a, b)

    def five_per_line(self):
        with open(self.a, 'r') as r:
            w = open(self.b, 'w')
            k = r.readlines()
            tow = []
            for i in k:
                j = i.rstrip().split(' ')
                for h in j:
                    if h != '':
                        tow.append(int(h))
            tow.sort()
            u = []
            s = []
            for i in range(len(tow)):
                if (i + 1) % 5 != 0 and i != len(tow) - 1:
                    u.append(str(tow[i]))
                elif i == len(tow) - 1:
                    u.append(str(tow[i]))
                    s.append(" ".join(u))
                else:
                    u.append(str(tow[i]))
                    s.append(" ".join(u))
                    u = []
            for i in s:
                w.write(i + '\n')


class Align(Rewrite):

    def __init__(self, a, b):
        Rewrite.__init__(self, a, b)

    def to_right(self):
        with open(self.a, 'r') as r:
            w = open(self.b, 'w')
            k = r.readlines()
            al = []
            k = [i.rstrip().split(' ') for i in k]
            for i in k:
                for j in i:
                    if j != '':
                        al.append(j)
            m = sorted(al, key=len)[-1]
            for i in al:
                w.write(' ' * (len(m) - len(i)) + i + '\n')

#################################
class Wardrobe:
    def __init__(self, *args):
        self.a = args

    def __str__(self):
        return " ".join(self.a)


class JustWardrobe(Wardrobe):
    def __init__(self, *args):
        self.a = args

    def __str__(self):
        self.a = [i.capitalize() if i == self.a[0] else i for i in self.a]
        return ", ".join(self.a) + '.'

    def __eq__(self, other):
        if type(other) == MagicWardrobe:
            return False
        else:
            return len(self.a) == len(other.a)

    def __ne__(self, other):
        if type(other) == MagicWardrobe:
            return True
        else:
            return len(self.a) != len(other.a)

    def __lt__(self, other):
        if type(other) == MagicWardrobe:
            return True
        else:
            return len(self.a) < len(other.a)

    def __gt__(self, other):
        if type(other) == MagicWardrobe:
            return False
        else:
            return len(self.a) > len(other.a)

    def __le__(self, other):
        if type(other) == MagicWardrobe:
            return True
        else:
            return len(self.a) <= len(other.a)

    def __ge__(self, other):
        if type(other) == MagicWardrobe:
            return False
        else:
            return len(self.a) >= len(other.a)


class MagicWardrobe(Wardrobe):
    def __init__(self, *args):
        self.a = args

    def __str__(self):
        self.a = [i.capitalize() for i in self.a]
        self.a.sort()
        return ", ".join(self.a) + '.'

    def __eq__(self, other):
        if type(other) == JustWardrobe:
            return False
        else:
            return len(self.a) == len(other.a)

    def __ne__(self, other):
        if type(other) == JustWardrobe:
            return True
        else:
            return len(self.a) != len(other.a)

    def __lt__(self, other):
        if type(other) == JustWardrobe:
            return False
        else:
            return len(self.a) < len(other.a)

    def __gt__(self, other):
        if type(other) == JustWardrobe:
            return True
        else:
            return len(self.a) > len(other.a)

    def __le__(self, other):
        if type(other) == JustWardrobe:
            return False
        else:
            return len(self.a) <= len(other.a)

    def __ge__(self, other):
        if type(other) == JustWardrobe:
            return True
        else:
            return len(self.a) >= len(other.a)