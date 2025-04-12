class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        if produto.quantidade >= quantidade:
            self.itens.append((produto, quantidade))
            produto.atualizar_estoque(quantidade)
        else:
            print("Estoque insuficiente.")

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco * quantidade
        return total

    def mostrar_carrinho(self):
        if not self.itens:
            print("Carrinho vazio.")
        for produto, quantidade in self.itens:
            print(f"{produto.nome} - R${produto.preco:.2f} x {quantidade}")

    def esvaziar(self):
        self.itens = []
