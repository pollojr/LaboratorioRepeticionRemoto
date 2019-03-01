p=0
c=0
n=0
for a in range(0,10):
    a=int(input("ingrese el numero"))
    if a==0:
            c=c+1
    else:
        if a<0:
            p=p+1
        else:
            n=n+1
print("los numeros positivos son:{}".format(p))
print("los numeros ceros son:{}".format(c))
print("los numeros negativos son:{}".format(n))
    
    

