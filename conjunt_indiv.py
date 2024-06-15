from arbre_binari_amb_nodes import ArbreBinari
from individu import *
from pytokr import pytokr

item = pytokr()

class Cjt_individu:

    def __init__(self,n):
        self.__individus = [None]
        self.__arbre = self.__llegir_arbre()
        for _ in range(n):
            self.afegir_individu(item())
        self.__conjunt_individus = []

    def consultar_individu(self,t):
        return self.__individus[t].escriure_ind()
    
    def afegir_individu(self, cromosomes):
        self.__individus.append(individu(cromosomes))
    
    def afegir_tret(self,t,n):
        self.__conjunt_individus[n-1].afegir_tret(t)

    def esborrar_tret(self,t,n): 
        self.__conjunt_indivius[n-1].esborrar_tret(t) 

    
    def llegir_individu(self,a,n): 
        self.__arbre = self.__llegeix_arbrebinari_int(0)
        for i in range(n): 
            ind = individu()
            ind.llegir_individu(n)
            self.__conjunt_individus[i] = ind

    def distribucio(self, tr): 
        alpha = self.__arbre_distribucio(self.__arbre, tr)  #alpha = self.__arbre_nou(self.__arbre, s)
        print(' ', end = '')
        self.__escriure_arbrebin_int(alpha)

## falten metodes privats 

    def __arbre_distribucio(self,arbre,tret):
        if arbre.buit(): 
            return None
        elif arbre.fulla():
            if self.__conjunt_individus[arbre.valor_arrel()].te_tret(tret): #self.__conjunt_individus[arbre.valor_arrel()-1]??
                return arbre
            else:
                return None
            
        elif self.__conjunt_individus[arbre.valor.arrel()].te_tret(tret):  #self.__conjunt_individus[arbre.valor_arrel()-1]??
            return ArbreBinari(arbre.valor_arrel(), self.__arbre_distribucio(arbre.fill_esq(),tret),self.__arbre_distribucio(arbre.fill_dre(),tret))
        else:
            res_esq = self. __arbre_distribucio(arbre.fill_esq(),tret)
            res_dre = self.__arbre_distribucio(arbre.fill_dre(),tret)
            if res_esq == res_dre == None:
                return None
            else:
                return ArbreBinari(-(arbre.valor_arrel()), res_esq, res_dre)

    
    def __escriure_arbre_bin(self,alpha):
        if alpha == None:
            return []
        else:
            return alpha.inorder()
        
    def __llegir_arbre(self, marca = 0):
        x = int(item())
        if x != marca:
            l = self.__llegir_arbre(marca)
            r = self.__llegir_arbre(marca)
            return ArbreBinari(x,l,r)
        else:
            return ArbreBinari()