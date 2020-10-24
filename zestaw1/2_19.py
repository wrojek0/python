#------------------------------------2.19-------------------------
#Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
#Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().


list = [12,136,1,78,65,432,111,12,9]
res = []
for i in list:
    res.append(str(i).zfill(3))

print(res)
