# -*- coding: utf-8 -*-
def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)

sayi = int(input("Bir sayı girin: "))
print(f"{sayi} sayısının faktoriyeli: {faktoriyel(sayi)}")
