def mySqrt(x):
    if x==0 or x==1: return x
    max = x;
    min = 0;
    q = (min+max)//2;
    print("q value is:",q)
    while(min < max):
        c = q * q;
        print("c value is: ", c)
        if c == x:
            return q;
        elif c < x:
            min = q+1;
        else:
            max=q;
        q=(min+max)//2;
    return q - 1;
print(mySqrt(176))