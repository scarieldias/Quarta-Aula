# Declaracao de Variavel

saldoInicial = 50
custoRefrigerante = 8
custoPao = 4
custoMortadela = 39.99
valorCompra = (custoRefrigerante * 2) + custoPao + ((custoMortadela / 1000) * 300)

saldoFinal = saldoInicial - valorCompra

print(f"Jose chegou com R$ {saldoInicial} e saiu com R$ {saldoFinal}")