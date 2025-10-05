a=int(input("Zadaj číslo:"))
if a/4 == a//4 and a/7 == a//7:
    print("je delitelné aj 7 a aj 4")
elif  a/4 == a//4:
    print("je delitelné 4")
elif a/7 == a//7:
    print("je delitelné 7")
else:
    print("není delitelné ani 7 a ani 4")