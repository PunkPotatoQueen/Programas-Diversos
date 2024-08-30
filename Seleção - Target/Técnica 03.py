import json

def calcular_faturamento(faturamento_diario):
    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
    
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)
    
    return min(dias_com_faturamento), max(dias_com_faturamento), dias_acima_da_media

with open('faturamento.json', 'r') as file:
    dados = json.load(file)
    faturamento_diario = dados['faturamento_diario']
    
menor, maior, dias_acima = calcular_faturamento(faturamento_diario)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima}")
