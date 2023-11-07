M1 = int(input("M1="))
M2 = int(input("M2="))
M3 = int(input("M3="))
S = int(input("S="))
T = 0
if S <= 100:
  T = S * M1
elif S <= 150:
  T = S * M2
else:
  T = S * M3
print("Phai tra=", T, sep="")