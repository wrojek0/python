
def add_frac(frac1, frac2):             # frac1 + frac2
    res = []
    if frac1[1] == frac2[1]:
        res.append(frac1[0]+frac2[0])
        res.append(frac1[1])
        reduce(res)
        return res
    else:
        common_denominator(frac1,frac2)
        res.append(frac1[0]+frac2[0])
        res.append(frac1[1])
        reduce(res)
        return res
    return res

def sub_frac(frac1, frac2):             # frac1 - frac2
    res = []
    if frac1[1] == frac2[1]:
        res.append(frac1[0]-frac2[0])
        res.append(frac1[1])
        reduce(res)
        return res
    else:
        common_denominator(frac1,frac2)
        res.append(frac1[0]-frac2[0])
        res.append(frac1[1])
        reduce(res)
        return res


def mul_frac(frac1, frac2):             # frac1 * frac2
    res = []
    res.append(frac1[0]*frac2[0])
    res.append(frac1[1]*frac2[1])
    reduce(res)
    return res


def div_frac(frac1, frac2):             # frac1 / frac2
    res = []
    res.append(frac1[0]*frac2[1])
    res.append(frac1[1]*frac2[0])
    reduce(res)
    return res

def is_positive(frac):                  # bool, czy dodatni
    if (frac[0] * frac[1]) > 0:
        return True
    else:
        return False

def is_zero(frac):                      # bool, typu [0, x]
    if frac[0] == 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):             # -1 | 0 | +1
    common_denominator(frac1,frac2)
    if frac1[0]< frac2[0]:
        return -1
    elif frac1[0]> frac2[0]:
        return 1
    else:
        return 0

def frac2float(frac):                 # konwersja do float
    f = frac[0]/frac[1]
    return f






###################################################################
#funkcja sprowadza 2 ulamki do wspolnego mianownika
def common_denominator(frac1,frac2):
    if( frac1[1] == frac2[1] ):
        return True
    else:
        frac1[0]*=frac2[1]
        frac2[0]*=frac1[1]
        frac1[1]*=frac2[1]
        frac2[1]=frac1[1]
        return True

#redukcja ulamka do najprostszej postaci
def reduce(frac):
    if frac[0] > frac[1]:
        larger = frac[0]
    else:
        larger = frac[1]

    i = 1
    while i<=larger:
        if frac[0] % i == 0 and frac[1] % i == 0:
            nwd = i
        i+=1

    if nwd != 0:
        frac[0] /= nwd
        frac[1] /= nwd
###################################################################
