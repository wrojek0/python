
def createMeasure(length):
    step = "|...."
    measure = ""
    numbers = ""

    for i in range(length):
        measure+=step
        if i == length-1:
            measure+="|"

    for i in range(length):
        if i == 0:
            numbers=str(i)+"    "+str(i+1)
        elif i<9:
            numbers=numbers+"    "+str(i+1)
        elif i<99:
            numbers=numbers+"   "+str(i+1)
        elif i<999:
            numbers=numbers+"  "+str(i+1)
        elif i<9999:
            numbers=numbers+" "+str(i+1)

    print(measure)
    print(numbers)

def main():
    createMeasure(15)


if __name__ == '__main__':
    main()
