import math
a=input("Zadaj spodnú hranicu intervalu:")
b=input("Zadaj hornú hranicu intervalu:")
x=input("Zadaj číslo:")
x=int(x)
a=int(a)
b=int(b)
if a<=x<=b:
    print("Čislo patrí do intervalu")
else:
    print("číslo nepatrí do intervalu")