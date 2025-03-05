# Função para calcular a produtividade da colheita
def calcular_produtividade(quantidade, area):
    return quantidade / area

# Exemplo de uso
quantidade_colhida = 1000  # em kg
area_plantio = 10  # em hectares
produtividade = calcular_produtividade(quantidade_colhida, area_plantio)
print(f"Produtividade: {produtividade} kg/hectare")
