nr=int(input("numarul este"))
s=0
for a in range(1,nr+1):
    if a%3==0 or a%5==0:
        s=s+a
print("suma =",s)