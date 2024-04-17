import math
import sympy as sp

def count_unknown(pattern):
    # Число неизвестных пружин (количество символов '?')
    return pattern.count('?')

def calculate_possible_variants(unknown_count):
    # Количество возможных вариантов расстановки для неизвестных
    return 2 ** unknown_count

def is_valid_combination(pattern, group_sizes):
    # Проверка валидности комбинации
    groups = extract_groups(pattern)
    return groups == group_sizes

def sum_valid_combinations(combinations):
    # Итоговый результат - сумма всех валидных комбинаций
    return sum(combinations)

def extract_groups(pattern):
    # Разделение строки на группы поврежденных пружин
    groups = []
    current_group_length = 0

    for char in pattern:
        if char == '#':
            current_group_length += 1
        elif current_group_length > 0:
            groups.append(current_group_length)
            current_group_length = 0

    if current_group_length > 0:
        groups.append(current_group_length)

    return groups

# Пример использования функций:

# Число неизвестных пружин в шаблоне
pattern = "###?##"
unknown_count = count_unknown(pattern)
print("Число неизвестных пружин:", unknown_count)

# Количество возможных вариантов расстановки для неизвестных
possible_variants = calculate_possible_variants(unknown_count)
print("Количество возможных вариантов расстановки:", possible_variants)

# Проверка валидности комбинации
pattern_example = "?#?#?#?#?#?#?#?"
group_sizes_example = [1,3,1,6]
valid = is_valid_combination(pattern_example, group_sizes_example)
print("Проверка валидности комбинации:", valid)

# Итоговый результат - сумма всех валидных комбинаций
combinations = [2, 3, 1, 0, 4]
result = sum_valid_combinations(combinations)
print("Итоговый результат:", result)
