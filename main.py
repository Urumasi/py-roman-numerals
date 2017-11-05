def test(fn, input=[], output=[]):
    passed = True
    for k, v in enumerate(input):
        fv = fn(v)
        if fv!=output[k]:
            return (False, k, (fv, output[k]))
    return (True,)


def rinc(s):
    chars = "IVXLCDM"
    return ''.join([chars[chars.index(c)+2] for c in s])

def roman(n):
    if n>=10:
        return rinc(roman(n//10)) + roman(n%10)
    if n<=3: return 'I'*n
    elif n<=8: return 'I'*(5-n)+'V'+'I'*(n-5)
    return 'IX'

if __name__=="__main__":
    print(test(roman, [1  , 2   , 3    , 4   , 5  , 6   , 7    , 8     , 9   , 10 , 50 , 100, 500, 1000],
                      ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'L', 'C', 'D', 'M']))
                      
    print(test(roman, [1830      , 295    , 964     , 1233       , 969     , 2189],
                      ['MDCCCXXX', 'CCXCV', 'CMLXIV', 'MCCXXXIII', 'CMLXIX', 'MMCLXXXIX']))
