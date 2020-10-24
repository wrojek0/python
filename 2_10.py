
#------------------------------------------------2.10------------------------------------------------------------------------#
#Mamy dany napis wielowierszowy line
#Podać sposób obliczenia liczby wyrazów w napisie.
#Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).


line = """
ala\n ma\t kota
raz     dwa trzy
cztery pięć     sześć  siedem
"""

list = line.split()
print("Liczba wyrazow w napisie wielowierszowym: ",len(list))
