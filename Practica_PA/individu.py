from parcrom import Parcrom

class individu: 
    def __init__(self, crom): 
        self.__parcrom = Parcrom(crom)
        self.__trets = set()
    
    def consultar_tret(self, t): 
        return t in self.__trets
    
    def afegir_tret(self, t): 
        self.__trets.add(t)
    
    def esborrar_tret(self, t): 
        self.__trets.remove(t)

    def cromosomes(self): 
        return self.__parcrom
    
    def llegir_individu(self, n): 
        self.__parcrom.llegir_cromosoma(n)

    def escriure_ind(self): 
        self.__parcrom.escriure_parcrom()
        ll = list(self.__trets)
        if ll is not None: 
            ll.sort()
            for e in ll: 
                print('  ', e, sep = '')
    
