a = float(input())
b = float(input())
c = float(input())
if a <= 0 or b <= 0 or c <= 0:
    print("Khong hop le")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Khong hop le")
else:
    if a == b == c:
        print("Tam giac deu")
    elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        print("Tam giac vuong")
    else:
        print("Tam giac loai khac")