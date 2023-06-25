maxaliy_qatnovlar = {1: {"air_name": 'Airbus A300',
                         'aviakompaniya': 'Uzbkeistan Airways',
                         'manzil': "Qo'qon",
                         'yolovchi': 140,
                         'vaqti': "2:10",
                         'bilet_narxi': 540000,
                         'biletlar_soni': 100 
                        },
                    2: {"air_name": 'Airbus A310',
                         'aviakompaniya': 'Qanot Sharq',
                         'manzil': "Xiva",
                         'yolovchi': 210,
                         'vaqti': "5:25",
                         'bilet_narxi': 1040000,
                         'biletlar_soni': 35 
                        },
                    3: {"air_name": 'Airbus A330',
                        'aviakompaniya': 'Uzbkeistan Airways',
                         'manzil': "Nukus",
                         'yolovchi': 160,
                         'vaqti': "5:55",
                         'bilet_narxi': 1240000,
                         'biletlar_soni': 75 
                        },
                    4: {"air_name": 'Airbus A340',
                        'aviakompaniya': 'Qanot Sharq',
                         'manzil': "Namangan",
                         'yolovchi': 140,
                         'vaqti': "1:25",
                         'bilet_narxi': 455000,
                         'biletlar_soni': 20 
                        },
                    5: {"air_name": 'Airbus A340',
                        'aviakompaniya': 'Uzbkeistan Airways',
                         'manzil': "Andijon",
                         'yolovchi': 140,
                         'vaqti': "1:55",
                         'bilet_narxi': 555000,
                         'biletlar_soni': 20 
                        },
                     6: {"air_name": 'Airbus A340',
                        'aviakompaniya': 'Qanot Sharq',
                         'manzil': "Qarshi",
                         'yolovchi': 170,
                         'vaqti': "2:25",
                         'bilet_narxi': 755000,
                         'biletlar_soni': 59 
                        },
                     7: {"air_name": 'Airbus A340',
                        'aviakompaniya': 'Uzbkeistan Airways',
                         'manzil': "Trmiz",
                         'yolovchi': 240,
                         'vaqti': "3:25",
                         'bilet_narxi': 855000,
                         'biletlar_soni': 61 
                        },
                     8: {"air_name": 'Airbus A340',
                        'aviakompaniya': 'Qanot Sharq',
                         'manzil': "Navoiy",
                         'yolovchi': 120,
                         'vaqti': "4:25",
                         'bilet_narxi': 764000,
                         'biletlar_soni': 60 
                        },
                     9: {"air_name": 'Airbus A340',
                        'aviakompaniya': 'Uzbkeistan Airways',
                         'manzil': "Jizzax",
                         'yolovchi': 140,
                         'vaqti': "1:45",
                         'bilet_narxi': 580000,
                         'biletlar_soni': 8 
                        }
                    }
def get_bilet_maxalliy():
  for m, i in maxaliy_qatnovlar.items():
    print(f"Aviokompaniya nomi: {i['aviakompaniya']}")
    print(f"Samalyot nomi: {i['air_name']}")
    print(f"Manzil: {i['manzil']}")
    print(f"Yolovchilar soni: {i['yolovchi']}")
    print(f"Uchish davomiyligi: {i['vaqti']}")
    print(f"Biletlar soni: {i['biletlar_soni']}")
    print(f"Biletlar narxi: {i['bilet_narxi']} so'm\n")
