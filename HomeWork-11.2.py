def generate_cube_numbers(end):
    """
    Генератор кубів натуральних чисел до end включно.
    :yield: Куби натуральних чисел.
    :param end: Верхня межа діапазону (включно).
    """
    n = 2
    while True:
        cube = n ** 3
        if cube > end:
            break
        yield cube
        n += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("Ok")