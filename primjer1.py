pocetna_pozicija = 0
cilj = 100
trenutna_pozicija = 0
brzina = 20
#potrebno je doći od početne do ciljne pozicije
#upotreba for petlje sa if i elif

for x in range(10): 
    print ("Dobro došli!")
    print("Vaša trenutna pozicija je: ", trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("Stigli ste na cilj!")
        break
    elif trenutna_pozicija > cilj:
        print("Prošli ste cilj!")
        break
    elif trenutna_pozicija < cilj:
        print("Niste još stigli na cilj!")
    trenutna_pozicija += brzina

    
