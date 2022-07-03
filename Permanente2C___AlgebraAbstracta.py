import math

def euclides_extendido(a, b):
    if a == 0 :
        return b, 0, 1
    mcd,x1,y1 = euclides_extendido(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return mcd,x,y

def modulo(a,b): 
    r=a%b
    if r < 0:
        r=r+ b;
    return r

def inversa(a,b):
    m, a, y = euclides_extendido(a, b)
    if m == 1:
      a = modulo(a, b)
    return a

#print(inversa(7, 1.3690042483646612e+109))
m = pow(747120213790,755383642193,999630013489)
print(m)