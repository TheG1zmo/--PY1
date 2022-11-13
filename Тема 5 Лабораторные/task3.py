import random
def get_unique_list_numbers() -> list[int]:
    min_ = -10
    max_ = 10
    list1 = []
    l = 15
    while len(list1) != l :
        list1 = list (list1)
        list1.append(random.randint(min_, max_))
        list1 = set (list1)
    return list1# TODO написать функцию для получения списка уникальных целых чисел
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
