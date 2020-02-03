import haravasto
import random
import time
import datetime
import os

def menu():
    print("Mitä haluat tehdä? \nPelaa: P\nTilastot: T\nLopeta: L")
    while True:
        try:
            valinta = str(input("Valitse (P)elaa, (T)ilastot, (L)opeta: \n"))
        except ValueError:
            print("Ei sallittu valinta.")
            pass
        else:
            if (valinta == "p"):
                print("pelaa")
                valinta = "pelaa"
                break
            if (valinta == "t"):
                print("tilastot")
                valinta = "tilastot"
                break
            if (valinta == "l"):
                print("lopeta")
                valinta = "lopeta"
                break
            else:
                print("Ei sallittu valinta.")
                time.sleep(1)
                pass
    return valinta

def tallenna(tiedosto, w_l):
    try:
        with open(tiedosto, "a") as kohde:
            datetime_info = datetime.datetime.now()
            stop_time = datetime.datetime.now().time()
            t1_m = start_time.strftime("%M")
            t2_m = stop_time.strftime("%M")
            game_lenght = ("{t3_m}".format(t3_m=int(t2_m) - int(t1_m)))
            kohde.write("{w_l} : {datetime_info} Pelin kesto:{game_lenght} min Liikkujen määrä: {liikkujen_maara} Kentän koko {leveys}x{korkeus} Miinojen määrä: {miinat}\n".format(w_l=w_l, datetime_info=datetime_info.strftime("%d.%m.%y"), 
            game_lenght=game_lenght, liikkujen_maara=liikkujen_maara, leveys=leveys, korkeus=korkeus, miinat=miinat))
    except IOError:
        print("Kohdetiedostoa ei voitu avata. Tallennus epäonnistui")

def tilastot(tiedosto):
    try:
        with open(tiedosto) as lahde:
            print(lahde.read())

    except FileNotFoundError:
        print("Ei tallennettuja tilastoja.")
        time.sleep(1)

