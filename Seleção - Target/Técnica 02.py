def pertence_fibonacci(num):
    fibonacci = [0, 1]

    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    if num in fibonacci:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

#Teste
print(pertence_fibonacci(78))
print(pertence_fibonacci(34))