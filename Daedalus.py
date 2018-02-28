from numpy import random

## Daedalus
class Daedalus:
    C = 0.118949192725403987583755553
    N = 0
    
    def __init__(self):
        self.N = 0

    def hit(self):
        self.N += 1
        P = self.N * self.C
        if P > 1.0: 
            P = 1.0
        crit = random.binomial(1, P)
        if (crit == 1):
            self.N = 0
        return int(crit)

## Statistic func
def count(mat, pat):
    cparr = map(int, pat)
    n = len(cparr)
    ret = 0
    for arr in mat:
        if (arr[:n]==cparr): 
            ret += 1
    return float(ret)

## Program starts
Daedalus1 = Daedalus()
Daedalus2 = Daedalus()

num = 1000*1000*1
mat = []
for i in range(num):
    n = random.randint(5,10)
    arr = []
    for j in range(n):
        hit1 = Daedalus1.hit()
        hit2 = Daedalus2.hit()
        hit = hit1 | hit2
        arr.append(hit)
    mat.append(arr)

## Count
crit1 = count(mat, '1')
print 'P(1) =', round(crit1/num, 3)
crit11 = count(mat, '11')
print 'P(11) =', round(crit11/num, 3)
crit111 = count(mat, '111')
print 'P(111) =', round(crit111/num, 3)
crit0 = count(mat, '0')
print 'P(0) =', round(crit0/num, 3)
crit00 = count(mat, '00')
print 'P(00) =', round(crit00/num, 3)
crit000 = count(mat, '000')
print 'P(000) =', round(crit000/num, 3)
crit01 = count(mat, '01')
print 'P(1|0) =', round(crit01/crit0, 3)
crit001 = count(mat, '001')
print 'P(1|00) =', round(crit001/crit00, 3)
crit0001 = count(mat, '0001')
print 'P(1|000) =', round(crit0001/crit000, 3)

