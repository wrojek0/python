

def Pr(i=5,j=5):
    if(isinstance(i,int)and isinstance(i,int))and(i>=0 and j>=0):
        if i == 0 and j == 0:
            return 0.5
        elif j == 0:
            return 0
        elif i == 0:
            return 1
        return 0.5*(Pr(i-1,j)+Pr(i,j-1))
    else:
        raise ValueError("Argumentami moga byc tylko wartosci typu int, dodatnie")


def P(i,j):
    if i == 0 and j == 0:
        return 0.5
    elif j == 0:
        return 0
    elif i == 0 :
        return 1
    elif(i<j):
        m=[[0 for k in range(0,j+1)] for l in range(0,j+1)]
    else:
        m = [[0 for k in range(0, i+1)] for l in range(0, i+1)]

    for k in range(i+1):
        m[k][0]=0
        for l in range(j+1):
            m[0][l]=1

    m[0][0]=0.5
    for k in range(1,i+1):
            for l in range(1,j+1):
                m[k][l]=0.5*(m[k-1][l]+m[k][l-1])

    return m[k][l]


import unittest

class test(unittest.TestCase):
    def test(self):
        self.assertEqual(P(3,4),Pr(3,4))
        self.assertEqual(P(7,6),Pr(7,6))



if __name__ == '__main__':
    unittest.main()
