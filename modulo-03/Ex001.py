cores = {'reset': '\033[m',
         'cor1': '\033[0;33;40m',
         'cor2': '\033[1;33;40m'}


def formata_valor(v_in):
    s_out = '{:,.2f}'.format(v_in)
    s_out = s_out.replace('.', ',')
    return s_out


nome_arq = 'lista_temp.txt'

with open(nome_arq) as farq:
    # pula o cabecalho
    linha = farq.readline()

    saida = '{}'.format(cores['cor2'])
    # item
    saida += ' ITM' + ' '
    # codigo
    saida += 'CCOD' + ' '
    # descricao do produto
    saida += '{:.<30.25}'.format('Produto')
    # quantidade
    saida += ' QTD' + ' '
    # valor unitario
    val_unit = '{:>10}'.format('UNIT')
    saida += val_unit
    # valor total
    val_total = '{:>16}'.format('TOTAL {}'.format(cores['reset']))
    saida += val_total
    print(saida)

    item = 0
    while True:
        linha = farq.readline()
        # chegou no final do arquivo?
        if linha == '':
            break
        # colunas estao separadas por virgula
        cols = linha.split(',')
        # atualiza item
        item += 1

        saida = '{}'.format(cores['cor1'])
        # item
        saida += ' {:03}'.format(item) + ' '
        # codigo
        saida += cols[0] + ' '
        # descricao do produto
        saida += '{:.<30.25}'.format(cols[1])
        # quantidade
        qtd = int(cols[2])
        saida += ' {:03}'.format(qtd) + ' '
        # valor unitario
        val = float(cols[3])
        val_unit = '{:>10}'.format(formata_valor(val))
        saida += val_unit
        # valor total
        val *= qtd
        val_total = '{:>12} {}'.format(formata_valor(val), cores['reset'])
        saida += val_total
        print(saida)
