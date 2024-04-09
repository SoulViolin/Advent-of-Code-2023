def count_combinations(pattern, group_sizes):
    unknown_count = pattern.count('?')  # количество неизвестных пружин
    possible_variants = 2 ** unknown_count  # количество возможных вариантов расстановки для неизвестных

    valid_combinations = 0

    # Генерируем все возможные комбинации для неизвестных пружин
    for variant in range(possible_variants):
        binary_representation = f'{variant:0{unknown_count}b}'  # представляем вариант в двоичной системе

        # Создаем новую строку с учетом расстановки неизвестных пружин
        new_pattern = list(pattern)
        index = 0
        for i in range(len(new_pattern)):
            if new_pattern[i] == '?':
                # Заменяем '?' на '.' или '#' в соответствии с битом в двоичном представлении
                new_pattern[i] = '.' if binary_representation[index] == '0' else '#'
                index += 1

        # Проверяем, соответствует ли новая строка заданным группам поврежденных пружин
        if is_valid_combination(''.join(new_pattern), group_sizes):
            valid_combinations += 1

    return valid_combinations

def is_valid_combination(pattern, group_sizes):
    groups = []
    current_group_length = 0

    # Разделяем строку на группы поврежденных пружин
    for char in pattern:
        if char == '#':
            current_group_length += 1
        elif current_group_length > 0:
            groups.append(current_group_length)
            current_group_length = 0

    # Добавляем последнюю группу
    if current_group_length > 0:
        groups.append(current_group_length)

    # Проверяем, соответствует ли порядок групп заданным размерам
    return groups == group_sizes

# Примеры использования:

# Строка с неизвестными пружинами и заданными группами поврежденных пружин
pattern = '?#?#?#?#?#?#?#?'
group_sizes = [1,3,1,6]

# Подсчет количества различных вариантов комбинаций
result = count_combinations(pattern, group_sizes)
print(f"Количество различных комбинаций: {result}")
