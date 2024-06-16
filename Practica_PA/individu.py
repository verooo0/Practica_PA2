from parcrom import Parcrom

class individu: 
    def __init__(self, crom): 
        self.__parcrom = Parcrom(crom)
        self.__trets = set()
        self.__cromosomes = crom
    
    def consultar_tret(self, a): 
        return a in self.__trets
    
    def afegir_tret(self, a): 
        self.__trets.add(a)
    
    def esborrar_tret(self, a): 
        self.__trets.remove(a)

    def cromosomes(self): 
        return self.__parcrom
    
    def llegir_individu(self, n): 
        self.__parcrom.llegir_cromosoma(n)
    
    def crom(self): 
        return self.__cromosomes

    def escriure_ind(self): 
        self.__parcrom.escriure_parcrom()
        ll = list(self.__trets)
        if ll is not None: 
            ll.sort()
            for e in ll: 
                print('  ', e, sep = '')    
