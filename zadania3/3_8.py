list1 = [1,3,5,7,9,6,'z']
list2 = [1,'z',2,4,7,8,10,6]
intersection =  list(set(list1).intersection(list2));
difference = list(set(list1).union(list2))
print("Lista elementow w list1 i list2: ",intersection)
print("Lista bez powtorzen z obu sekwencji: ",difference)
