# Ввод чисел
numbers = list(map(int, input("Введите числа через запятую: ").split(',')))
print("Введены числа:", numbers)

even_numbers = []

# Проверка чисел на четность
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print("Четные числа:", even_numbers)

# Сортировка чисел "Выбором"
for i in range(len(numbers)):
    min_idx = i
    for j in range(i + 1, len(numbers)):
        if numbers[min_idx] > numbers[j]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print("Максимальное число:", numbers[-1])
print("Минимальное число:", numbers[0])
print("Отсортированный список:", numbers)
