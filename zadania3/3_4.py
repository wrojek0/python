while True:
    x = input("Prosze podac liczbe: ")
    try:
        if x=="stop":
                break;
        x=float(x)
        print("(",x,",",x**3,")" );
    except ValueError:
            print("Blad!");
