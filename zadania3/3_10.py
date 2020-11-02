#sposob I
D = {"I": 1, "V": 5, "X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}

#sposob II
D1 ={}
D1["I"]= 1
D1["V"]= 5
D1["X"]= 10
D1["L"]= 50
D1["C"]= 100
D1["D"]= 500
D1["M"]= 1000

#sposob III
D2=dict([("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)])

def roman_to_int(roman):
        D = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        for i in range(len(roman)):
            if i > 0 and D[roman[i]] > D[roman[i - 1]]:
                number += D[roman[i]] - 2 * D[roman[i - 1]]
            else:
                number += D[roman[i]]
        return number


def main():
    print(roman_to_int("XXXVI"))

if __name__ == '__main__':
    main()
