n = int(input("n="))
if n < 0 or n > 100:
    print("0<=n<=100")
    exit()
s = 1
i = 1
while i <= n:
    s *= i
    i += 1
print(f"{n}!={s}")