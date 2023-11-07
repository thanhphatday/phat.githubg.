n=int(input("n="))
i=1
s=1
while n>=0 or n<=100:
    if n==0:
        print("0!=1")
else:
    while i<=n:
        s=s*i
        i=i+1
print(f'{n}!={s}')        
        
        
        
    