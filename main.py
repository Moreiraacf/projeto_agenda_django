import random
from random import randint

num = [
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34,
    35, 36, 37, 38, 40, 42, 43, 49, 41, 45, 48, 46, 39,
    50, 51, 44, 47, 52,
]

names = [
    'Charles', 'Jose', 'Crystal', 'Robin', 'Allison', 'Courtney', 'Alex', 'Daniel', 'Rafael', 'Reidel',
    'Remilson', 'Edmilson', 'Thaís', 'Nathalia', 'Priscila', 'Ursula', 'Fernanda', 'Maria', 'Eduarda', 'Eduardo',
    'Luana', 'Luana', 'Lauro', 'Laura', 'Dante', 'Geraldo', 'Gustavo', 'Giovana', 'Antônio', 'Paulo', 'Pedro'
]

sobre = [
    'Moreira', 'Pereira', 'De Souza', 'Carvalho', 'Oliveira', 'Louvante', 'Batista', 'Taylor', 'Valente',

    'Da Fonseca', 'Da Silva', 'Nascimento', 'De Oliveira', 'Gárcia', 'Guerreiro', 'Bertoldo'
]

numbers = randint(0, 9)

cat = [
    'Família', 'Conhecidos', 'Amigos'
]

nome = random.choices(names)
sobrenome = random.choice(sobre)
idade = random.choice(num)
telefone = numbers * 6

# tel = telefone.astype(str)
categoria = random.choice(cat)

# for i in numbers:
#     print(i)
#
# print(f'Nome: {nome} \n'
#       f'Sobrenome: {sobrenome} \n'
#       f'Idade: {idade} \n'
#       f'Telefone: {telefone} \n'
#       f'E-mail: {nome}@email.com \n'
#       f'Categoria: {categoria} \n')

cont = 0
while True:
    if cont < 65:
        for n in names:
            print(f'Nome: {n} \n'
                  f'Sobrenome: {random.choice(sobre)} \n'
                  f'E-mail: {n.lower()}@email.com \n'
                  f'Idade: {random.choice(num)} \n'
                  f'Categoria: {random.choice(cat)} \n'
                  f'-----------------------------------')
            cont += 1
    else:
        break
