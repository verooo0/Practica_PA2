from pytokr import pytokr
from conjunt_indiv import Cjt_individu
from conjunt_trets import Cjt_trets

item = pytokr()
instruccio = item()

while instruccio != 'fi':
    if instruccio == 'experiment':
        #print la instruccio aqui o dentro de las funciones(esto para todas las instrucciones)
        numero_individu = int(item())
        numero_cromosomes = int(item())
        experiment_actual = Cjt_individu(numero_individu)
        trets_actuals = Cjt_trets()
        

    elif instruccio == 'afegir_tret':
        tret = item()
        individu = int(item())

        trets_actuals.afegir_tret(tret,individu, individu)
        experiment_actual.afegir_tret(tret,individu) #o llamar esta funcion dentro de la funcion de cjt_trets
    
    elif instruccio == 'treure_tret': # només grups 3 persones
        tret = item()
        individu = int(item())
        cjt = item()
        trets_actuals.esborrar_tret(individu, tret, cjt)
        experiment_actual.esborrar_tret(tret,individu)

    elif instruccio == 'consulta_tret':
        nom_tret = item()
        trets_actuals.consulta_tret(nom_tret)
        
    elif instruccio == 'consulta_individu':
        n = int(item())
        experiment_actual.consultar_individu(n)

    elif instruccio == 'distribucio_tret':
        nom_tret = item()
        trets_actuals.distribucio_tret(nom_tret)


    instruccio = item()
    
print("fi")
