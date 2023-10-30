import math


def zad1():
    print("wpisz wartość bezwzględną")
    a = float(input())
    print("wartość bezwględna liczby x={} ".format(a),end=" ")
    if 0 > float(a):
        a = a*(-1)
    print("jest równa ", a)
def zad2():
    print("wpisz wastość ")
    n = float(input())

    def sgn(x):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        else:
            return 1
    sgn(n)
    print("jest równa ", sgn(n))
def zad3():
    print("wpisz pierwszą liczbę")
    a = float(input())
    print("wpisz drugą liczbę")
    b = float(input())
    if b == 0:
        print("Błąd (Nie można dzielić przez zero) ")
    else:
        a = a/b
        print(a)
def zad4():

def main():
    #zad1()
    #zad2()
    #zad3()
    zad4()

main()
