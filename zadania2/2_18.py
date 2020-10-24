#---------------------------------2.18------------------------------
#Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.



liczba = 120003000405550

liczba_str = str(liczba)
ile = 0
for char in liczba_str:
    if char == '0':
        ile+=1

print("Liczba zer: ",ile)
