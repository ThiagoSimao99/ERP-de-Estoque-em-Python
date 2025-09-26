def gerar_id(produtos):
    if not produtos:
        return 1
    return max(p['id'] for p in produtos) + 1

def cadastrar_produto(produtos):
    print("\n== Cadastrar Produto ==")
    nome = input("Nome: ").strip()
    if nome == "":
        print("Nome inválido. Cadastro cancelado.")
        return

    categoria = input("Categoria: ").strip() or "Sem categoria"

    while True:
        preco_str = input("Preço (ex: 19.90): ").strip().replace(',', '.')
        try:
            preco = float(preco_str)
            if preco < 0:
                print("Preço não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número (ex: 19.90).")

    while True:
        qtd_str = input("Quantidade inicial (inteiro): ").strip()
        if qtd_str == "":
            quantidade = 0
            break
        try:
            quantidade = int(qtd_str)
            if quantidade < 0:
                print("Quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    novo = {
        'id': gerar_id(produtos),
        'nome': nome,
        'categoria': categoria,
        'preco': preco,
        'quantidade': quantidade
    }
    produtos.append(novo)
    print(f"Produto cadastrado com sucesso! ID = {novo['id']}")

def encontrar_por_id(produtos, id_busca):
    for p in produtos:
        if p['id'] == id_busca:
            return p
    return None

def remover_produto(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return
    print("\n== Excluir Produto ==")
    op = input("Remover por (1) ID ou (2) Nome? [1/2]: ").strip()
    if op == "1":
        try:
            id_str = input("Digite o ID do produto: ").strip()
            id_int = int(id_str)
        except ValueError:
            print("ID inválido.")
            return
        produto = encontrar_por_id(produtos, id_int)
        if produto:
            produtos.remove(produto)
            print(f"Produto ID {id_int} removido.")
        else:
            print("Produto com esse ID não encontrado.")
    elif op == "2":
        nome = input("Digite o nome do produto (ou parte dele): ").strip().lower()
        encontrados = [p for p in produtos if nome in p['nome'].lower()]
        if not encontrados:
            print("Nenhum produto encontrado com esse nome.")
            return
        if len(encontrados) == 1:
            produtos.remove(encontrados[0])
            print(f"Produto '{encontrados[0]['nome']}' removido.")
        else:
            print("Foram encontrados vários produtos:")
            for p in encontrados:
                print(f"ID {p['id']} - {p['nome']} ({p['categoria']}) - qtd: {p['quantidade']}")
            try:
                id_escolhido = int(input("Digite o ID do produto que deseja remover: ").strip())
            except ValueError:
                print("ID inválido. Operação cancelada.")
                return
            produto = encontrar_por_id(produtos, id_escolhido)
            if produto and produto in encontrados:
                produtos.remove(produto)
                print(f"Produto ID {id_escolhido} removido.")
            else:
                print("ID não corresponde aos resultados listados. Cancelado.")
    else:
        print("Opção inválida.")

def mostrar_relatorio(produtos):
    print("\n== Relatório de Produtos ==")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    print(f"{'ID':<4} {'Nome':<25} {'Categoria':<15} {'Preço':>8} {'Qtd':>5}  Observação")
    print("-"*70)
    for p in produtos:
        obs = ""
        if p['quantidade'] < 5:
            obs = "!! Estoque baixo !!"
        preco_format = f"R$ {p['preco']:.2f}"
        print(f"{p['id']:<4} {p['nome'][:24]:<25} {p['categoria'][:14]:<15} {preco_format:>8} {p['quantidade']:>5}  {obs}")

def menu():
    produtos = []
    while True:
        print("\n=== Mini-ERP de Estoque ===")
        print("1 - Cadastrar produto")
        print("2 - Excluir produto")
        print("3 - Mostrar relatório de produtos")
        print("4 - Sair")
        escolha = input("Escolha uma opção [1-4]: ").strip()
        if escolha == "1":
            cadastrar_produto(produtos)
        elif escolha == "2":
            remover_produto(produtos)
        elif escolha == "3":
            mostrar_relatorio(produtos)
        elif escolha == "4":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
