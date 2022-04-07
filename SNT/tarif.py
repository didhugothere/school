def tarif(age,prix):
  if age <= 5:
    return "Gratuit"
  elif 6 <= age <= 18:
    return prix * 0.75
  elif 19 <= age <= 64:
    return prix
  elif age >= 65:
    return prix * 0.80

iNumPassagers = int(input("Combien de passagers vont participer à cette excursion? "))

if iNumPassagers == 0:
  exit()

iPrix = int(input("Prix plein tarif de l'excursion? (en euros) "))

if iNumPassagers == 1:
  iAge = int(input("Âge du passager? (en années) "))
  print("Tarif total de l'excursion: " + str(tarif(iAge, iPrix)))
else:
  tarifTotal = 0;
  for i in range(iNumPassagers):
    iAge = int(input("Âge du passager " + str(i) + "? (en années) "))
    tarifPassager = tarif(iAge, iPrix)
    print("Tarif pour le passager " + str(i) + ": " + str(tarifPassager))
    if tarifPassager != "Gratuit":
      tarifTotal = tarifTotal + tarifPassager
  print("Tarif total de l'excursion: " + str(tarifTotal))
