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
        elif arbre.fulla():
            if self.__individus[arbre.valor_arrel()].consultar_tret(tret): #self.__conjunt_individus[arbre.valor_arrel()-1]??
                return arbre
            else:
                return None
            
        elif self.__individus[arbre.valor_arrel()].consultar_tret(tret):  #self.__conjunt_individus[arbre.valor_arrel()-1]??
            return ArbreBinari(arbre.valor_arrel(), self.__arbre_distribucio(arbre.fill_esq(),tret),self.__arbre_distribucio(arbre.fill_dre(),tret))
        else:
            res_esq = self. __arbre_distribucio(arbre.fill_esq(),tret)
            res_dre = self.__arbre_distribucio(arbre.fill_dre(),tret)
            if res_esq == res_dre == None:
                return None
            else:
                return ArbreBinari(-(arbre.valor_arrel()), res_esq, res_dre)
