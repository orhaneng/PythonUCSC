'''
# Question 1: 5 points

Quadratic equations
'''
class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return '%d x^2 + %d x + %d' %(self.a,self.b,self.c)

    def __add__(self,other):
        return Quadratic(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self,other):
        return Quadratic(self.a - other.a, self.b - other.b, self.c - other.c)

    def __eq__(self,other):
        if(self.a == other.a and self.b == other.b and self.c == other.c):
            print("The two quadratic expressions are equal")
            return True
        else:
            print("The two quadratic expressions are not equal")
            return False

q1 = Quadratic(3, 8, -5)
q2 = Quadratic(2, 3, 7)

print("The sum of the given quadratic expressions is ", q1 + q2)
print("The difference of the given quadratic expressions is ", q1 - q2)
print(q1 == q2)


'''
# Question 2: 5 points

Word counter

'''

import string, csv

class WordCounter:
    def __init__(self,filename):
        self.filename = filename
        self.contentlist = []
        self.cleanlist = []
        self.countdict = {}
        fo = open(self.filename,'r')
        for lines in fo.readlines():
            lineitems = lines.strip().split()
            self.contentlist.extend(lineitems)

    def removepunctuation(self):
        for items in self.contentlist:
            cleanstring = items
            for c in string.punctuation:
                cleanstring = cleanstring.replace(c,"")
            if cleanstring != '':
                self.cleanlist.append(cleanstring)

    def findcount(self):
        uniqlist = list(set(self.cleanlist))
        print uniqlist
        for items in uniqlist:
            self.countdict[items] = self.cleanlist.count(items)

    def writecountfile(self,csvfilename):
        writer = csv.writer(open(csvfilename, 'wb'))
        for key, value in self.countdict.items():
            writer.writerow([key, value])

wc = WordCounter('red-headed-league.txt')
wc.removepunctuation()
wc.findcount()
print(wc.countdict)
wc.writecountfile('my4.csv')
