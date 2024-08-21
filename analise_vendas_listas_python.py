def analise_vendas(vendas):
    # Calcula o total de vendas
    total_vendas = sum(vendas)
    # Calcula a média mensal de vendas
    media_vendas = total_vendas / len(vendas)
    
    # Retorna o resultado formatado como solicitado
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("")
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

# Obtém a lista de vendas
vendas = obter_entrada_vendas()
# Exibe o resultado da análise
print(analise_vendas(vendas))
