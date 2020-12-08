def solve(a,b,c):
    if( a == 0 and b!=0 ):
        y = -c/b
        print("x jest dowolne, y = ",str(y))
    elif( a!=0 and b==0 ):
        x = -c/a
        print("y jest dowolne, x = ",str(x))
    elif( a!=0 and b!= 0 ):
        y="(-"+str(a)+"*x-"+str(c)+"/b"
        print("Rozwiazanie nalezy do przedzialu (x,",str(y),")","x nalezy do zbioru liczb rzeczywistych.")

    elif( a==0 and b==0 and c==0):
        print("Równanie posiada nieskonczenie wiele rozwiazan")

    elif(a==0 and b==0 and c!=0):
        print("Rownanie sprzeczne")
