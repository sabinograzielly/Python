from produto import Produto

class Loja:
    def __init__(self):
        self.estoque = []

    def adicionar_produto(self, nome, preco, quantidade):
        produto = Produto(nome, preco, quantidade)
        self.estoque.append(produto)

    def exibir_produtos(self):
        for i, produto in enumerate(self.estoque):
            print(f"{i+1}. {produto.nome} - R${produto.preco:.2f} - Estoque: {produto.quantidade}")

    def buscar_produto(self, indice):
        if 0 <= indice < len(self.estoque):
            return self.estoque[indice]
        return None
