#---------------------2_15-----------------------
#Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.


L = [1,2,3,4,5,6,7,8,9]
napis = ""
for number in L:
    napis+=str(number)

print(napis)
