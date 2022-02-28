"""
Primeiro código python
"""
# Quebra de linha
print()

# Saudação
print('Olá! Bem-vindo ao meu primeiro projeto Python!\n' 
      'Gostaria de pedir para que não use unidades de medidas, como pro exemplo: kg, cm, m, etc. \n'
      'Pois o código não irá funcionar corretamente, peço perdão pela inconveniência\n\n')

# Adquirindo Informações
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
altura = input('Qual a sua altura? ')
peso = input('Quanto você pesa? ')

# Alterando alguns dados para o tipo 'int/float'
idade = int(idade)
peso = int(peso)
altura = float(altura)

# Fórmula IMC
imc = peso / (altura ** 2)

# Resultado
print()
print(f'{nome} tem {idade} anos de idade.\n'
      f'Considerando que {nome} tem {altura}m de altura e pesa {peso}kg, o seu IMC será:\n'
      f'> {imc:.2f}')