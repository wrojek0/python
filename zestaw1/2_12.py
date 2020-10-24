
#-----------------------2.12-----------------------------------------#
#Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.#
#Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line. #



napis = "wlazl kotek na plotek"
res = ""
res2= ""
list = napis.split()
for words in list:
    res+=words[0]
    res2+=words[-1]

print(res)
print(res2)
