# 2026-01-19  13:28:46
import copy
def copy_use():

    a=[1,2,3]
    b=a.copy()
    b[0]=10
    print(a)
    print(b)
def copy_use2():
    a=[1,2]
    b=[3,4]
    c=[a,b]
    d=copy.copy(c)
    print(id(c))
    print(id(d))
    print('-'*50)
    a[0]=10
    print(c)
    print(d)
    print(id(c[0][0]))
    print(id(d[0][0]))
    print('-'*50)
def deepcopy_use():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d=copy.deepcopy(c)
    print(id(c))
    print(id(d))
    print('-'*50)
    a[0] = 10
    print(c)
    print(d)
    print(id(c[0]))
    print(id(d[0]))
    print('-' * 50)



if __name__ == '__main__':
    deepcopy_use()
