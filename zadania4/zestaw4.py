#4.2
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

    measure+='\n'+numbers
    return measure
#4.2
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
    return rectangle

#4.3
def factorial(n):
    if n == 1 or n == 0:
        return 1
    res = 1;
    while n>0:
        res*=n
        n-=1
    return res



#4.4
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1

    while n-1>0:
        c=a+b
        a,b = b,c
        n=n-1
    return c
#4.5
def odwracanie(L,left,right):
    if right<left:
        left,right = right,left
    while( left < right ):
        L[right],L[left]=L[left],L[right]
        left+=1
        right-=1
    return L

def odwracanieR(L,left,right):
    if left<=right:
        L[right],L[left]=L[left],L[right]
        return odwracanieR(L,left+1,right-1)
    else:
        return L

#4.6
def sum_seq(sequence):
    sum = 0
    for i in sequence:
        if isinstance(i,(list,tuple)):
            sum+=sum_seq(i)
        else:
            sum+=i

    return sum

#4.7
def flatten(sequence):
    res = []
    for i in sequence:
        if isinstance(i,(list,tuple)):
            res+=flatten(i)
        else:
            res.append(i)

    return res










def main():
    list = [1,2,3,4,5,6]
    list1 = [1,2,3,4,5,6]
    list2 = [1,2,3,4,5,6,7,8]
    sum = [1,2,3,[1,2,[4,5,6]],(1,1,(2,2))]
    seq = [1,2,3,[4,[5,6],[7,8]],(9,(10,11))]
    seq2 = (1,(((2,3,4)),5,(6,7,8,9),[10]))


    assert factorial(4) ==  24
    assert factorial(5) == 120
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert odwracanie(list,0,5) == [6,5,4,3,2,1]
    assert odwracanie(list1,0,3) == [4,3,2,1,5,6]
    assert odwracanieR(list2,0,7) == [8,7,6,5,4,3,2,1]
    assert sum_seq(sum) == 30
    assert flatten(seq) == [1,2,3,4,5,6,7,8,9,10,11]
    assert flatten(seq2) == [1,2,3,4,5,6,7,8,9,10]











if __name__ == '__main__':
    main()
