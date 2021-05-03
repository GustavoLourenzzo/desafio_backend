
class Utils:
    def __init__(self):
        self.enumTipoTaxa = [
            "NEGATIVADO",
            "SCORE_ALTO",
            "SCORE_BAIXO"
        ]

    def getPerfilScore(self,score_value, negativado):
        if negativado:
            return self.enumTipoTaxa[0]
        
        if score_value > 500:
            return self.enumTipoTaxa[1]

        return self.enumTipoTaxa[2]