def havio():
    rajahdys = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____\nOsuit miinaan. Hävisit pelin."""
    print(rajahdys)
    time.sleep(3)
    haravasto.lopeta()
    tallenna("miinaharava_tallennukset.txt", "L")
    os.system("cls")

def voitto():
    victory_flag =  """
   __
  <__>
   ||______________________________
   ||######   #####################|
   ||######   #####################|
   ||######   #####################|
   ||######   #####################|
   ||                              |
   ||######   #####################|
   ||######   #####################|
   ||######   #####################|
   ||######   #####################|
   ||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   ||
   || Vältit kaikki miinat. Voitit pelin.
   ||
   ||   
   """
    
    voitit = True
    for x in range(len(sotakentta[0])):
        for y in range(len(sotakentta)):
            if miinakentta[y][x] == "x":
                pass
            else:
                if miinakentta[y][x] == sotakentta[y][x]:
                    pass
                else:
                    voitit = False
                    break
        if voitit == False:
            break
    if voitit == True:
        print(victory_flag)
        time.sleep(3)
        haravasto.lopeta()
        tallenna("miinaharava_tallennukset.txt", "W")
        os.system("cls")

def alusta_peli():
    global leveys
    global korkeus
    global miinat

    while True:
        try:
            kentan_leveys = int(input("Valitse kentän leveys: "))
            kentan_korkeus = int(input("Valitse kentän korkeus: "))
            miinojen_maara = int(input("Valitse miinojen määrä: "))
        except ValueError:
            print("Ei sallittu valinta.")
            pass
        else:
            if miinojen_maara > kentan_korkeus * kentan_leveys:
                print("Miinojen määrä ei voi ylittää kentän kokoa.")
                pass
            else:
                leveys = kentan_leveys
                korkeus = kentan_korkeus
                miinat = miinojen_maara
                break
    return kentan_leveys, kentan_korkeus, miinojen_maara

def laske_miinat(x, y, list):
    x_max = len(list[0]) - 1
    y_max = len(list) - 1
    viereisten_miinojen_maara = 0
    for n in range(3):
        for m in range(3):
            try:
                if (list[(y - 1) + n][(x - 1) + m] == "x"):
                    if (((x - 1) + m > x_max) or ((y - 1) + n > y_max)):
                        pass
                    elif(((x - 1) + m < 0) or ((y - 1) + n < 0)):
                        pass
                    else:
                        viereisten_miinojen_maara += 1
            except IndexError:
                pass
    return viereisten_miinojen_maara

def luo_kentta():
    miinakentta = []
    sotakentta = []

    kentan_leveys, kentan_korkeus, miinojen_maara = alusta_peli()

    for rivi in range(kentan_korkeus):
        miinakentta.append([])
        for sarake in range(kentan_leveys):
            miinakentta[-1].append(" ")
    
    jaljella = []
    for x in range(kentan_leveys):
        for y in range(kentan_korkeus):
            jaljella.append((x, y))
    
    for i in range(miinojen_maara):
        list_len = len(jaljella)
        miina = jaljella.pop(random.randint(0, list_len - 1))
        x = miina[0]
        y =  miina[1]
        miinakentta[y].pop(x)
        miinakentta[y].insert(x, "x")
    
    for y in range(len(miinakentta)):
        for x in range(len(miinakentta[0])):
            if (miinakentta[y][x] == "x"):
                pass
            else:
                viereisten_miinojen_maara = laske_miinat(x, y, miinakentta)
                miinakentta[y].pop(x)
                miinakentta[y].insert(x, str(viereisten_miinojen_maara))
    
    for rivi in range(kentan_korkeus):
        sotakentta.append([])
        for sarake in range(kentan_leveys):
            sotakentta[-1].append(" ")
    return miinakentta, sotakentta

def tulvatäyttö(miinakentta, x, y):
    tunnetut = [(x, y)]

    while True:
        x_max = len(miinakentta[0]) - 1
        y_max = len(miinakentta) - 1
    
        try:
            x, y = tunnetut.pop()
        except IndexError:
            break

        sotakentta[y].pop(x)
        sotakentta[y].insert(x, "0")
        
        for n in range(3):
            for m in range(3):
                try:
                    if ((miinakentta[(y - 1) + n][(x - 1) + m] != "x") and (sotakentta[(y - 1) + n][(x - 1) + m] == " ")):
                        if int(miinakentta[(y - 1) + n][(x - 1) + m]) >= 1:
                            if (((x - 1) + m > x_max) or ((y - 1) + n > y_max)):
                                pass
                            elif(((x - 1) + m < 0) or ((y - 1) + n < 0)):
                                pass
                            else:
                                sotakentta[(y - 1) + n].pop((x - 1) + m)
                                sotakentta[(y - 1) + n].insert((x - 1) + m, str(miinakentta[(y - 1) + n][(x - 1) + m]))
                        else:
                            if (((x - 1) + m > x_max) or ((y - 1) + n > y_max)):
                                pass
                            elif(((x - 1) + m < 0) or ((y - 1) + n < 0)):
                                pass
                            else:
                                tunnetut.append(((x - 1) + m, (y - 1) + n))
                except IndexError:
                    pass

def kasittele_hiiri(x, y, painike, muokkausnappaimet):
    global liikkujen_maara
    painikkeet = {haravasto.HIIRI_VASEN : "vasen",
    haravasto.HIIRI_KESKI : "keski",
    haravasto.HIIRI_OIKEA : "oikea"}

    if (painike == 1):
        painike = painikkeet[haravasto.HIIRI_VASEN]
    if (painike == 2):
        painike = painikkeet[haravasto.HIIRI_KESKI]
    if (painike == 4):
        painike = painikkeet[haravasto.HIIRI_OIKEA]
    
    x = int(x / 40)
    y = int((len(miinakentta)) - y/40)

    if painike == "vasen":
        if sotakentta[y][x] == "f":
            print("Lippu pitää poistaa ennen kuin voit avata ruudun.")
        else:
            if miinakentta[y][x] == "x":
                sotakentta[y].pop(x)
                sotakentta[y].insert(x, "x")
                liikkujen_maara += 1
                havio()
            if miinakentta[y][x] == "0":
                tulvatäyttö(miinakentta, x, y)
                liikkujen_maara += 1
                voitto()
            try:
                if int(miinakentta[y][x]) >= 1:
                    sotakentta[y].pop(x)
                    sotakentta[y].insert(x, str(miinakentta[y][x]))
                    liikkujen_maara += 1
                    voitto()
            except ValueError:
                pass
    
    if painike == "oikea":
        if sotakentta[y][x] == "f":
            sotakentta[y].pop(x)
            sotakentta[y].insert(x, " ")
            print("Poistit lipun.")
            liikkujen_maara += 1
        else:
            sotakentta[y].pop(x)
            sotakentta[y].insert(x, "f")
            print("Asetit lipun.")
            liikkujen_maara += 1

def piirra_kentta():
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    for x in range(len(sotakentta[0])):
        for y in range(len(sotakentta)):
            avain = sotakentta[(len(sotakentta) - 1) - y][x]
            x_1 = x * 40
            y_1 = y * 40
            haravasto.lisaa_piirrettava_ruutu(avain, x_1, y_1)
    haravasto.piirra_ruudut()

def main():
    kentan_leveys = len(miinakentta[0]) * 40
    kentan_korkeus = len(miinakentta) * 40
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(kentan_leveys, kentan_korkeus)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()



if __name__ == "__main__":
    while True:
        valinta = menu()
        if valinta == "pelaa":
            liikkujen_maara = 0
            leveys = 0
            korkeus = 0
            miinat = 0
            miinakentta, sotakentta = luo_kentta()
            start_time = datetime.datetime.now().time()
            main()
        if valinta == "tilastot":
            tilastot("miinaharava_tallennukset.txt")
            pass
        if valinta == "lopeta":
            break
