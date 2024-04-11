class Rose():
    def __init__(self, navn, beskrivelse, storrelse, farge, pris):
        self.navn = navn
        self.beskrivelse = beskrivelse
        self.storrelse = storrelse
        self.farge = farge
        self.pris = pris
        
class Klatreroser(Rose):
    def __init__(self, navn, beskrivelse, storrelse, farge, pris, lengde_rank, stottekrav, voksemonster):
        super().__init__(navn, beskrivelse, storrelse, farge, pris)
        self.lengde_rank = lengde_rank
        self.stottekrav = stottekrav
        self.voksemonster = voksemonster

class Stilkroser(Rose):
    def __init__(self, navn, beskrivelse, storrelse, farge, pris, lengde_stilk, antall_blomster, duft):
        super().__init__(navn, beskrivelse, storrelse, farge, pris)
        self.lengde_stilk = lengde_stilk
        self.antall_blomster = antall_blomster
        self.duft = duft

class Buskroser(Rose):
    def __init__(self, navn, beskrivelse, storrelse, farge, pris):
        super().__init__(navn, beskrivelse, storrelse, farge, pris)