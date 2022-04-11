#Soma dos números naturais. Escreva uma função recursiva que retorna a soma dos n primeiros
#números naturais, onde n é um número informado como parâmetro. Por exemplo se n= 5, a função
#retorna 15, se n= 6, a função retorna 21.

n = int(input("Digite um número positivo e inteiro: "))
soma = 0
if n > 0:
  for i in range(n+1):
    soma = soma + i
    print(f"para n = ",i," a soma é: ", soma)
print("Somando os ",n," primeiros números naturais, temos: ",soma)




