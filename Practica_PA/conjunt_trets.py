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

    def consulta_tret(self, nom_tret):
        if not nom_tret in self.__trets:
            print("  error")
        else:
            print(f"  {nom_tret}")
            self.__trets[nom_tret]._parcrom.escriure_parcrom()
            individus = sorted(self.__trets[nom_tret]._individus)
            for a in individus:
                print(f"  {a}")

    def distribucio_tret(self, tret):
        if not tret in self.__trets:
            print("  error")
        else:
            inordre = self.__conjunt_individus.distribucio(tret)
            print(end=" ")
            for i in inordre:
                print(f" {i}", end="")
            print()

                        #individu_obj = self.__conjunt_individus.obtenir_individu(ind_num)
                        #self.__trets[p]._parcrom.interseccio_tret(individu_obj.cromosomes())
