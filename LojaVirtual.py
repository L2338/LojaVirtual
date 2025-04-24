class ProdutoInvalido(Exception):
    def __init__(self, codigo):
        super().__init__(f"Produto com código {codigo} não existe no catálogo.")

class QuantidadeInvalida(Exception):
    def __init__(self, quantidade):
        super().__init__(f"Quantidade inválida: {quantidade}. Deve ser um número positivo.")

class CarrinhoVazio(Exception):
    def __init__(self):
        super().__init__("O carrinho está vazio. Adicione produtos antes de finalizar a compra.")

class SaldoInsuficiente(Exception):
    def __init__(self, saldo, total):
        super().__init__(f"Saldo insuficiente. Tem €{saldo:.2f}, mas precisa de €{total:.2f}.")

class Loja:
    def __init__(self):
        self.catalogo = {
            1: ["T-shirt", 13.00],
            2: ["Calças de ganga", 40.00],
            3: ["Camisa", 30.00],
            4: ["Casaco", 60.00],
            5: ["Ténis", 45.00],
        }
        self.carrinho = {}
        self.saldo = 150.00

    def mostrar_produtos(self):
        print("\n--- Catálogo ---")
        for cod, (nome, preco) in self.catalogo.items():
            print(f"{cod}: {nome} - €{preco:.2f}")

    def adicionar_ao_carrinho(self):
        try:
            cod = int(input("Código do produto: "))
            if cod not in self.catalogo:
                raise ProdutoInvalido(cod)

            qtd = int(input("Quantidade: "))
            if qtd <= 0:
                raise QuantidadeInvalida(qtd)

            self.carrinho[cod] = self.carrinho.get(cod, 0) + qtd
            print(f"{qtd}x '{self.catalogo[cod][0]}' adicionado(s) ao carrinho.")
        except (ProdutoInvalido, QuantidadeInvalida) as e:
            print(f"Erro: {e}")
        except ValueError:
            print("Erro: introduza números válidos.")

    def ver_carrinho(self):
        if not self.carrinho:
            print("\nO carrinho está vazio.")
            return 0

        print("\n--- Carrinho ---")
        total = 0
        for cod, qtd in self.carrinho.items():
            nome, preco = self.catalogo[cod]
            subtotal = preco * qtd
            total += subtotal
            print(f"{nome} ({qtd}x) - €{subtotal:.2f}")
        print(f"Total: €{total:.2f}")
        return total

    def finalizar_compra(self):
        try:
            if not self.carrinho:
                raise CarrinhoVazio()

            total = self.ver_carrinho()
            if self.saldo < total:
                raise SaldoInsuficiente(self.saldo, total)

            self.saldo -= total
            self.carrinho.clear()
            print(f"\nCompra concluída com sucesso! Saldo restante: €{self.saldo:.2f}")
        except (CarrinhoVazio, SaldoInsuficiente) as e:
            print(f"Erro: {e}")

    def ver_saldo(self):
        print(f"Saldo atual: €{self.saldo:.2f}")

def menu():
    loja = Loja()
    print("Bem-vindo à Loja Virtual!")

    while True:
        print("\n1. Ver produtos")
        print("2. Adicionar ao carrinho")
        print("3. Ver carrinho")
        print("4. Finalizar compra")
        print("5. Ver saldo")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            loja.mostrar_produtos()
        elif escolha == "2":
            loja.adicionar_ao_carrinho()
        elif escolha == "3":
            loja.ver_carrinho()
        elif escolha == "4":
            loja.finalizar_compra()
        elif escolha == "5":
            loja.ver_saldo()
        elif escolha == "0":
            print("Obrigado por visitar a loja!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
