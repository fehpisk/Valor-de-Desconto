valorinicial = float(input("Informe o valor da compra: R$"))


#Indicação de porcentagem de acordo com o valor da compra

if valorinicial < 200.00:
   percentual_desconto = 0.05
   
else:
   
   if valorinicial < 300.00:
      percentual_desconto = 0.10
   
   else:
      percentual_desconto = 0.15

#Fórmulas dos cálculos de porcentagem e valor do desconto

valor_desconto = valorinicial * percentual_desconto


#Valor final com desconto já aplicado

valor_total = valorinicial - valor_desconto


#Resultados...

print("\n--- Descontos Aplicados ---")
print(f"Valor da compra: R$ {valorinicial:.2f}")
print(f"Parabens! Voce recebeu um desconto de ({percentual_desconto * 100:.0f}%): Corresponde a R$ {valor_desconto:.2f} de desconto.")
print(f"Com o desconto, o total a pagar: R${valor_total:.2f}")