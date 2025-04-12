from loja import Loja
from carrinho import Carrinho

loja = Loja()
carrinho = Carrinho()

loja.adicionar_produto("Camiseta", 50.0, 10)
loja.adicionar_produto("Calça", 120.0, 5)
loja.adicionar_produto("Tênis", 200.0, 3)

while True:
    print("\n MENU LOJA ")
    print("1. Ver produtos disponíveis")
    print("2. Adicionar produto ao carrinho")
    print("3. Aplicar desconto a um produto")
    print("4. Ver carrinho")
    print("5. Finalizar compra")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        loja.exibir_produtos()

    elif opcao == "2":
        loja.exibir_produtos()
        indice = int(input("Digite o número do produto: ")) - 1
        produto = loja.buscar_produto(indice)
        if produto:
            qtd = int(input("Quantidade: "))
            carrinho.adicionar_produto(produto, qtd)
        else:
            print("Produto inválido.")

    elif opcao == "3":
        loja.exibir_produtos()
        indice = int(input("Número do produto para aplicar desconto: ")) - 1
        produto = loja.buscar_produto(indice)
        if produto:
            percentual = float(input("Percentual de desconto: "))
            produto.aplicar_desconto(percentual)
            print("Desconto aplicado.")
        else:
            print("Produto inválido.")

    elif opcao == "4":
        carrinho.mostrar_carrinho()

    elif opcao == "5":
        if not carrinho.itens:
            print("O carrinho está vazio. Adicione produtos antes de finalizar a compra.")
        else:
            print("\nFormas de pagamento:")
            print("1. Dinheiro (10% de desconto)")
            print("2. Pix (10% de desconto)")
            print("3. Cartão (5% de acréscimo em compras parceladas)")

        forma = input("Escolha a forma de pagamento (1/2/3): ")

        total_original = carrinho.calcular_total()
        total_final = total_original  # começa igual

        print(f"\nValor original da compra: R${total_original:.2f}")

        if forma == "1" or forma == "2":
            total_final *= 0.9
            print("Desconto de 10% aplicado.")

        elif forma == "3":
            parcelas = int(input("Em quantas vezes deseja parcelar? "))
            if parcelas > 1:
                total_final *= 1.05
                print(f"Acréscimo de 5% aplicado para pagamento parcelado em {parcelas}x.")
            else:
                print("Pagamento à vista no cartão. Sem acréscimos ou descontos.")

        print(f"Total com desconto/acréscimo: R${total_final:.2f}")
        valor_pago = float(input("Digite o valor pago: "))

        if valor_pago >= total_final:
            troco = valor_pago - total_final
            print(f"Pagamento aprovado. Troco: R${troco:.2f}")
            carrinho.esvaziar()
        else:
            print("Pagamento insuficiente.")

    elif opcao == "6":
        break
    else:
        print("Opção inválida.")
