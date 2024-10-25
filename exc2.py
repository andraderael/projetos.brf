print("█████████████Bem-vindos à Pizzaria do Israel!███████████████")
print("█████████████████████████CARDÁPIO███████████████████████████")
print("-------------------------------------------------------------")
print("---█ TAMANHO █ Pizza Salgada (PS)  █  Pizza Doce (PD)   █---")
print("---█    P    █        R$30         █        R$34        █---")    
print("---█    M    █        R$45         █        R$48        █---")
print("---█    G    █        R$60         █        R$66        █---")
print("████████████████████████████████████████████████████████████")

totalpedido = 0

while True:
    #escolha do sabor
    sabor = input("Digite o sabor (PS para Pizza Salgada, PD para Pizza Doce): ").upper()
    
    #verificando se o sabor é válido
    if sabor != 'PS' and sabor != 'PD':
        print("Sabor inválido.")
        continue

    #escolha do tamanho
    tamanho = input("Digite o tamanho da pizza (P/M/G): ").upper()
    
    #verificando se o tamanho é válido ou não
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido.")
        continue 

    #calcular o preço
    if sabor == 'PS':
        if tamanho == 'P':
            preco = 30
        elif tamanho == 'M':
            preco = 45
        elif tamanho == 'G':
            preco = 60
    elif sabor == 'PD':
        if tamanho == 'P':
            preco = 34
        elif tamanho == 'M':
            preco = 48
        elif tamanho == 'G':
            preco = 66

    #acumulando o total do valor 
    totalpedido += preco
    print(f"O valor da sua pizza é R$,", preco ,". Total acumulado:", totalpedido , "R$")

    #perguntar se o cliente deseja algo mais 
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if continuar == 'N':
        break  

#valor total do pedio
print(f"Obrigado pelo pedido! O total a pagar é ", totalpedido , "R$")
