
def drawRectangle(height,width):
    h = "+---+"
    v = "|   |"

    if height == 0 or width == 0:
        return
    for i in range(width):
        if i == 0:
            gora = h
            bok = v
        elif i>0:
            gora+=h[1:]
            bok+=v[1:]

    rectangle = gora + "\n" + bok + "\n" + gora
    module = bok+ "\n" +gora
    # print(rectangle)
    # print(module)


    for j in range(height-1):
            rectangle+="\n"+module
    print(rectangle)

def main():
    drawRectangle(3,5)



if __name__ == '__main__':
    main()
