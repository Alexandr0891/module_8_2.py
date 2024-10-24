# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
            #print(result)
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорекктный тип данных для подсчёта суммы - {i})')
    return result, incorrect_data

# numbers = "1, 2, 3"
# print(personal_sum(numbers))
def calculate_average(numbers):
    try:
        result_1 = personal_sum(numbers)
        return result_1[0] / (len(numbers) - result_1[1])
    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc:
        return print(f'В numbers записан некорректный тип данных')
    if isinstance(numbers, int):
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')