import service

escolha = ''

while escolha != 'S':

    escolha= input('Para (G)erar, (V)álidar e (S)aír: ').upper()

    try:
        if escolha == 'G':
            gerador = service.gerador_cpf()
            print(gerador.compilador())



        elif escolha == 'V':
            #cpf = '746.824.890-70'
            cpf_entrada= str(input('Digite o cpf a ser validado: '))

            if '-' not in cpf_entrada:
                cpf= cpf_entrada[:9] + '-' + cpf_entrada[9:]
            
            else:
                continue
            
            validacao= service.validador_cpf(cpf)

        #print(validacao.validacao_completa())

            print(f'O CPF {cpf} é {'Válido' if validacao.validacao_completa() == True else 'Inválido'}')

        else:
            print('A opção digitada é invalida!')
            continue
    except ValueError:
        print(f'Erro de valor "{ValueError}", digite somente a letra de acordo com a opção!')
        continue

    except TypeError:
        print(f'Tipo da entrada incorreto "{TypeError}", digite somente a letra de acordo com a opção!')
        continue
    
