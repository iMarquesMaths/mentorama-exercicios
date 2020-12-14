s = 'Mentorama'.upper()
print('De trás pra frente a palavra fica', s[::-1])
vogais = []
for vogal in s:
    if vogal in 'AEIOU':
        vogais.append(vogal)
print('Existem {} vogais nessa palavra, e são elas {}'.format(len(vogais), vogais))
