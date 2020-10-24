#-----------------------------------------2.13------------------------------------------------#
#Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

napis = "ala ma kota"
dlugosc = 0
list = napis.split()

for word in list:
    dlugosc+=len(word)

print(dlugosc)
