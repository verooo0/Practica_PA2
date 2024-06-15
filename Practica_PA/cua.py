class Cua:
    # ----------------------------------------------------
    # Cada element de la cua serà una instància de _Node
    class _Node:
        __slots__ = '_element', '_next' 
        def __init__(self, element, next):
            self._element = element 
            self._next = next              
    # ------------------------------------------

    def __init__(self):
        self._cap = None
        self._cua = None
        self._mida = 0

    def buida(self):
        return self._mida == 0
 
    def mida(self):
        return self._mida

    def primer(self):
        # Pre: La cua no és buida
        return (self._cap)._element

    def encuar(self, e):
        # nou node al final de la cua
        nou = self._Node(e, None)   
        if self.buida():
            # cas especial, cua buida
            self._cap = nou       
        else:
            self._cua._next = nou
        # actualitzar referència al darrer node
        self._cua = nou            
        self._mida += 1
        return self

    def desencuar(self):
        # Pre: La cua no és buida
        resposta = self._cap._element
        self._cap = self._cap._next
        self._mida -= 1
        if self.buida():               
            # cas especial, cua buida
            # el _cap eliminat també
            # era la cua
            self._cua = None          
        return resposta
    def trenar(self,c): 
        if self.buida(): 
            self._cap, self._cua = c._cap, c._cua
            self._mida = c._mida
        else: 
            sp = self._cap
            cp = c._cap 
            while sp is not None and cp is not None: 
                spnext, cpnext = sp._next, cp._next
                sp._next = cp
                cp._next = spnext if spnext is not None else cp._next
                sp, cp= spnext, cpnext 
            if sp is None: 
                self._cua = c._cua
            self._mida += c._mida
        c._cap = c._cua = None
        c._mida = 0 
