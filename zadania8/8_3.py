import random
import math

def calc_pi(n=100):
    inside = 0
    for i in range(n):
        x=random.random()**2
        y=random.random()**2
        if( math.sqrt(x+y) <= 1.0 ):
            inside+=1

    pi = (inside/n)*4
    return pi


def main():
    print("Wartosc pi dla n=100",calc_pi() )
    print("Wartosc pi dla n=500",calc_pi(500) )
    print("Wartosc pi dla n=1000",calc_pi(1000) )
    print("Wartosc pi dla n=10000",calc_pi(10000) )
    print("Wartosc pi dla n=100000",calc_pi(100000) )
    print("Wartosc pi dla n=1000000",calc_pi(1000000) )
    print("Wartosc pi dla n=2000000",calc_pi(2000000) )



if __name__ == '__main__':
    main()
