# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:52:01 2022

@author: HP
"""
# def yosh_hisobla(ism,t_yil):
#     """ Foydalanuvchining tug`ilgan kunini chiqaruvchi dastur"""
#     print(f"{ism.title()} siz {2022-t_yil}-yilda tug`ilgansiz")
# yosh_hisobla('Xojiakbar', 20)

# def kvadrat(kvadrat):
#     """Kiritilgan sonning kvadratini va kubini qaytaruvchi dastur"""
#     print(f"Sonning Kvadrati: {kvadrat**2}\n"
#           f"Sonning kubi {kvadrat**3}")
# kvadrat(4)
# print(kvadrat.__doc__)
# print(range.__doc__)
# def son_tekshir(son):
#     if son%2 == 0:
#         print("Bu son juft")
#     else:
#         print("Bu son toq")
# son_tekshir(4)
# def son_solishtirish():
#  """Sonlarni solishtiruvchi funksiya"""
#     x = int(input("Son kiriting:"))
#     y = int(input("Son kiriting:"))
#     if x>y:
#         print(f"{x}>{y}")
#     elif y>x:
#         print(f"{y}>{x}")
#     else:
#         print(f"{x}={y}")
# son_solishtirish()

# def daraja_hisobla(x,n=2):
#     print(f"{x} ning {n} i darajasi {x**n} ga teng")
# daraja_hisobla(5)
def bolinma_tekshir(son):
    for i in range(1,11):
        if son%i == 0:
            print(i)
    print("Kiritilgan son shu sonlarga qoldiqsiz bo`linadi")
bolinma_tekshir(son=int(input("Son kirit")))