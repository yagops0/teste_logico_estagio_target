'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''

def sequencia_fibonacci(numero):
    sequencia = []
    f1 = 0
    f2 = 1
    
    sequencia.append(f1)
    sequencia.append(f2)
    for i in range(numero):
        soma = f1 + f2
        sequencia.append(soma)
        
        f1 = f2
        f2 = soma
        
    return sequencia
             
print("="*50)

numero = int(input("Digite um número para calcular e saber se ele pertence à sequência de fibonacci ou não: "))

print("="*50)

if numero in sequencia_fibonacci(numero):
    print(f"O número {numero} PERTENCE à sequência de fibonacci!")
else:
    print(f"O número {numero} NÃO pertence a sequência de fibonacci!")
    
print("="*50)
print("SEQUÊNCIA")
print("="*50)
print(sequencia_fibonacci(numero))
print("="*50)
