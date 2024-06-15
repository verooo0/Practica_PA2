from arbre_binari_amb_nodes import ArbreBinari
from parcrom import Parcrom
from conjunt_indiv import Cjt_individu
from individu import individu
import copy as cp

class Cjt_trets:   
    class _tretsstr: 
        def _init_(self): 
            self._parcrom = Parcrom()
            self._individus = set()
            
    def _init_(self): 
        self.__trets = dict()

    def afegir_tret(self, a, ind, n): 
        # a es un string, ind es Individu, n és int
        if a in self.__trets: 
            if ind in self.__trets[a]._individus:
                print("  error")
            else:
                self.__trets[a]._individus.add(n)
                self.__trets[a]._parcrom.interseccio_tret(ind.cromosomes())
        else: 
            elem = self._tretsstr()
            elem._individus.add(n)
            elem._parcrom = cp.deepcopy(ind.cromosomes())
            self.__trets[a] = elem

    def esborrar_tret(self, n, p, cjt): 
        if p in self.__trets: 
            if n in slef.__trets[p].__individus:
                self.__trets[p]._individus.remove(n)
                if len(self.__trets[p]._individus) == 0:
                    del self.__trets[p]
                # else:
                    # ll = list(self.__trets[p]._individus)
                    # ll.sort()
            else:
                print("  error")
        else:
            print("  error")
    

    def consulta_tret(self, nom_tret):
        if nom_tret in self.__trets:
            print(f"  {nom_tret}")
            for inv in self.__trets[nom_tret]._individus: #ordre?
                print(f"Individu {inv} té el tret {nom_tret}")
        else:
            print("  error")


    def distribucio_tret(self, nom_tret): #acabar
        count = len(self.__trets.get(nom_tret, []))
        print(f"{nom_tret}: {count}")
