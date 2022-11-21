n = int(input(f'Digite a quantidade de números que deseja a combinações:'))
noteValue = []
for i in range(n):
    noteValue.append(str(input(f'Digite caracteres:')))

powerSet = []
for i in range(1 << n):
    sub = []
    for j in range(n):
        if (i & (1 << j) > 0):
            sub.append(noteValue[j])

    powerSet.append(sub)

print(f'Todas as combinações possíveis são:', powerSet)