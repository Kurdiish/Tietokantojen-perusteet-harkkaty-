import sqlite3

db = sqlite3.connect('kurssit.db')
db.isolation_level = None



while True:
  toiminto = input("Valitse toiminto: ")

  if toiminto == '1':
    vuosi = input('Anna vuosi: ')
    op = db.execute("SELECT SUM(K.laajuus), S.paivays FROM Kurssit K, Suoritukset S WHERE K.id = S.kurssi_id AND paivays LIKE ?",["%"+vuosi+"%"]).fetchone()
    print(f'Opintopisteiden määrä: {op[0]}')

  if toiminto == '2':
    nimi = input('Anna opiskelijan nimi: ')
    suoritukset = db.execute("SELECT K.nimi AS kurssi, K.laajuus, S.paivays, S.arvosana FROM Kurssit K, Suoritukset S, Opiskelijat O WHERE K.id = S.kurssi_id AND O.id = S.opiskelija_id AND O.nimi=? ORDER BY S.paivays DESC LIMIT 2 ",[nimi]).fetchall()
    print(f'kurssit        op        päiväys        arvosana')
    for suoritus in suoritukset:
      print(f'{suoritus[0]}        {suoritus[1]}         {suoritus[2]}     {suoritus[3]}')

  if toiminto == '3':
    nimi = input('Anna kurssin nimi: ').upper()
    jakaumat = db.execute("SELECT S.arvosana,COUNT(K.id) FROM Kurssit K, Suoritukset S WHERE K.id = S.kurssi_id  AND K.nimi = ? GROUP BY S.arvosana",[nimi]).fetchall()
    for jakauma in jakaumat:
      print(f'Arvosana {jakauma[0]}: {jakauma[1]} kpl')
  if toiminto == '5':
    break
    
