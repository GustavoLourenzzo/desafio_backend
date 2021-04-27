

class Utils:
    def __init__(self):
        self.enumTipoTaxa = [
            "NEGATIVADO",
            "SCORE_ALTO",
            "SCORE_BAIXO"
        ]
        self.enumParcelas = [
            6,12,18,24,36
        ]

    def checkEnumTipoTaxa(self, value):
        return value in self.enumTipoTaxa
    
    def checkEnumParcelas(self, value):
        return value in self.enumParcelas