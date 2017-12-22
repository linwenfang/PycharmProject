from functools import reduce
# def splitD(s):
#
def char2num(s):
    digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
def fun(x,y):
    return x*10+y

def str2float(s):
    a=s.split(s)
    f1=reduce(lambda x,y:x*10+y,map(char2num,a[0]))
    f2=reduce(fun,map(char2num,a[1]))/(10*len(a[1]))
    return f1+f2
s='123.456'
#
print(str2float(s))



