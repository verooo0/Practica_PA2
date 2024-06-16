from pytokr import item
from conjunt_indiv import Cjt_individu
from conjunt_trets import Cjt_trets

instruccio = item()
while instruccio != 'fi':   #mentres instrucció no sigui fi
    if instruccio == 'experiment':
        numero_individu = int(item())
        experiment_actual = Cjt_individu(numero_individu)     #inicialitzar conjunt_individu
        trets_actuals = Cjt_trets(experiment_actual)          #inicialitzar conjunt_trets
        numero_cromosomes = int(item())                       
        print(f"experiment {numero_individu} {numero_cromosomes}")

    elif instruccio == 'afegir_tret':
        tret = item()
        individu_num = int(item())
        print(f"afegir_tret {tret} {individu_num}")
        individu = experiment_actual.obtenir_individu(individu_num)    #assignar a individu la informació de l'individu( número cromosomes) des de la classe cjt_individu
        trets_actuals.afegir_tret(tret, individu, individu_num)        #cridar funcio afegir_tret de classe conjunts_trets
    
    elif instruccio == 'treure_tret':
        tret = item()
        individu_num = int(item())
        individu = experiment_actual.obtenir_individu(individu_num)  #assignar a individu la informació de l'individu( número cromosomes) des de la classe cjt_individu
        print(f"treure_tret {tret} {individu_num}")
        trets_actuals.esborrar_tret(tret, individu_num, individu)     #cridar funcio esborrar_tret de classe conjunts_trets

    elif instruccio == 'consulta_tret':
        nom_tret = item()
        print(f"consulta_tret {nom_tret}")                
        trets_actuals.consulta_tret(nom_tret)            #cridar funcio consulta_tret de classe conjunts_trets
        
    elif instruccio == 'consulta_individu':
        n = int(item())
        print(f"consulta_individu {n}")
        if n < 1 or n > numero_individu:             #si l'individu no existeix dona error 
            print(" error")
        else:                                        
            experiment_actual.consultar_individu(n)            #si l'individu existeix crida la funció consultar_individu de la classe cjt_individu

    elif instruccio == 'distribucio_tret':
        nom_tret = item()
        print(f"distribucio_tret {nom_tret}")
        trets_actuals.distribucio_tret(nom_tret)             #cridar funció distribucio_tret de classe conjunts_trets

    instruccio = item()
    
print("fi")
        


    #instruccio = item()
    
#print("fi")
