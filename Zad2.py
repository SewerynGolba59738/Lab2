x = 1
y = 2
z = 3

def zad2(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            print(c,b,a)
        else:
            print(b,c,a)
    elif b >= a and b >= c:
        if c >= a:
            print(a,c,b)
        else:
            print(c,a,b)
    elif c >= a and c >= b:
        if a >= b:
            print(b,a,c)
        else:
            print(a,b,c)

a = zad2(x,y,z)

