from pytokr import item
from conjunt_indiv import Cjt_individu
from conjunt_trets import Cjt_trets

instruccio = item()
while instruccio != 'fi':
    if instruccio == 'experiment':
        numero_individu = int(item())
        experiment_actual = Cjt_individu(numero_individu)
        trets_actuals = Cjt_trets(experiment_actual)
        numero_cromosomes = int(item())
        print(f"experiment {numero_individu} {numero_cromosomes}")

    elif instruccio == 'afegir_tret':
        tret = item()
        individu_num = int(item())
        print(f"afegir_tret {tret} {individu_num}")
        individu = experiment_actual.obtenir_individu(individu_num)
        trets_actuals.afegir_tret(tret, individu, individu_num)
    
    elif instruccio == 'treure_tret':
        tret = item()
        individu_num = int(item())
        individu = experiment_actual.obtenir_individu(individu_num)
        print(f"treure_tret {tret} {individu_num}")
        trets_actuals.esborrar_tret(tret, individu_num, individu)

    elif instruccio == 'consulta_tret':
        nom_tret = item()
        print(f"consulta_tret {nom_tret}")
        trets_actuals.consulta_tret(nom_tret)
        
    elif instruccio == 'consulta_individu':
        n = int(item())
        print(f"consulta_individu {n}")
        if n < 1 or n > numero_individu: 
            print(" error")
        else: 
            experiment_actual.consultar_individu(n)

    elif instruccio == 'distribucio_tret':
        nom_tret = item()
        print(f"distribucio_tret {nom_tret}")
        trets_actuals.distribucio_tret(nom_tret)

    instruccio = item()
    
print("fi")
        


    instruccio = item()
    
print("fi")
