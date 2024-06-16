from arbre_binari_amb_nodes import ArbreBinari
from individu import *
from pytokr import pytokr
item = pytokr()

class Cjt_individu:
    def __init__(self, n):
        self.__individus = [None]                    #crear llista amb None per a que el número de l'individu coincideix-hi amb la seva posició a la llista
        self.__arbre = self.__llegir_arbre()         #llegir l'arbre en preorde i marca 0
        for _ in range(n):
            self.afegir_individu(item())             #cridar al mètode afegir_individu amb els cromosomes com input
    
    def consultar_individu(self, ind):
        return self.__individus[ind].escriure_ind()     #crida al mètode escriure_ind de la classe individu 
    
    def afegir_individu(self, cromosomes):
        self.__individus.append(individu(cromosomes))    #afageix a la llista d'individus la informació d'aquest( número y cromosomes) que s'ha obtingut després d'inicialitzar la classe individu
    
    def afegir_tret(self, t, n):
        self.__individus[n].afegir_tret(t)              #crida al mètode afegir_tret de la classe individu 

    def esborrar_tret(self, t, n): 
        self.__individus[n].esborrar_tret(t)             #crida al mètode esborrar_tret de la classe individu

    def distribucio(self, tr): 
        sub_arbre = self.__arbre_distribucio(self.__arbre, tr)      #crida al mètode __arbre_distribucio de la classe cjt_individu
        if sub_arbre is None:                                       #si el sub_arbre és None vol dir que cap individu te el tret
            return []
        else: 
            return sub_arbre.inordre()                              #retorna el sub_arbre dels individus que tenen el tret en inordre
          
    def obtenir_individu(self, n):
        return self.__individus[n]                                  #retorna la informació guardada de l'individu en la llista dels conjunts d'individus

        
    def __llegir_arbre(self, marca = 0):
        x = int(item())
        if x != marca:
            l = self.__llegir_arbre(marca)
            r = self.__llegir_arbre(marca)
            return ArbreBinari(x, l, r)
        else:
            return ArbreBinari()
        
    def __arbre_distribucio(self, arbre, tret):
        if arbre.buit():
            return None
            
        # Mira recursivamente los hijos izquierdo y derecho
        esq_subArbre = self.__arbre_distribucio(arbre.fill_esq(), tret)
        dre_subArbre = self.__arbre_distribucio(arbre.fill_dre(), tret)

        te_tret = self.__individus[arbre.valor_arrel()].consultar_tret(tret)

        if te_tret:
            # si te tret, construeix arbre amb els dos fills
            return ArbreBinari(arbre.valor_arrel(), esq_subArbre, dre_subArbre)
        else:
            # Sino, marcar arrel amb un valor negatiu si algun fills te tret o return None si no es el cas.
            if esq_subArbre or dre_subArbre:
                return ArbreBinari(-arbre.valor_arrel(), esq_subArbre, dre_subArbre)
            else:
                return None
