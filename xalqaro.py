xalqaro_samolyot_qatnovlar = {
    1: {
        "aviakompaniya": "Uzbekistan Airways",
        "mamlakat": "O'zbekiston",
        "telefon": "+998 71 200 00 55",
        "yolovchi_soni": 120,
        "bilet": 200,
        "bilet_narxi": 5670000
    },
    2: {
        "aviakompaniya": "Turkish Airlines",
        "mamlakat": "Turkiya",
        "telefon": "+90 212 444 08 49",
        "yolovchi_soni": 300,
        "bilet": 5,
        "bilet_narxi": 4540000
    },
    3: {
        "aviakompaniya": "Emirates",
        "mamlakat": "Birlashgan Arab Amirliklari",
        "telefon": "+971 600 55 55 55",
        "yolovchi_soni": 500,
        "bilet": 154,
        "bilet_narxi": 1540000
    },
    4: {
        "aviakompaniya": "Lufthansa",
        "mamlakat": "Germaniya",
        "telefon": "+49 69 86 799 799",
        "yolovchi_soni": 400,
        "bilet": 304,
        "bilet_narxi": 3490000
    },
    5: {
        "aviakompaniya": "Air France",
        "mamlakat": "Fransiya",
        "telefon": "+33 1 41 56 78 00",
        "yolovchi_soni": 350,
        "bilet": 23,
        "bilet_narxi": 2390000
    }
}

def get_bilet_xalqaro():
  for m, i in xalqaro_samolyot_qatnovlar.items():
    print(f"Aviokompaniya nomi: {i['aviakompaniya']}")
    print(f"Mamlakati: {i['mamlakat']}")
    print(f"Telefon raqami: {i['telefon']}")
    print(f"Yolovchilar soni: {i['yolovchi_soni']}")
    print(f"Biletlar soni: {i['bilet']}")
    print(f"Biletlar narxi: {i['bilet_narxi']} so'm\n")
