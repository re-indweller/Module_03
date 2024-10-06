# def calculate_structure_sum(data_structure):
    # total_sum = 0
    #
    # for element in data_structure:
    #     if isinstance(element, list):
    #         total_sum += calculate_structure_sum(element)
    #     elif isinstance(element, dict):
    #         total_sum += sum(element.values())
    #         total_sum += sum(len(key) for key in element.keys()) # добавил сюда проверку
    #
    #     elif isinstance(element, tuple):
    #         for sub_element in element:
    #             if isinstance(sub_element, (list, dict, tuple)):
    #                 total_sum += calculate_structure_sum(sub_element)
    #             elif isinstance(sub_element, str):
    #                 total_sum += len(sub_element)
    #             elif isinstance(sub_element, dict):
    #                 total_sum += sum(len(key) for key in sub_element.keys()) # добавил сюда проверку
    #     elif isinstance(element, str):
    #         total_sum += len(element)
    #
    # return total_sum
def calculate_structure_sum(data_structure):
    summa = 0
    # Прописываем условие при помощи цикла 1 summa для key и value
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
            # иначе выполняеться цикл 2 add к summa - список,кортэж,множества
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
            # иначе выполняеться действие 3 add к summa - целое число и число с плавающей запятой
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
        # иначе выполняеться действие 4 add k summa - фу-цию len
    elif isinstance(data_structure, str):
        summa += len(data_structure)
        # возврат из функции значения summa
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)