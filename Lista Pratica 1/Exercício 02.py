#Soma dos algarismos de um número. Escreva uma função recursiva que retorna a soma dos
#algarismos de um número informado como parâmetro. Por exemplo se n= 1203, a função retorna 6,
#se n= 2131, a função retorna 7.


n = int(input('Digite o numero: '))


def digitalSum(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + digitalSum(n // 10)


print(digitalSum(n))
