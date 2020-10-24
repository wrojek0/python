#----------------------------2.11----------------------------------------------------------------#
#Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

word = "slowo"
new_word = ""
temp = word[:-1]

for char in temp:
    new_word += char+"_"

new_word+=word[-1]
print(new_word)
