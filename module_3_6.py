data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_structure = 0


def calculate_structure_sum(data):
    global sum_structure
    sum_elements = 0
    for i in data:
        if isinstance(i, list):
            calculate_structure_sum(i)
        if isinstance(i, dict):
            calculate_structure_sum(i.keys())
            calculate_structure_sum(i.values())
        if isinstance(i, tuple):
            calculate_structure_sum(i)
        if isinstance(i, set):
            calculate_structure_sum(i)
        if isinstance(i, int):
            sum_elements += i
        if isinstance(i, str):
            sum_elements += len(i)
    sum_structure += sum_elements


calculate_structure_sum(data_structure)
print(sum_structure)
