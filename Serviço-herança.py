class ProdutoEletronico:
    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Marca: {self.marca}")
        print(f"Preço: R${self.preco:.2f}")



class Smartphone(ProdutoEletronico):

  def __init__(self, nome, marca, preco, capacidade_armazenamento):
    super().__init__(nome, marca, preco)
    self.capacidade_armazenamento = capacidade_armazenamento

  def exibir_informacoes(self):
    super().exibir_informacoes()
    print(f"Capacidade de Armazenamento: {self.capacidade_armazenamento}")



class leptop(ProdutoEletronico):
  
  def __init__(self, nome, marca, preco, memoria_ram):
    super().__init__(nome, marca, preco)
    self.processador = memoria_ram

  def exibir_informacoes(self):
    super().exibir_informacoes()
    print(f"Memória RAM: {self.processador}")


class Televisao(ProdutoEletronico):
  def __init__(self, nome, marca, preco, tamanho_tela):
    super().__init__(nome, marca, preco)
    self.tamanho_tela = tamanho_tela

  def exibir_informacoes(self):
    super().exibir_informacoes()
    print(f"Tamanho da Tela: {self.tamanho_tela}")
  