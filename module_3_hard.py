def calculate_structure_sum(data_structure):
    total_sum = 0
    for element in data_structure:
        if isinstance(element, list):
            total_sum += sum(calculate_structure_sum(element))
        elif isinstance(element, dict):
            total_sum += sum(element.values())
        elif isinstance(element, tuple):
            for sub_element in element:
                if isinstance(sub_element, (list, dict, tuple)):
                    total_sum += calculate_structure_sum(sub_element)
                elif isinstance(sub_element, str):
                    total_sum += len(sub_element)
        elif isinstance(element, str):
            total_sum += len(element)
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)