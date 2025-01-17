class Bil:
    def __init__(self, merke, modell, årsmodell, hestekrefter, tank_strl):
        self.merke = merke
        self.modell = modell
        self.årsmodell = årsmodell
        self.hestekrefter = hestekrefter
        self.tank_strl = tank_strl


    def min_bil(self):
        print(f"Min bil er en {self.merke} {self.modell} ({self.årsmodell}-modell)")

    def tanken(self):
        print(f"Min bil har en tank som er {self.tank_strl} liter stor")

#Oppretter et objekt som passer inn i klassen
min_egen_bil = Bil("Toyota", "MR2","2002","193", "42")

min_egen_bil.min_bil()
min_egen_bil.tanken()