# Gerador e Validador de CPF

Projeto de estudo desenvolvido em **Python** para explorar a geração e a validação de números de CPF por meio de um menu interativo no terminal.

## Funcionalidades

- Menu interativo para selecionar geração, validação ou saída.
- Geração de nove dígitos aleatórios e cálculo dos dígitos finais pela lógica implementada.
- Conferência dos dígitos verificadores de uma entrada.
- Exibição do resultado da validação no terminal.
- Aceitação de letras maiúsculas ou minúsculas nas opções do menu.

## Tecnologias

- Python.
- Módulo `random`, da biblioteca padrão.

Não é necessário instalar bibliotecas externas.

## Requisitos

- **Python 3.12 ou superior** para executar o código atual.
- Terminal ou prompt de comando.
- Git, caso opte por clonar o repositório.

A versão mínima decorre da sintaxe de uma f-string em `main.py`, que reutiliza aspas simples dentro de uma expressão delimitada por aspas simples.

## Como executar

### 1. Obtenha o projeto

```bash
git clone https://github.com/Victoidi/Gerador-e-validador-de-CPF.git
cd Gerador-e-validador-de-CPF
```

Caso o repositório esteja privado, será necessário ter acesso e autenticar-se no GitHub.

Também é possível baixar os arquivos pelo GitHub e abrir um terminal na pasta do projeto.

### 2. Inicie o programa

```bash
python main.py
```

Dependendo da instalação, utilize:

```bash
python3 main.py
```

No Windows, com o inicializador do Python instalado, também é possível selecionar a versão explicitamente:

```powershell
py -3.12 main.py
```

## Como usar

Ao iniciar, o programa exibe:

```text
Para (G)erar, (V)álidar e (S)aír:
```

| Opção | Ação |
| --- | --- |
| `G` | Gera uma sequência numérica e a exibe no terminal. |
| `V` | Solicita uma entrada e apresenta o resultado da validação. |
| `S` | Encerra o programa. |

### Gerar

Digite `G` e pressione Enter.

O programa sorteia nove dígitos e acrescenta os resultados dos cálculos dos dígitos verificadores. A saída não possui pontos nem hífen.

**Atenção:** devido às limitações atuais, a sequência gerada pode não ter 11 dígitos ou não atender ao algoritmo correto de CPF.

### Validar

Digite `V` e pressione Enter. Em seguida, informe os **11 dígitos, sem pontos, hífen ou espaços**.

O programa insere um hífen após o nono caractere e chama a classe de validação. A resposta informa se a entrada foi considerada `Válido` ou `Inválido` pela implementação atual.

Entradas que já contêm hífen fazem o programa retornar ao menu sem apresentar o resultado.

### Sair

Digite `S` e pressione Enter.

Na versão atual, o programa exibe a mensagem `A opção digitada é invalida!` antes de encerrar, devido à organização das condições do menu.

## Estrutura do projeto

```text
Gerador-e-validador-de-CPF/
├── main.py       # Menu interativo e leitura das entradas
└── service.py    # Classes de geração e validação
```

### `main.py`

Responsável por:

- Exibir o menu.
- Ler e converter a opção para letras maiúsculas.
- Acionar a geração ou a validação.
- Exibir resultados e tratar exceções `ValueError` e `TypeError`.

### `service.py`

Contém duas classes:

| Classe | Método principal | Responsabilidade |
| --- | --- | --- |
| `gerador_cpf` | `compilador()` | Gerar a base aleatória, calcular os dígitos finais e retornar a sequência. |
| `validador_cpf` | `validacao_completa()` | Executar as duas verificações e retornar um valor booleano. |

## Uso das classes

As classes também podem ser importadas em outro arquivo Python, desde que `service.py` esteja disponível no caminho de importação.

### Geração

```python
from service import gerador_cpf

gerador = gerador_cpf()
numero = gerador.compilador()

print(numero)
```

### Validação

Ao utilizar a classe diretamente, forneça o hífen separando os nove dígitos iniciais dos dois verificadores:

```python
from service import validador_cpf

entrada = input("Digite os 11 dígitos, sem pontuação: ").strip()

if len(entrada) == 11 and entrada.isascii() and entrada.isdigit():
    cpf = f"{entrada[:9]}-{entrada[9:]}"
    resultado = validador_cpf(cpf).validacao_completa()
    print(f"Resultado da implementação atual: {resultado}")
else:
    print("Informe exatamente 11 dígitos numéricos.")
```

A verificação de formato acima pertence ao exemplo; ela ainda não está implementada no menu original. As limitações matemáticas descritas a seguir também se aplicam ao uso direto das classes.

## Limitações conhecidas

### Cálculo dos dígitos verificadores

- **Comparação de strings:** o resto da divisão é convertido em texto antes da comparação com `'9'`. Assim, `'10'` é tratado como menor que `'9'`, em vez de ser convertido para `'0'`. Isso afeta a validação e pode produzir sequências geradas com tamanho incorreto.
- **Pesos do segundo dígito:** o código utiliza pesos de `10` a `1`. Para o segundo dígito do CPF, o cálculo deve utilizar pesos de `11` a `2`.
- **Dígitos repetidos:** não há uma regra específica para rejeitar entradas compostas por um único dígito repetido.

### Entrada e interação

- O menu não verifica previamente se a entrada contém exatamente 11 dígitos.
- CPFs com hífen são ignorados pelo fluxo de validação do menu.
- Entradas com pontos não são normalizadas corretamente pelo menu.
- Entradas incompletas ou com tamanho inadequado podem causar `IndexError`, que não é tratado.
