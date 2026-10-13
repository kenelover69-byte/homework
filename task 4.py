def process_list(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    average = total / len(numbers) if len(numbers) > 0 else 0
    return total, maximum, average

# Введення списку чисел від користувача
user_input = input("Введіть числа через пробіл: ")
nums = [float(x) for x in user_input.split()]

if nums:
    total_sum, max_val, avg_val = process_list(nums)
    print(f"Сума елементів: {total_sum}")
    print(f"Максимальний елемент: {max_val}")
    print(f"Середнє значення: {avg_val:.2f}")
else:
    print("Список порожній.")
