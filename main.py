from mahalliy import maxaliy_qatnovlar
from xalqaro import xalqaro_samolyot_qatnovlar
import random
from datetime import datetime, timedelta
import os

class Airport:
  
  def mahalliy_reys(self, manzil):
    os.system('clear')
    for key, value in maxaliy_qatnovlar.items():
      if manzil.lower() == value['manzil'].lower():
        if value['biletlar_soni'] != 0:
          print(f"Aviokompaniya nomi: {value['aviakompaniya']}")
          print(f"Samalyot nomi: {value['air_name']}")
          print(f"Manzil: {value['manzil']}")
          print(f"Yolovchilar soni: {value['yolovchi']}")
          print(f"Uchish davomiyligi: {value['vaqti']}")
          print(f"Biletlar soni: {value['biletlar_soni']}")
          print(f"Biletlar narxi: {value['bilet_narxi']} so'm\n")
          ism = input("Ismingizni kiriting: ")
          familiya = input("Familiyangizni kiriting: ")
          bilet_nom = ''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ123456789', k=6))
          uchish_san = datetime.now() + timedelta(days=random.randint(1, 30))
          uchish_san = uchish_san.strftime('%Y-%m-%d\n')
          os.system('clear')
          print('-'*(40))
          print("Bilet tasdiqlandi!")
          k['biletlar_soni']-=1
          print(f"Bilet raqami: {bilet_nom}")
          print(f"Ism: {ism}")
          print(f"Familiya: {familiya}")
          print(f"Uchish sanasi: {uchish_san}")
          print('-'*(40))
          break
        else:
          print("Siz qidirgan manzil uchun biletlar tugagan.")
    else:
        print("Siz qidirgan manzil uchun reyslar mavjud emas")

  
  def xalqaro_reys(self, manzil):
    os.system('clear')
    for key, value in xalqaro_samolyot_qatnovlar.items():
      if manzil.lower() == value['mamlakat'].lower():
        if value['bilet'] != 0:
          print(f"Aviokompaniya nomi: {value['aviakompaniya']}")
          print(f"Mamlakati: {value['mamlakat']}")
          print(f"Telefon raqami: {value['telefon']}")
          print(f"Yolovchilar soni: {value['yolovchi_soni']}")
          print(f"Biletlar soni: {value['bilet']}")
          print(f"Biletlar narxi: {value['bilet_narxi']} so'm\n")
          ism = input("Ismingizni kiriting: ")
          familiya = input("Familiyangizni kiriting: ")
          bilet_nom = ''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ123456789', k=6))
          uchish_san = datetime.now() + timedelta(days=random.randint(1, 30))
          uchish_san = uchish_san.strftime('%Y-%m-%d\n')
          os.system('clear')
          print('-'*(40))
          print("Bilet tasdiqlandi!")
          value['bilet']-=1
          print(f"Bilet raqami: {bilet_nom}")
          print(f"Ism: {ism}")
          print(f"Familiya: {familiya}")
          print(f"Uchish sanasi: {uchish_san}")
          print('-'*(40))
          break
        else:
          print("Siz qidirgan manzil uchun biletlar tugagan.")
    else:
        print("Siz qidirgan manzil uchun reyslar mavjud emas")

while True:
  tanlov = input("[1] Mahalliy qatnovlar\n[2] Xalqaro qatnovlar\n>>> ")
  if tanlov == '1':
    manzil = input("Manzil kiriting: ")
    Airport().mahalliy_reys(manzil)
  elif tanlov == '2':
    manzil = input("Manzil kiriting: ")
    Airport().xalqaro_reys(manzil)