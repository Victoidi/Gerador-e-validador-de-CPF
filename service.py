#cpf= '746.824.890-70'
import random

class validador_cpf:
    
    
    def __init__(self,cpf):
        self.cpf = cpf

    def primeiro_digito(self):

        nr_validacao= self.cpf.split('-')
        
        nr_cpf = []

        nr_multiplicado = []

        nr_calculo = []

        for i in range(10,1,-1):
            nr_calculo.append(i)

        for n in nr_validacao[0]:
            if n != '.':
                nr_cpf.append(int(n))


        for n in range(len(nr_cpf)):
            nr_multiplicado.append(nr_cpf[n] * nr_calculo[n])



        total_nr_multiplicado = sum(nr_multiplicado) * 10

        resto =  str(total_nr_multiplicado % 11)

        vereficacao = resto if resto <= '9' else '0'

        #print(f'O primeiro digito de valid CPF {self.cpf} é {'Válido' if vereficacao == nr_validacao[1][0] else 'Inválido'}')

        return True if vereficacao == nr_validacao[1][0] else False
            
        
    def segundo_digito(self):
        
        nr_validacao= self.cpf.split('-')
        
        nr_cpf = []

        nr_multiplicado = []

        nr_calculo = []

        for i in range(10,0,-1):
            nr_calculo.append(i)

        for n in nr_validacao[0]:
            if n != '.':
                nr_cpf.append(int(n))

        nr_cpf.append(int(nr_validacao[1][0]))


        for n in range(len(nr_cpf)):
            nr_multiplicado.append(nr_cpf[n] * nr_calculo[n])


        total_nr_multiplicado = sum(nr_multiplicado) * 10

        resto =  str(total_nr_multiplicado % 11)

        vereficacao = resto if resto <= '9' else '0'

        #print(f'O CPF {self.cpf} é {'Válido' if vereficacao == nr_validacao[1][1] else 'Inválido'}')

        return True if vereficacao == nr_validacao[1][1] else False

        

    def validacao_completa(self):
        token_1 = self.primeiro_digito()
        token_2 = self.segundo_digito()

        token = token_1 and token_2       
        
        return token
        
class gerador_cpf:
    
    def gerador(self):

        nove_digitos = ''

        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        self.nove_digitos = nove_digitos

    def primeiro_digito(self):

        nr_cpf = self.nove_digitos

        nr_multiplicado = []

        nr_calculo = []

        for i in range(10,1,-1):
            nr_calculo.append(i)

        for n in range(len(nr_cpf)):
            nr_multiplicado.append(int(nr_cpf[n]) * nr_calculo[n])



        total_nr_multiplicado = sum(nr_multiplicado) * 10

        resto =  str(total_nr_multiplicado % 11)

        vereficacao_1 = resto if resto <= '9' else '0'
        
        self.vereficacao_1 = vereficacao_1

        #print(f'O primeiro digito de valid CPF {self.cpf} é {'Válido' if vereficacao == nr_validacao[1][0] else 'Inválido'}')

        #return vereficacao_1
            
        
    def segundo_digito(self):
        
        nr_cpf = self.nove_digitos + self.vereficacao_1

        nr_multiplicado = []

        nr_calculo = []

        for i in range(10,0,-1):
            nr_calculo.append(i)

        for n in range(len(nr_cpf)):
            nr_multiplicado.append(int(nr_cpf[n]) * nr_calculo[n])


        total_nr_multiplicado = sum(nr_multiplicado) * 10

        resto =  str(total_nr_multiplicado % 11)

        vereficacao_2 = resto if resto <= '9' else '0'

        self.vereficacao_2 = vereficacao_2

        #print(f'O CPF {self.cpf} é {'Válido' if vereficacao == nr_validacao[1][1] else 'Inválido'}')

        #return vereficacao_2

    def compilador(self):
        self.gerador()            # ← adicione essas 3 linhas
        self.primeiro_digito()
        self.segundo_digito()

        cpf_gerado = self.nove_digitos + self.vereficacao_1 + self.vereficacao_2

        return cpf_gerado