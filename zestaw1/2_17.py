#----------------------------------------2.17-----------------------------
#Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().




napis ="ala ma kota abc raz dwa trzy "
lista = napis.split()

print("Sortowanie alfabetyczne: ",sorted(lista))
print("Sortowanie pod wzgledem dlugosci: ",sorted(lista,key=len))
