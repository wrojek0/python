#------------------------2.14---------------------------------
#Zalezc:
#a) najdluzszy wyraz
#b) dlugosc najdluzszego wyrazu w napisie

napis = "12      123 1234 12 123456789 1 aaaaa"
list = napis.split()
list2 = []

longest = max(list,key=len)
longest_len = len(longest)
ind = list.index(longest)
print("Najdluzszy wyraz: ",longest)
print("Jego długosc:",longest_len)
