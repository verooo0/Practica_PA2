from parcrom import Parcrom
class Cjt_trets:   
    class _tretsstr:                                 #creem classe de trets dins de cjt_trets
        def __init__(self, cromosomes): 
            self._parcrom = Parcrom(cromosomes)   #inicialitza la clase Parcrom
            self._individus = set()               #creem un set() per als individus
            
    def __init__(self, conjunt_individus): 
        self.__trets = dict()                            #creem diccionari per guardar el conjunt de trets
        self.__conjunt_individus = conjunt_individus

    def afegir_tret(self, t, ind, n): 
        cromosomes = ind.cromosomes()                                 #crida al mètode cromosomes a la classe individu
        if t in self.__trets:                                         #si el trets esta al diccionari (ja existeix)
            if n in self.__trets[t]._individus:                           #si l'individu ja té aquest tret dona error
                print("  error")
            else:                                                         #si l'individu no té el tret s'afegeix al set i es crida al mètode intersecció_tret de la clase Parcrom
                self.__trets[t]._individus.add(n)
                self.__trets[t]._parcrom.interseccio_tret(cromosomes)
        else:                                                         #si el tret no existeix s'afegeix el tret al diccionari de trets i al set d'individus
            elem = self._tretsstr(ind.crom())
            elem._individus.add(n)
            self.__trets[t] = elem
        ind.afegir_tret(t)                                            #es crida al mètode afegir_tret de la classe individu


    def esborrar_tret(self, t, n, ind): 
        if not t in self.__trets:                                  # Si el tret no existeix dona error
            print("  error")
        else:                                                       # Si el tret existeix
            if not n in self.__trets[t]._individus:                     # Si l'individu no té el tret error
                print("  error")
            else:                                                        # Si l'individuo té el tret s'elimina el tret
                self.__trets[t]._individus.remove(n)                      #s'elimina el tret de l'individu
                ind.esborrar_tret(t)                                      #crida al mètode esborrar_tret de la classe individu
                if len(self.__trets[t]._individus) == 0:                  #si cap individu té el tret s'elimina el tret del diccionari
                    del self.__trets[t]
                else:                                                     #si queda algún individu amb el tret
                    self.__trets[t]._parcrom.reiniciar()                    #crida al mètode reiniciar de la clase Parcrom 
                    for ind_num in self.__trets[t]._individus:                #per als individus que tenen el tret es fa la intersecció dels cromosomes
                        individu_obj = self.__conjunt_individus.obtenir_individu(ind_num)
                        self.__trets[t]._parcrom.interseccio_tret(individu_obj.cromosomes())

    def consulta_tret(self, nom_tret):
        if not nom_tret in self.__trets:                                    #si el tret no existeix error
            print("  error")
        else:                                                                  #si el tret existeix 
            print(f"  {nom_tret}")
            self.__trets[nom_tret]._parcrom.escriure_parcrom()                 #crida al mètode escriure_parcrom de la classe Parcrom
            individus = sorted(self.__trets[nom_tret]._individus)              #guarda els individus que tenen el tret en la variable
            for a in individus:                                                #escriu els individus que tenen el tret
                print(f"  {a}")

    def distribucio_tret(self, tret):
        if not tret in self.__trets:                                        #si el tret no existeix error
            print("  error")
        else:                                                               #si el tret existeix
            inordre = self.__conjunt_individus.distribucio(tret)            #crida al mètode distribucio de la classe cjt_individus i escriu el subarbre retornat en inordre
            print(end=" ")
            for i in inordre:
                print(f" {i}", end="")
            print()

