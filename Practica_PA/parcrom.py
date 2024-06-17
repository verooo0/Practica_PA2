class Parcrom: 

    def __init__(self, cromosomes=""): # 
        self.__num_cromosomes = len(cromosomes) // 2
        self.__cromosomes_sup = cromosomes[:self.__num_cromosomes]        #es divideix la seqüència de cromosomes en dos cromosomes
        self.__cromosomes_inf = cromosomes[self.__num_cromosomes:]

    def num_cromosomes(self):                                
        return self.__num_cromosomes                                             # Retorna el nombre que té cada parells de cromosomes

    def cromosomes_sup(self): 
        return self.__cromosomes_sup                                            # Retorna la meitat superior dels cromosomes

    def cromosomes_inf(self): 
        return self.__cromosomes_inf                                            # Retorna la meitat inferior dels cromosomes

    def interseccio_tret(self, nou_parell): 
        if  self.__num_cromosomes == 0:                                        #si els cromosoma esta buit els nous cromosomes són els cromosomes input
            self.__num_cromosomes = nou_parell.num_cromosomes()
            self.__cromosomes_sup = nou_parell.cromosomes_sup()
            self.__cromosomes_inf = nou_parell.cromosomes_inf()
        else:
            nou_superior = []
            nou_inferior = []
            for i in range(self.__num_cromosomes):                                #per el nombre que té cada cromosoma es compara el dos cromosomes superior i inferior
                if self.__cromosomes_sup[i] != nou_parell.cromosomes_sup()[i] or self.__cromosomes_inf[i] != nou_parell.cromosomes_inf()[i]:   
                    nou_superior.append("-")                                        #si no son iguals es guarda com a '-' a la llista del nou cromosoma
                    nou_inferior.append("-")
                else:
                    nou_superior.append(self.__cromosomes_sup[i])                    #si son iguals es guarda com eren
                    nou_inferior.append(self.__cromosomes_inf[i])
            self.__cromosomes_sup = ''.join(nou_superior)                            #es guarden a les variables d'instància com a string
            self.__cromosomes_inf = ''.join(nou_inferior)

    def reiniciar(self):
        self.__num_cromosomes = 0                                                     # Restableix les dades del cromosoma a un estat buit
        self.__cromosomes_sup = ""
        self.__cromosomes_inf = ""

    def escriure_parcrom(self):         
        print(f"  {self.__cromosomes_sup}")                                            # Imprimeix l'estat actual del parells de cromosomes
        print(f"  {self.__cromosomes_inf}")
