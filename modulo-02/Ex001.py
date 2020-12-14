import datetime as dt


class TipoMonstro:

    def __init__(self, nome, tipo, ps):
        self.nome = nome

        self.tipo = tipo

        self.ps = ps

        self.evolucao = 1

        self.ativo = True

        self.alimentos = 1

        self.data_cap = dt.datetime.today()

    def __str__(self):
        s = ''

        s += 'Nome        :%s\n' % self.nome

        s += 'Tipo        :%s\n' % self.tipo

        s += 'Ponto Saude :%d\n' % self.ps

        s += 'Evolucao    :%d\n' % self.evolucao

        s += 'Ativo       :%s\n' % self.ativo

        s += 'Alimentos   :%d\n' % self.alimentos

        s += 'Data Captura:%s\n' % self.data_cap.strftime('%d/%m/%Y')

        return s

    def reviver(self):
        self.ativo = True

    def desmaiar(self):
        self.ativo = False

    def evoluir(self):
        self.evolucao += 1

    def alimentar(self):
        self.alimentos += 1


class TipoFogo(TipoMonstro):

    def __init__(self, nome, tipo, ps, temperatura):
        super().__init__(nome, tipo, ps)
        self.temperatura = temperatura

    def __str__(self):
        s = ''

        s += 'Temperatura :%d\n' % self.temperatura

        return super().__str__() + s

    def aquecer(self):
        self.temperatura += 15

    def incendio(self):
        print(self.nome, 'incendio')


class TipoAgua(TipoMonstro):

    def __init__(self, nome, tipo, ps, fluxo):
        super().__init__(nome, tipo, ps)
        self.fluxo = fluxo

    def __str__(self):
        s = ''
        s += 'Fluxo       :%d\n' % self.fluxo
        return super().__str__() + s

    def fluir(self):
        self.fluxo += 20

    def chuva(self):
        print(self.nome, 'chuva')


Zuko = TipoFogo('Zuko', 'Fogo', 200, 50)
Katara = TipoAgua('Katara', 'Agua', 250, 25)


print(Zuko)
Zuko.incendio()

print('-' * 25)

print(Katara)
Katara.chuva()
