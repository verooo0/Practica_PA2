from parcrom import Parcrom
class Cjt_trets:   
    class _tretsstr: 
        def __init__(self, cromosomes): 
            self._parcrom = Parcrom(cromosomes)
            self._individus = set()
            
    def __init__(self, conjunt_individus): 
        self.__trets = dict()
        self.__conjunt_individus = conjunt_individus

    def afegir_tret(self, a, ind, n): 
        cromosomes = ind.cromosomes() 
        if a in self.__trets: 
            if n in self.__trets[a]._individus:
                print("  error")
            else:
                self.__trets[a]._individus.add(n)
                self.__trets[a]._parcrom.interseccio_tret(cromosomes)
        else: 
            elem = self._tretsstr(ind.crom())
            elem._individus.add(n)
            self.__trets[a] = elem
        ind.afegir_tret(a)


    def esborrar_tret(self, p, n, ind): 
        if not p in self.__trets:  # Si el tret no existe
            print("  error")
        else:  # Si el tret existe
            if not n in self.__trets[p]._individus:  # Si el individuo no tiene el tret
                print("  error")
            else:  # Si el individuo tiene el tret
                self.__trets[p]._individus.remove(n)
                ind.esborrar_tret(p)
                if len(self.__trets[p]._individus) == 0:
                    del self.__trets[p]
                else:
                    self.__trets[p]._parcrom.reiniciar() 
                    for ind_num in self.__trets[p]._individus:
                        individu_obj = self.__conjunt_individus.obtenir_individu(ind_num)
                        self.__trets[p]._parcrom.interseccio_tret(individu_obj.cromosomes())
