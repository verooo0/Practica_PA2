from parcrom import Parcrom

class individu: 
    def __init__(self, crom): 
        self.__parcrom = Parcrom(crom)            #inicialitza la classe Parcrom
        self.__trets = set()                      #crea set() per als trets
        self.__cromosomes = crom
    
    def consultar_tret(self, a): 
        return a in self.__trets                    #retorna els trets per comprobar que existeixen 
    
    def afegir_tret(self, a): 
        self.__trets.add(a)                        #afegeix el tret al set()
    
    def esborrar_tret(self, a): 
        self.__trets.remove(a)                     #elimina el tret del set()

    def cromosomes(self): 
        return self.__parcrom                      #retorna el par de cromosomes des de la classe Parcrom
    
    def crom(self): 
        return self.__cromosomes                   #retorna els cromosomes

    def escriure_ind(self): 
        self.__parcrom.escriure_parcrom()            #crida al mètode escriure_parcrom de la classe Parcrom
        ll = list(self.__trets)                      #crea una llista dels trets que té l'individu i els escriu si en té
        if ll is not None: 
            ll.sort()
            for e in ll: 
                print('  ', e, sep = '')    
