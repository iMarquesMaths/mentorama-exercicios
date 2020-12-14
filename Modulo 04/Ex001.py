import datetime as dt


def formata_valor(v_in):
    # 1 -> 0,01
    # 13456 -> 1.234,56
    s_out = '{:,.2f}'.format(v_in)
    s_out = s_out.replace(',', '_')
    s_out = s_out.replace('.', ',')
    s_out = s_out.replace('_', '.')
    return s_out


def le_arq_cat(nome_arq):
    dict_cat = {}
    try:
        with open(nome_arq, 'rt') as farq:
            for linha in farq:
                # retira \n
                linha = linha.rstrip()
                # separa colunas por espaco
                cols = linha.split()
                # A  = Aguas, qtd 0, valor 0
                dict_cat[cols[0]] = [cols[1], 0, 0]
    except FileNotFoundError:
        print('Erro no nome do arquivo de categorias')
    except IndexError:
        print('Erro no formato do arquivo de categorias')
    except:
        print('Erro no processamento do arquivo de categorias')

    return dict_cat


def le_arq_in(nome_arq):
    # le as linhas do arquivo em um gole so
    itens = []
    try:
        with open(nome_arq, 'rt') as farq:
            itens = farq.readlines()
    except FileNotFoundError:
        print('Erro no nome do arquivo de itens')
    except:
        print('Erro no processamento do arquivo de itens')

    return itens


def monta_header_item():
    saida = ''
    # item
    saida += ' IT' + ' '
    # codigo
    saida += ' COD' + ' '
    # descricao do produto
    saida += '{:.<30.25}'.format('Produto')
    # quantidade
    saida += 'QTD' + ' '
    # valor unitario
    saida += '{:>10}'.format('VAL.UNI')
    # valor total
    saida += '{:>10}'.format('VAL.TOT')
    return saida


def monta_header_cat():
    saida = ''
    saida += '{:.<20}'.format('CATEGORIA')
    saida += 'QTD' + ' '
    saida += '{:>10}'.format('VAL.CAT')
    return saida


def monta_linha_item(item, cols, dict_cat):
    saida = ''
    try:
        # item
        i = int(item)
        saida += '{:03}'.format(i) + ' '
        # codigo
        saida += cols[0] + ' '
        # descricao do produto
        saida += '{:.<30.25}'.format(cols[1])
        # quantidade
        qtd = int(cols[2])
        saida += '{:03}'.format(qtd) + ' '
        # valor unitario
        val = float(cols[3])
        val_p = '{:>10}'.format(formata_valor(val))
        saida += val_p
        # valor total
        val *= qtd
        val_p = '{:>10}'.format(formata_valor(val))
        saida += val_p

        # atualiza dicionario das categorias para este item
        chave = cols[0][0]
        dict_cat[chave][1] += qtd
        dict_cat[chave][2] += val
    except KeyError:
        print(f'Categoria {chave} invalida')
    except:
        print('Erro no processamento de item')

    return saida


def monta_linha_cat(cat):
    saida = ''
    # nome da categoria
    saida += '{:.<20}'.format(cat[0])
    # qtd de itens
    saida += '{:03}'.format(cat[1]) + ' '
    # valor total dos itens
    val = float(cat[2])
    val_p = '{:>10}'.format(formata_valor(val))
    saida += val_p
    return saida


def escreve_arq_saida(nome_arq, dict_cat, lista_itens):
    try:
        with open(nome_arq, 'wt') as farq:
            # varre a lista de itens
            for i, item in enumerate(lista_itens):
                # pula a 1a linha mas monta o header
                if i == 0:
                    linha = monta_header_item()
                    farq.write(linha + '\n')
                    continue
                # retira \n e separa as colunas por virgula
                item = item.rstrip()
                cols = item.split(',')
                # monta linha de saida formatada
                linha = monta_linha_item(i, cols, dict_cat)
                farq.write(linha + '\n')

            # header das categorias
            linha = monta_header_cat()
            farq.write(linha + '\n')
            # valor total da compra
            val_total = 0
            for chave in dict_cat.keys():
                linha = monta_linha_cat(dict_cat[chave])
                farq.write(linha + '\n')
                # atualiza valor total da compra
                val = float(dict_cat[chave][2])
                val_total += val

            # grava valor total e data da compra
            linha = 'TOTAL: R$ {:10}'.format(formata_valor(val_total))
            farq.write(linha + '\n')

            data_hora = dt.datetime.now()
            linha = 'DATA: ' + data_hora.strftime('%d/%m/%Y %H:%M:%S')
            farq.write(linha + '\n')
    except FileNotFoundError:
        print('Erro no nome do arquivo de saida')
    except:
        print('Erro no processamento do arquivo de saida')


dict_cat = le_arq_cat('categorias.txt')
if len(dict_cat) != 0:
    lista_itens = le_arq_in('lista_temp.txt')
    escreve_arq_saida('cupom_fiscal.txt', dict_cat, lista_itens)
