import math
a=input("Zadaj stranu a:")
b=input("Zadaj stranu b:")
c=input("Zadaj stranu c:")
a=float(a)
b=float(b)
c=float(c)
if a+b>c and a+c>b and c+b>a:
    if a==b==c:
        print("trojuholník je rovnostranný")
    else:
        if (a==b or a==c or c==b) and (a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a==b*b):
            print("Trojuholník je Rovnsotranný a pravoúhly")
        else:
            if a==b or a==c or b==c:
                print("Trojuholník je rovnoramenny")
            else:
                if a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a==b*b:
                    print("Trojuholník je pravoúhly")
                else:
                    print("Je to trojuholník")
else:
    print("Není to trojuholník")
