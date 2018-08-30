def avsplit(Str, Len):
    fn = len(Str)//Len
    rn = len(Str)%Len
    ar = [fn+1]*rn+ [fn]*(Len-rn)
    si = [i*(fn+1) if i<rn else (rn*(fn+1)+(i-rn)*fn) for i in range(Len)]
    sr = [Str[si[i]:si[i]+ar[i]] for i in range(Len)]
    return sr
