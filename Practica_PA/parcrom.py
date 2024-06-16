class Parcrom: 

    def __init__(self, cromosomes=""):
        self.__num_cromosomes = len(cromosomes) // 2
        self.__cromosomes_sup = cromosomes[:self.__num_cromosomes]
        self.__cromosomes_inf = cromosomes[self.__num_cromosomes:]

    def num_cromosomes(self):
        return self.__num_cromosomes

    def cromosomes_sup(self):
        return self.__cromosomes_sup

    def cromosomes_inf(self):
        return self.__cromosomes_inf

    def interseccio_tret(self, nou_parell):
        if  self.__num_cromosomes == 0:
            self.__num_cromosomes = nou_parell.num_cromosomes()
            self.__cromosomes_sup = nou_parell.cromosomes_sup()
            self.__cromosomes_inf = nou_parell.cromosomes_inf()
        else:
            nou_superior = []
            nou_inferior = []
            for i in range(self.__num_cromosomes):
                if self.__cromosomes_sup[i] != nou_parell.cromosomes_sup()[i] or self.__cromosomes_inf[i] != nou_parell.cromosomes_inf()[i]:
                    nou_superior.append("-")
                    nou_inferior.append("-")
                else:
                    nou_superior.append(self.__cromosomes_sup[i])
                    nou_inferior.append(self.__cromosomes_inf[i])
            self.__cromosomes_sup = ''.join(nou_superior)
            self.__cromosomes_inf = ''.join(nou_inferior)

    def reiniciar(self):
        self.__num_cromosomes = 0
        self.__cromosomes_sup = ""
        self.__cromosomes_inf = ""

    def escriure_parcrom(self):
        print(f"  {self.__cromosomes_sup}")
        print(f"  {self.__cromosomes_inf}")
