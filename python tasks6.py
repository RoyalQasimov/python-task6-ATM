import sqlite3

db = sqlite3.connect('bank.db')

sql = db.cursor()


sql.execute(
    """

CREATE TABLE IF NOT EXISTS ATM (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pin INT NOT NULL,
        cash INT NOT NULL
)

"""
)

secim = input("""

(1) Balansi yoxlayin
(2) Mexaric et
(3) Medaxil et
(4) Pini deyisin
(5) Cixis edin
              
              Secim edin: 

 """)



if secim == '1':
    pin = int(input("pin daxil edin: "))
    sql.execute(f"SELECT cash FROM ATM WHERE pin = '{pin}'")
    balans = ''.join(map(str, sql.fetchone()))
    print(balans)



elif secim == '2':
    pin = int(input("pin daxil edin: "))
    mexaric = int(input('Mexaric etmek istediyiniz meblegi daxil edin: '))
    sql.execute(f"UPDATE ATM SET cash = cash - '{mexaric}' WHERE pin = '{pin}'")
    db.commit()


elif secim == '3':
    pin = int(input("pin daxil edin: "))
    medaxil = int(input('Medaxil etmek istediyiniz meblegi daxil edin: '))
    sql.execute(f"UPDATE ATM SET cash = cash + '{medaxil}' WHERE pin = '{pin}'")
    db.commit()


elif secim == '4':
    daxil_et = str(input("Evvelki pini daxil edin: "))
    kohne_pin = sql.execute('SELECT pin FROM ATM')
    pin = ''.join(map(str, sql.fetchone()))

    if daxil_et != pin:
            print('Daxil etdiyiniz pin dogru deyil..')

    elif daxil_et == pin:
        yeni_pin = int(input('Yeni pini daxil edin: '))
        sql.execute(f"UPDATE ATM SET pin = '{yeni_pin}' WHERE pin = '{kohne_pin}'")
        db.commit()
        print("Pin ugurla deyisdirildi")

        