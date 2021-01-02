import math
import random

# Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
# (a) różne liczby int od 0 do N-1 w kolejności losowej,
# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).


#a
def randIntegers(N):
    nums = list(range(N))
    random.shuffle(nums)
    return nums

#b
def almostSortedRandIntegers(N):
    nums = list(range(N))
    for i in range(0,int(N/3)):
        rand = random.randint(2,N-1)
        temp = nums[rand]
        nums[rand] = nums[rand-2]
        nums[rand-2] = temp
    return nums


#c
def almostSortedRandIntegersReversed(N):
    lista = almostSortedRandIntegers(N)
    lista.reverse()
    return lista

#d
def randGaus(N):
    nums = []
    for i in range(N):
        nums.append(random.gauss(0,N))
    return nums

#e
def repeatedElements(N):
    nums=[]
    for i in range(N):
        nums.append(random.randint(0, math.floor(math.sqrt(N))))
    return nums



def main():
    lista = randIntegers(10)
    print(lista)

    lista2 = almostSortedRandIntegers(10)
    print(lista2)
    
    lista3 = almostSortedRandIntegersReversed(10)
    print(lista3)

    lista4 = randGaus(10)
    print(lista4)
    
    lista5 = repeatedElements(10)
    print(lista5)

if __name__ == "__main__":
    main()