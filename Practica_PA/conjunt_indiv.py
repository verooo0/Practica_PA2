from arbre_binari_amb_nodes import ArbreBinari
from individu import *
from pytokr import pytokr
item = pytokr()

class Cjt_individu:
    def __init__(self, n):
        self.__individus = [None]
        self.__arbre = self.__llegir_arbre()
        for _ in range(n):
            self.afegir_individu(item())
    
    def consultar_individu(self, t):
        return self.__individus[t].escriure_ind()
    
    def afegir_individu(self, cromosomes):
        self.__individus.append(individu(cromosomes))
    
    def afegir_tret(self, t, n):
        self.__individus[n].afegir_tret(t)

    def esborrar_tret(self, t, n): 
        self.__individus[n].esborrar_tret(t) 

    def distribucio(self, tr): 
        alpha = self.__arbre_distribucio(self.__arbre, tr)  
        if alpha is None: 
            return []
        else: 
            return alpha.inordre()
          
    def obtenir_individu(self, n):
        return self.__individus[n]

        
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
