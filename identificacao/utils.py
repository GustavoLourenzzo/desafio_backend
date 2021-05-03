import re

class Utils:
    def __init__(self):
        pass

    def validaCpf(self, value, testaDigito=False):
        cpf = self.cpfViewToData(value)
        if cpf is None:
            return False
        #Demais validações se forem necessarias
        if testaDigito:
            if cpf=='00000000000' or cpf=='11111111111' or cpf=='22222222222' or cpf=='33333333333' or cpf=='44444444444' or cpf=='55555555555' or cpf=='66666666666' or cpf=='77777777777' or cpf=='88888888888' or cpf=='99999999999':
                return False
            
            sum = 0
            weight = 10

           
            for n in range(9):
                sum = sum + int(cpf[n]) * weight

                weight = weight - 1

            verifyingDigit = 11 -  sum % 11

            if verifyingDigit > 9 :
                firstVerifyingDigit = 0
            else:
                firstVerifyingDigit = verifyingDigit

            
            sum = 0
            weight = 11
            for n in range(10):
                sum = sum + int(cpf[n]) * weight

                weight = weight - 1

            verifyingDigit = 11 -  sum % 11

            if verifyingDigit > 9 :
                secondVerifyingDigit = 0
            else:
                secondVerifyingDigit = verifyingDigit

            if cpf[-2:] != "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
                return False
        return True

    def validaCelular(self, value):
        celular = self.celularViewToData(value)
        if celular is None:
            return False
        #Demais validações se forem necessarias
        return True

    def validaScore(self, value):
        if not isinstance(value, int):
            return False

        if value > 1000 or value < 0:
            return False
        return True

    def cpfViewToData(self, value):
        
        if not isinstance(value, str):
            return None
        
        cpf = re.sub("[^0-9]", "", value)
        if len(cpf) != 11:
            return None

        return cpf

    def celularViewToData(self, value):
        
        if not isinstance(value, str):
            return None
        
        celular = re.sub("[^0-9]", "", value)
        if len(celular) > 11 or len(celular) < 10:
            return None

        return celular
    
    