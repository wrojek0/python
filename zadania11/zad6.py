from zad1 import *
from stack import *

def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item



def partition(L,left,right):
    i = left - 1
    x = L[right]

    for j in range(left,right):
        if L[j]<=x:
            i+=1
            swap(L,i,j)
    swap(L,i+1,right)
    return i+1


#iteracyjna wersja quicksort z uzyciem stosu
def quicksort(L,left,right):
    stack = Stack(right-left+1)
    stack.push(left)
    stack.push(right)
    while( stack.is_empty() == False ):
        right = stack.pop()
        left = stack.pop()
        pivot = partition(L,left,right)
        if( pivot-1>left):
            stack.push(left)
            stack.push(pivot-1)

        if pivot+1<right:
            stack.push(pivot+1)
            stack.push(right)







def main():
    tab = randIntegers(20)
    print("Przed sortowaniem: ",tab)
    quicksort(tab,0,19)
    print("Posortowane:",tab)

    print("\n\n")

    tab2 = randIntegers(100)
    quicksort(tab2,0,99)
    for i in range(100):
        assert(tab2[i] == i)
   

   
    

if __name__ == "__main__":
    main()
    




