T=int(input())
L=int(input())
H=int(input())
Dtb=((T*2)+(L*3)+H)/6
if Dtb<3:
    print("Kem")
elif (Dtb<5) and (Dtb>=3):
    print("Yeu")
elif (Dtb>=5) and (Dtb<6):
    print("Trung binh")
elif (Dtb>=6) and (Dtb<7):
    print("Trung binh kha")
elif (Dtb>=7) and (Dtb<8):
    print("Kha")
elif (Dtb<=8) and (Dtb<9):
    print("Gioi")
else:
    (Dtb>=9) and (Dtb<10)
    print("Xuat sac")
    