def numero_primo(i):
    primos = []
    for x in range(2,i+1):
        e_primo = 0
        divisors = 1
        for a in primos:
            if x%a == 0:
                e_primo = 1
                divisors = divisors + 1
            else:
                e_primo = 0
        if e_primo == 0 and divisors == 1:
            primos.append(x)
    print(primos)

parameter = int(input('Digite um número: '))
numero_primo(parameter)
