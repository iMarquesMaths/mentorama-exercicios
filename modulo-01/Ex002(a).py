count = soma_par = qtd_par = soma_impar = qtd_impar = 0 
while count <= 9:
    count += 1
    if count % 2 == 0:
        qtd_par += 1
        soma_par = soma_par + count
    else:
        qtd_impar += 1
        soma_impar = soma_impar + count
print('Entre os números 1 e 10 existem {} numeros pares e {} numeros ímpares'.format(qtd_par, qtd_impar))
print('As somas dos valores pares resulta em {} e dos valores ímpares em {}'.format(soma_par, soma_impar))
