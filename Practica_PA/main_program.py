from pytokr import pytokr
from conjunt_indiv import Cjt_individu
from conjunt_trets import Cjt_trets

item = pytokr()
instruccio = item()

while instruccio != 'fi':
    if instruccio == 'experiment':
        #print la instruccio aqui o dentro de las funciones(esto para todas las instrucciones)
        numero_individus = int(item())
        numero_cromosomes = int(item())
        experiment_actual = Cjt_individu(numero_individus)
        trets_actuals = Cjt_trets()
        print(f"experiment {numero_individus} {numero_cromosomes}")
        

    elif instruccio == 'afegir_tret':
        tret = item()
        individu = int(item())
        print(f"afegir_tret {tret} {individu}")
        trets_actuals.afegir_tret(tret,individu, individu)
        experiment_actual.afegir_tret(tret,individu) #o llamar esta funcion dentro de la funcion de cjt_trets
       
    
    elif instruccio == 'treure_tret': # només grups 3 persones
        tret = item()
        individu = int(item())
        #cjt = item()  no se puede leer 3 cosas pq esta ya sera la siguiente instruccion
        print(f"treure_tret {tret} {individu}")
        trets_actuals.esborrar_tret(individu, tret, cjt) #pq tiene tres inputs??
        experiment_actual.esborrar_tret(tret,individu)
        

    elif instruccio == 'consulta_tret':
        nom_tret = item()
        print(f"consulta_tret {nom_tret}")
        trets_actuals.consulta_tret(nom_tret)
        
        
    elif instruccio == 'consulta_individu':
        individu = int(item())
        print(f"consulta_individu {individu}")
        experiment_actual.consultar_individu(individu)
        

    elif instruccio == 'distribucio_tret':
        nom_tret = item()
        print(f"distribucio_tret {nom_tret}")
        trets_actuals.distribucio_tret(nom_tret)
        


    instruccio = item()
    
print("fi")
